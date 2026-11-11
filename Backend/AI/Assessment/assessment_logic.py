from .questions import questions
from .models import AssessmentResult


def evaluate_assessment(
    subject: str,
    topic: str,
    answers: list[str]
) -> AssessmentResult:

    topic_questions = questions.get(subject, {}).get(topic, [])
    if not topic_questions:
        topic_questions = questions.get("OOPS", {}).get("Inheritance", [])

    if len(topic_questions) < 30:
        backup = questions.get("OOPS", {}).get("Inheritance", [])
        pool = list(topic_questions) + [q for q in backup if q not in topic_questions]
        topic_questions = (pool * ((30 // len(pool)) + 1))[:30]
    else:
        topic_questions = topic_questions[:30]

    score = 0

    for question, student_answer in zip(topic_questions, answers):

        # Convert selected option number into actual answer text
        try:
            answer_index = int(student_answer)
            selected_answer = question["options"][answer_index]
        except (ValueError, IndexError):
            selected_answer = student_answer

        # Compare selected answer with correct answer
        if selected_answer == question["correct_answer"]:
            score += 1

    total_questions = len(topic_questions)

    if total_questions == 0:
        knowledge_level = "No assessment available"
    else:
        percentage = (score / total_questions) * 100

        if percentage < 40:
            knowledge_level = "Beginner"
        elif percentage < 70:
            knowledge_level = "Intermediate"
        else:
            knowledge_level = "Advanced"

    return AssessmentResult(
        subject=subject,
        topic=topic,
        score=score,
        total_questions=total_questions,
        knowledge_level=knowledge_level
    )