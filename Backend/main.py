from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List, Dict, Any

from AI.Assessment.assessment_generator import (
    generate_subject_assessment,
    generate_topic_quiz,
    generate_assessment,
)
from AI.Assessment.assessment_logic import evaluate_assessment
from AI.Assessment.assessment_store import (
    save_assessment,
    get_assessment,
    get_assessment_metadata,
)
from AI.Assessment.models import (
    AssessmentRequest,
    AssessmentSubmission,
)
from AI.Assessment.questions import questions
from AI.Performance.models import PerformanceRequest
from AI.Performance.performance_logic import analyze_performance
from AI.Recommendation.models import AssessmentReviewRequest
from AI.Recommendation.recommendation_logic import explain_wrong_answers
from AI.SpacedRepetition.models import SpacedRepetitionRequest
from AI.SpacedRepetition.spaced_repetition_logic import calculate_next_review

import database

app = FastAPI(title="Personalized Learning Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Personalized Learning Backend is running"
    }


# ==============================================================================
# SUBJECT-LEVEL ASSESSMENT ENDPOINT
# Tests the student across all hierarchical topics in the subject.
# Questions 1 to 30 are strictly ordered from Easy to Hard.
# Option choices are randomized uniquely on every request.
# ==============================================================================
@app.get("/assessment/generate/subject/{subject}")
def generate_subject_level_assessment(subject: str, count: int = 30):
    assessment_data = generate_subject_assessment(subject, number_of_questions=count)
    raw_questions = assessment_data.get("questions", [])

    if not raw_questions:
        raise HTTPException(status_code=404, detail=f"No questions found for subject '{subject}'")

    assessment_id = save_assessment(
        questions=raw_questions,
        subject=assessment_data["subject"],
        topic="Subject Comprehensive Assessment",
        is_subject_level=True
    )

    # Hide correct answers from student payload, include difficulty
    student_questions = []
    for idx, q in enumerate(raw_questions):
        student_questions.append({
            "id": idx,
            "question": q["question"],
            "options": q["options"],
            "topic": q.get("topic", "General"),
            "difficulty": q.get("difficulty", "Easy")
        })

    return {
        "assessment_id": assessment_id,
        "subject": assessment_data["subject"],
        "is_subject_level": True,
        "total_questions": len(student_questions),
        "questions": student_questions
    }


# ==============================================================================
# TOPIC-LEVEL SPACED REPETITION QUIZ ENDPOINT
# Tests a specific learned topic with questions 1 to 30 in order Easy to Hard.
# ==============================================================================
@app.get("/assessment/generate/{subject}/{topic}")
def generate_topic_spaced_repetition_quiz(subject: str, topic: str, count: int = 30):
    quiz_data = generate_topic_quiz(subject, topic, number_of_questions=count)
    raw_questions = quiz_data.get("questions", [])

    if not raw_questions:
        raise HTTPException(status_code=404, detail=f"No questions found for topic '{topic}' in subject '{subject}'")

    assessment_id = save_assessment(
        questions=raw_questions,
        subject=quiz_data["subject"],
        topic=quiz_data["topic"],
        is_subject_level=False
    )

    # Hide correct answers from student payload, include difficulty
    student_questions = []
    for idx, q in enumerate(raw_questions):
        student_questions.append({
            "id": idx,
            "question": q["question"],
            "options": q["options"],
            "topic": q.get("topic", topic),
            "difficulty": q.get("difficulty", "Easy")
        })

    return {
        "assessment_id": assessment_id,
        "subject": quiz_data["subject"],
        "topic": quiz_data["topic"],
        "is_subject_level": False,
        "total_questions": len(student_questions),
        "questions": student_questions
    }


