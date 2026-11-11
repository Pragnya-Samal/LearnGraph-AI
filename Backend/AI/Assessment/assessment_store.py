import uuid
from typing import Dict, Any, List, Optional

# In-memory storage for active generated assessments
assessments: Dict[str, Dict[str, Any]] = {}


def save_assessment(
    questions: List[Dict[str, Any]],
    subject: str = "OOPS",
    topic: Optional[str] = None,
    is_subject_level: bool = False
) -> str:
    """Save an assessment with full questions (including correct answers) and metadata."""
    assessment_id = str(uuid.uuid4())

    assessments[assessment_id] = {
        "questions": questions,
        "subject": subject,
        "topic": topic or "General",
        "is_subject_level": is_subject_level,
    }

    return assessment_id


def get_assessment(assessment_id: str) -> Optional[List[Dict[str, Any]]]:
    """Retrieve question list with answers for a given assessment ID."""
    data = assessments.get(assessment_id)
    if data is None:
        return None
    if isinstance(data, dict) and "questions" in data:
        return data["questions"]
    return data


def get_assessment_metadata(assessment_id: str) -> Dict[str, Any]:
    """Retrieve metadata (subject, topic, is_subject_level) for an assessment."""
    data = assessments.get(assessment_id)
    if isinstance(data, dict):
        return {
            "subject": data.get("subject", "OOPS"),
            "topic": data.get("topic", "General"),
            "is_subject_level": data.get("is_subject_level", False),
        }
    return {
        "subject": "OOPS",
        "topic": "General",
        "is_subject_level": False,
    }
