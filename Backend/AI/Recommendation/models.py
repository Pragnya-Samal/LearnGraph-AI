from pydantic import BaseModel


class QuestionResult(BaseModel):
    question: str
    options: list[str]
    student_answer: str
    correct_answer: str


class AssessmentReviewRequest(BaseModel):
    subject: str
    topic: str
    questions: list[QuestionResult]


class WrongAnswerExplanation(BaseModel):
    question: str
    student_answer: str
    correct_answer: str
    explanation: str


class AssessmentReviewResult(BaseModel):
    subject: str
    topic: str
    wrong_answers: list[WrongAnswerExplanation]
    recommendation: str | None = None