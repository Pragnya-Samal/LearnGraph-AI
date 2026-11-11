"""
Spaced Repetition Engine for Personalized Learning System
Implements the 4-stage interval ladder:
  Stage 1: Tomorrow (1 day later)
  Stage 2: 3 days later
  Stage 3: 7 days later
  Stage 4: 30 days later

Failure rule: If the learner fails the review quiz (score < pass_threshold),
the interval drops back to the previous stage in the ladder and restarts from there.
"""

from typing import Dict, Any, List

INTERVAL_LADDER: List[int] = [1, 3, 7, 30]
DEFAULT_PASS_THRESHOLD: float = 70.0


def calculate_next_review(
    score: float,
    current_interval: int = 0,
    pass_threshold: float = DEFAULT_PASS_THRESHOLD
) -> Dict[str, Any]:
    """
    Calculate the next spaced repetition interval based on performance.

    Parameters:
      - score: percentage score achieved (0 - 100)
      - current_interval: current interval stage in days (0 if initial learning, or 1, 3, 7, 30)
      - pass_threshold: minimum percentage to advance to next interval (default: 70.0)

    Returns dictionary with next_review_in_days, stage, passed, and explanation message.
    """
    passed = score >= pass_threshold
    total_stages = len(INTERVAL_LADDER)

    # Determine position in the ladder
    if current_interval <= 0:
        idx = -1
    elif current_interval in INTERVAL_LADDER:
        idx = INTERVAL_LADDER.index(current_interval)
    else:
        # Fallback closest ladder index
        if current_interval < 1:
            idx = -1
        elif current_interval < 3:
            idx = 0
        elif current_interval < 7:
            idx = 1
        elif current_interval < 30:
            idx = 2
        else:
            idx = 3

    is_mastered = False

    # 1. Initial Topic Learning (idx == -1)
    if idx == -1:
        next_interval = INTERVAL_LADDER[0]  # 1 day (tomorrow)
        stage = 1
        message = "Topic completed! Initial spaced-repetition quiz scheduled for tomorrow (1 day later)."

    # 2. Passed the Review Quiz (score >= pass_threshold)
    elif passed:
        if idx + 1 < total_stages:
            next_idx = idx + 1
            next_interval = INTERVAL_LADDER[next_idx]
            stage = next_idx + 1
            message = (
                f"Passed with {score:.1f}%! Retention verified. "
                f"Advanced to next interval: {next_interval} days later."
            )
        else:
            # Passed Stage 4 (30 days) -> Mastered
            next_interval = INTERVAL_LADDER[-1]
            stage = total_stages
            is_mastered = True
            message = (
                f"Passed with {score:.1f}%! Outstanding long-term memory retention. "
                f"Concept fully mastered at the 30-day interval."
            )

    # 3. Failed the Review Quiz (score < pass_threshold) -> Drop back to previous interval
    else:
        if idx > 0:
            prev_idx = idx - 1
            next_interval = INTERVAL_LADDER[prev_idx]
            stage = prev_idx + 1
            message = (
                f"Score {score:.1f}% is below {pass_threshold:.0f}%. Dropped back to previous interval: "
                f"{next_interval} day(s) later to reinforce understanding."
            )
        else:
            # Already at Stage 1 (1 day), stay at 1 day (tomorrow)
            next_interval = INTERVAL_LADDER[0]
            stage = 1
            message = (
                f"Score {score:.1f}% is below {pass_threshold:.0f}%. Reinforcement needed: "
                f"Review quiz rescheduled for tomorrow (1 day later)."
            )

    return {
        "score": score,
        "current_interval": current_interval,
        "next_review_in_days": next_interval,
        "passed": passed,
        "stage": stage,
        "total_stages": total_stages,
        "interval_ladder": INTERVAL_LADDER,
        "message": message,
        "is_mastered": is_mastered
    }