# ==============================================================================
# ASSESSMENT SUBMISSION & TOPIC-LEVEL ANALYSIS
# Analyzes accuracy per topic, identifies weak topics, recommends next topic,
# suggests study materials, and advances the student once a topic is cleared.
# ==============================================================================
@app.post("/assessment/submit")
def submit_assessment(request: AssessmentSubmission):
    questions_list = get_assessment(request.assessment_id)
    metadata = get_assessment_metadata(request.assessment_id)

    if questions_list is None:
        raise HTTPException(status_code=404, detail="Assessment session not found or expired")

    subject_name = metadata.get("subject", "OOPS")
    topic_name = metadata.get("topic", "General")
    is_subject_level = metadata.get("is_subject_level", False)

    question_results = []
    correct_count = 0
    total_questions = len(questions_list)

    # Map to track accuracy per topic
    topic_breakdown: Dict[str, Dict[str, Any]] = {}

    for i, question in enumerate(questions_list):
        student_answer = request.answers[i] if i < len(request.answers) else ""
        correct_answer = question["correct_answer"]
        q_topic = question.get("topic", topic_name)

        is_correct = (str(student_answer).strip().lower() == str(correct_answer).strip().lower())

        if is_correct:
            correct_count += 1

        if q_topic not in topic_breakdown:
            topic_breakdown[q_topic] = {
                "topic": q_topic,
                "total": 0,
                "correct": 0,
                "wrong": 0,
                "wrong_questions": []
            }

        topic_breakdown[q_topic]["total"] += 1
        if is_correct:
            topic_breakdown[q_topic]["correct"] += 1
        else:
            topic_breakdown[q_topic]["wrong"] += 1
            topic_breakdown[q_topic]["wrong_questions"].append({
                "question": question["question"],
                "your_answer": student_answer,
                "correct_answer": correct_answer,
                "explanation": question.get("explanation", "")
            })

        question_results.append({
            "question": question["question"],
            "options": question["options"],
            "your_answer": student_answer,
            "correct_answer": correct_answer,
            "is_correct": is_correct,
            "topic": q_topic,
            "difficulty": question.get("difficulty", "Easy"),
            "explanation": question.get("explanation", "")
        })

    # Compute percentages for each topic
    weak_topics = []
    passed_topics = []
    for t_name, t_stats in topic_breakdown.items():
        pct = round((t_stats["correct"] / t_stats["total"]) * 100, 1) if t_stats["total"] > 0 else 0.0
        t_stats["percentage"] = pct
        t_stats["passed"] = (pct >= 70.0)

        if not t_stats["passed"]:
            weak_topics.append(t_stats)
        else:
            passed_topics.append(t_stats)

    overall_percentage = round((correct_count / total_questions) * 100, 1) if total_questions > 0 else 0.0

    if overall_percentage < 40:
        knowledge_level = "Beginner"
    elif overall_percentage < 70:
        knowledge_level = "Intermediate"
    else:
        knowledge_level = "Advanced"

    # Explanations for wrong answers
    explanation_result = explain_wrong_answers(question_results)

    # -------------------------------------------------------------------------
    # Recommendation & Progression Logic
    # -------------------------------------------------------------------------
    hierarchy = database.get_subject_hierarchy(subject_name)
    recommended_topic_data = None
    next_topic_data = None
    topic_cleared = False
    spaced_result = None
    next_review_days = 1
    next_review_date = None

    if is_subject_level:
        # Subject assessment: identify weak topic in hierarchical order to recommend for learning
        weak_topic_names = {w["topic"].lower(): w for w in weak_topics}

        # Find first weak topic in hierarchical sequence (Easy to Hard)
        selected_weak_topic_name = None
        for h_topic in hierarchy:
            if h_topic["name"].lower() in weak_topic_names:
                selected_weak_topic_name = h_topic["name"]
                break

        # Fallback if names didn't match directly
        if not selected_weak_topic_name and weak_topics:
            selected_weak_topic_name = weak_topics[0]["topic"]

        # If student passed everything (100%), recommend the first unmastered/advanced topic in hierarchy
        if not selected_weak_topic_name:
            if hierarchy:
                selected_weak_topic_name = hierarchy[-1]["name"]
            else:
                selected_weak_topic_name = "Classes and Objects"

        # Fetch curated study materials (YouTube & Websites) for the recommended topic
        materials = database.get_study_materials(subject_name, selected_weak_topic_name)

        # Get metadata from hierarchy
        h_match = next((h for h in hierarchy if h["name"].lower() == selected_weak_topic_name.lower()), None)

        recommended_topic_data = {
            "name": selected_weak_topic_name,
            "subject": subject_name,
            "difficulty": h_match["difficulty"] if h_match else "Intermediate",
            "display_order": h_match["display_order"] if h_match else 1,
            "description": h_match["description"] if h_match else f"Study materials for {selected_weak_topic_name}",
            "reason": (
                f"Based on your {subject_name} assessment, you missed questions in '{selected_weak_topic_name}'. "
                f"Reviewing these curated study materials will strengthen your foundation before advancing."
                if weak_topics else
                f"Great performance! Advance your mastery with '{selected_weak_topic_name}'."
            ),
            "materials": materials,
            "ready_for_quiz_prompt": True
        }

    else:
        # Topic-level Spaced Repetition Quiz: Record progress and advance if cleared
        try:
            db_progress = database.record_learner_progress(
                student_id=1,
                subject_name=subject_name,
                topic_name=topic_name,
                score=overall_percentage
            )
            spaced_result = db_progress.get("spaced_repetition") or calculate_next_review(overall_percentage, 0)
            next_review_days = db_progress.get("current_interval_days", spaced_result.get("next_review_in_days", 1))
            next_review_date = db_progress.get("next_review")
            topic_cleared = db_progress.get("topic_cleared", False)
            next_topic_data = db_progress.get("next_topic")
        except Exception:
            spaced_result = calculate_next_review(overall_percentage, 0)
            next_review_days = spaced_result.get("next_review_in_days", 1)
            topic_cleared = (overall_percentage >= 70.0)
            if topic_cleared:
                next_topic_data = database.get_next_topic_in_hierarchy(subject_name, topic_name)

    return {
        "assessment_id": request.assessment_id,
        "subject": subject_name,
        "topic": topic_name,
        "is_subject_level": is_subject_level,
        "score": correct_count,
        "total_questions": total_questions,
        "percentage": overall_percentage,
        "knowledge_level": knowledge_level,
        "topic_breakdown": topic_breakdown,
        "weak_topics": [w["topic"] for w in weak_topics],
        "passed_topics": [p["topic"] for p in passed_topics],
        "recommended_topic": recommended_topic_data,
        "topic_cleared": topic_cleared,
        "next_topic": next_topic_data,
        "question_results": question_results,
        "wrong_answers": explanation_result.get("wrong_answers", []),
        "next_review_in_days": next_review_days,
        "next_review_date": next_review_date,
        "spaced_repetition": spaced_result
    }


