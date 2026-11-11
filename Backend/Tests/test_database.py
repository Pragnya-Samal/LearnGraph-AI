import sys
from pathlib import Path

backend_dir = str(Path(__file__).resolve().parent.parent)
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

import database
from main import (
    get_topic_study_materials,
    get_database_subjects,
    get_student_progress,
    generate_initial_assessment,
    submit_assessment,
)
from AI.Assessment.models import AssessmentSubmission
from AI.Assessment.questions import questions


def test_database_initialization():
    conn = database.get_connection()
    cursor = conn.cursor()

    tables = ["subject", "topic", "student", "study_material", "quiz", "learner_topic_progress", "revision_record"]
    for t in tables:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (t,))
        row = cursor.fetchone()
        assert row is not None, f"Table {t} does not exist!"

    # Verify student exists
    cursor.execute("SELECT COUNT(*) FROM student")
    count = cursor.fetchone()[0]
    assert count > 0, "Default student should be seeded"


def test_study_materials_only_youtube_and_website():
    conn = database.get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT type FROM study_material")
    types = [row[0] for row in cursor.fetchall()]

    for t in types:
        assert t in ("youtube", "website"), f"Invalid material type '{t}' found! Only 'youtube' and 'website' allowed."

    # Test CHECK constraint rejection
    try:
        cursor.execute("INSERT INTO study_material (topic_id, title, type, url) VALUES (1, 'Bad File', 'pdf', 'http://test.pdf')")
        assert False, "Should have thrown a CHECK constraint failure for PDF"
    except Exception as e:
        assert "CHECK constraint failed" in str(e)


def test_study_materials_endpoint():
    res = get_topic_study_materials("OOPS", "Inheritance")
    assert res["subject"] == "OOPS"
    assert res["topic"] == "Inheritance"
    assert res["count"] >= 2
    for m in res["materials"]:
        assert m["type"] in ("youtube", "website")
        assert m["url"].startswith("http")


def test_assessment_persists_to_sql_database():
    # 1. Generate assessment (30 questions)
    gen = generate_initial_assessment("OOPS", "Inheritance")
    assert len(gen["questions"]) == 30
    aid = gen["assessment_id"]

    # 2. Submit with 28 correct answers
    inh = questions["OOPS"]["Inheritance"]
    answers = [q["correct_answer"] for q in inh]
    # 2 wrong
    answers[0] = [opt for opt in inh[0]["options"] if opt != inh[0]["correct_answer"]][0]
    answers[1] = [opt for opt in inh[1]["options"] if opt != inh[1]["correct_answer"]][0]

    sub = AssessmentSubmission(assessment_id=aid, answers=answers)
    res = submit_assessment(sub)

    assert res["score"] == 28
    assert res["total_questions"] == 30
    assert "next_review_in_days" in res
    assert res["next_review_date"] is not None

    # 3. Check database record
    conn = database.get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.score, p.status, r.current_interval_days
        FROM learner_topic_progress p
        JOIN topic t ON p.topic_id = t.topic_id
        JOIN revision_record r ON r.progress_id = p.progress_id
        WHERE t.name = 'Inheritance'
        ORDER BY r.revision_id DESC LIMIT 1
    """)
    row = cursor.fetchone()
    assert row is not None, "Progress or revision record was not created in database!"
    score, status, interval = row[0], row[1], row[2]
    assert score == round((28 / 30) * 100, 1)
    assert status in ("In Progress", "Mastered")
    assert interval in (1, 3, 7, 30)


def test_spaced_repetition_progression_and_regression_db():
    from database import record_learner_progress, get_connection

    # Dedicated student ID for isolated ladder testing
    s_id = 9999
    subject = "OOPS"
    topic = "Polymorphism"

    # Reset any existing test records for student 9999
    with get_connection() as conn:
        conn.execute("DELETE FROM revision_record WHERE student_id = ?", (s_id,))
        conn.execute("DELETE FROM learner_topic_progress WHERE student_id = ?", (s_id,))
        conn.commit()

    # 1. Initial attempt -> Tomorrow (1 day)
    p1 = record_learner_progress(student_id=s_id, subject_name=subject, topic_name=topic, score=80.0)
    assert p1["current_interval_days"] == 1, f"Expected 1 day, got {p1['current_interval_days']}"
    assert p1["spaced_repetition"]["passed"] is True

    # 2. Passed Day 1 quiz -> 3 days later
    p2 = record_learner_progress(student_id=s_id, subject_name=subject, topic_name=topic, score=85.0)
    assert p2["current_interval_days"] == 3, f"Expected 3 days, got {p2['current_interval_days']}"

    # 3. Passed Day 3 quiz -> 7 days later
    p3 = record_learner_progress(student_id=s_id, subject_name=subject, topic_name=topic, score=90.0)
    assert p3["current_interval_days"] == 7, f"Expected 7 days, got {p3['current_interval_days']}"

    # 4. FAILED Day 7 quiz (score 40% < 70%) -> drops back to previous interval: 3 days!
    p4 = record_learner_progress(student_id=s_id, subject_name=subject, topic_name=topic, score=40.0)
    assert p4["current_interval_days"] == 3, f"Expected drop back to 3 days on fail, got {p4['current_interval_days']}"
    assert p4["spaced_repetition"]["passed"] is False
    assert p4["status"] == "Needs Review"

    # 5. FAILED Day 3 quiz (score 30% < 70%) -> drops back to previous interval: 1 day (tomorrow)!
    p5 = record_learner_progress(student_id=s_id, subject_name=subject, topic_name=topic, score=30.0)
    assert p5["current_interval_days"] == 1, f"Expected drop back to 1 day on fail, got {p5['current_interval_days']}"


if __name__ == "__main__":
    test_database_initialization()
    test_study_materials_only_youtube_and_website()
    test_study_materials_endpoint()
    test_assessment_persists_to_sql_database()
    test_spaced_repetition_progression_and_regression_db()
    print("All SQL database and ER diagram tests passed successfully!")
