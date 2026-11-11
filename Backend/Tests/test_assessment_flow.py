import sys
from pathlib import Path

backend_dir = str(Path(__file__).resolve().parent.parent)
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from main import (
    home,
    get_questions,
    generate_initial_assessment,
    submit_assessment,
    assessment,
)
from AI.Assessment.models import (
    AssessmentRequest,
    AssessmentSubmission,
)
from AI.Assessment.questions import questions
from AI.Assessment.assessment_logic import evaluate_assessment


def test_home():
    res = home()
    assert res == {"message": "Personalized Learning Backend is running"}


def test_questions_bank_all_topics_30():
    for subject, topics in questions.items():
        for topic, q_list in topics.items():
            assert len(q_list) == 30, f"Expected 30 questions for {subject} - {topic}, found {len(q_list)}"
            for q in q_list:
                assert len(q["options"]) == 4, f"Options count error in {subject} - {topic}: {q}"
                assert q["correct_answer"] in q["options"], f"Correct answer not in options in {subject} - {topic}: {q}"


def test_get_questions():
    for subject, topics in questions.items():
        for topic in topics.keys():
            resp = get_questions(subject, topic)
            assert "questions" in resp
            assert len(resp["questions"]) == 30, f"Expected 30 questions for {subject} - {topic}, got {len(resp['questions'])}"
            for q in resp["questions"]:
                assert "question" in q
                assert "options" in q
                assert len(q["options"]) == 4


def test_assessment_flow():
    # 1. Generate assessment (should have 30 questions)
    gen = generate_initial_assessment("OOPS", "Inheritance")
    assert gen["subject"] == "OOPS"
    assert gen["topic"] == "Inheritance"
    assert len(gen["questions"]) == 30

    assessment_id = gen["assessment_id"]

    # 2. Submit assessment
    inh = questions["OOPS"]["Inheritance"]
    answers = [q["correct_answer"] for q in inh]
    # Intentionally make 5 wrong
    for i in range(5):
        wrong = [opt for opt in inh[i]["options"] if opt != inh[i]["correct_answer"]][0]
        answers[i] = wrong

    sub = AssessmentSubmission(assessment_id=assessment_id, answers=answers)
    result = submit_assessment(sub)

    assert result["score"] == 25
    assert result["total_questions"] == 30
    assert result["percentage"] == round((25 / 30) * 100, 1)
    assert result["knowledge_level"] == "Advanced"
    assert len(result["question_results"]) == 30
    assert len(result["wrong_answers"]) == 5


def test_static_evaluate():
    inh = questions["OOPS"]["Inheritance"]
    answers = [q["correct_answer"] for q in inh]
    req = AssessmentRequest(subject="OOPS", topic="Inheritance", answers=answers)
    res = assessment(req)
    assert res.score == 30
    assert res.total_questions == 30
    assert res.knowledge_level == "Advanced"


if __name__ == "__main__":
    test_home()
    test_questions_bank_all_topics_30()
    test_get_questions()
    test_assessment_flow()
    test_static_evaluate()
    print("All assessment tests passed successfully!")