# ==============================================================================
# HIERARCHY AND STUDY MATERIAL ENDPOINTS
# ==============================================================================
@app.get("/subjects/database")
def get_database_subjects():
    """Return all subjects with their 10 hierarchical topics (Easy to Hard)."""
    return database.get_all_subjects()


@app.get("/subjects/{subject}/hierarchy")
def get_subject_topics_hierarchy(subject: str):
    """Return topics in hierarchical order for a subject."""
    return database.get_subject_hierarchy(subject)


@app.get("/subjects/{subject}/next-topic/{topic}")
def get_next_topic_step(subject: str, topic: str):
    """Retrieve the next sequential topic in a subject after clearing the current one."""
    next_topic = database.get_next_topic_in_hierarchy(subject, topic)
    return {
        "subject": subject,
        "current_topic": topic,
        "next_topic": next_topic
    }


@app.get("/study-materials/{subject}/{topic}")
def get_topic_study_materials(subject: str, topic: str, type: Optional[str] = None):
    materials = database.get_study_materials(subject, topic, type)
    return {
        "subject": subject,
        "topic": topic,
        "count": len(materials),
        "materials": materials
    }


@app.get("/student/{student_id}/progress")
def get_student_progress(student_id: int = 1):
    return database.get_student_progress_summary(student_id)


# ==============================================================================
# LEGACY & COMPATIBILITY ENDPOINTS
# ==============================================================================
@app.post("/assessment")
def legacy_assessment(request: AssessmentRequest):
    return evaluate_assessment(request.subject, request.topic, request.answers)


@app.get("/assessment/questions/{subject}/{topic}")
def get_questions_legacy(subject: str, topic: str):
    quiz_data = generate_topic_quiz(subject, topic, number_of_questions=30)
    questions_list = quiz_data.get("questions", [])

    result = []
    for q in questions_list:
        result.append({
            "question": q["question"],
            "options": q["options"]
        })

    return {
        "subject": subject,
        "topic": topic,
        "questions": result
    }


@app.post("/performance")
def performance_analysis(request: PerformanceRequest):
    return analyze_performance(request.subject, request.topics)


@app.post("/spaced-repetition")
def spaced_repetition_endpoint(request: SpacedRepetitionRequest):
    return calculate_next_review(request.score, request.current_interval)


@app.post("/assessment/review")
def review_assessment_endpoint(request: AssessmentReviewRequest):
    questions_list = [question.model_dump() for question in request.questions]
    result = explain_wrong_answers(questions_list)
    return {
        "subject": request.subject,
        "topic": request.topic,
        **result
    }


# Backwards compatibility aliases for tests
get_questions = get_questions_legacy
generate_initial_assessment = generate_topic_spaced_repetition_quiz
assessment = legacy_assessment

