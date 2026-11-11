from typing import List
from pydantic import BaseModel


class AssessmentQuestion(BaseModel):
    question: str
    options: List[str]
    correct_answer: str


class AssessmentRequest(BaseModel):
    subject: str
    topic: str
    answers: List[str]


class AssessmentResult(BaseModel):
    subject: str
    topic: str
    score: int
    total_questions: int
    knowledge_level: str


class AssessmentSubmission(BaseModel):
    assessment_id: str
    answers: List[str]
