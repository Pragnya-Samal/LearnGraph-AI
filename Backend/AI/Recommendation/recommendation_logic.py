import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=groq_api_key, timeout=2.0) if groq_api_key else None


def explain_wrong_answers(questions: list[dict]):

    # Find only the wrong answers
    wrong_answers = []

    for item in questions:
        student_ans = item.get("your_answer", item.get("student_answer"))
        if student_ans != item["correct_answer"]:
            wrong_answers.append({
                "question": item["question"],
                "student_answer": student_ans,
                "correct_answer": item["correct_answer"]
            })

    # If everything is correct
    if not wrong_answers:
        return {
            "wrong_answers": [],
            "message": "All answers are correct. No explanation is needed."
        }

    # Send wrong answers to Groq if client is available
    if client:
        prompt = f"""
You are an AI learning assistant.

Analyze the following wrong answers from a student's assessment.

For EACH wrong answer:
1. Show what the student answered.
2. Show the correct answer.
3. Explain clearly why the correct answer is correct.
4. Explain why the student's answer is wrong.
5. Keep the explanation educational and easy to understand.

Do NOT explain questions that were answered correctly.

Wrong answers:

{json.dumps(wrong_answers, indent=2)}

Return ONLY valid JSON in this format:

{{
    "wrong_answers": [
        {{
            "question": "Question",
            "student_answer": "Student answer",
            "correct_answer": "Correct answer",
            "explanation": "Detailed explanation"
        }}
    ]
}}
"""
        try:
            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,
                timeout=3.0,
                response_format={
                    "type": "json_object"
                }
            )

            response_text = response.choices[0].message.content
            return json.loads(response_text)
        except Exception:
            pass

    # Educational fallback explanations if LLM call is unavailable
    fallback_explanations = []
    for wa in wrong_answers:
        fallback_explanations.append({
            "question": wa["question"],
            "student_answer": wa["student_answer"],
            "correct_answer": wa["correct_answer"],
            "explanation": (
                f"The correct answer is '{wa['correct_answer']}' because it accurately represents the core principle. "
                f"'{wa['student_answer']}' is incorrect for this concept."
            )
        })

    return {
        "wrong_answers": fallback_explanations
    }
