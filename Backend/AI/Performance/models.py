from pydantic import BaseModel


class PerformanceRequest(BaseModel):
    subject: str
    topics: dict[str, float]


class PerformanceResult(BaseModel):
    subject: str
    overall_performance: float
    strong_concepts: list[str]
    weak_concepts: list[str]
    topics_requiring_attention: list[str]