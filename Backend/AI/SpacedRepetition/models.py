from typing import List, Optional
from pydantic import BaseModel


class SpacedRepetitionRequest(BaseModel):
    score: float
    current_interval: int = 0
    pass_threshold: float = 70.0


class SpacedRepetitionResult(BaseModel):
    score: float
    current_interval: int
    next_review_in_days: int
    passed: bool
    stage: int
    total_stages: int = 4
    interval_ladder: List[int] = [1, 3, 7, 30]
    message: str
    is_mastered: bool = False
