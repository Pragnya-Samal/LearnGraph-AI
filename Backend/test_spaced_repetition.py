import sys
from pathlib import Path

backend_dir = str(Path(__file__).resolve().parent)
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from AI.SpacedRepetition.spaced_repetition_logic import calculate_next_review

print("--- 1. Initial Topic Completion ---")
r0 = calculate_next_review(score=85, current_interval=0)
print("Initial:", r0)
assert r0["next_review_in_days"] == 1, "Initial must be 1 day (tomorrow)"

print("\n--- 2. Passing Progression (1 -> 3 -> 7 -> 30) ---")
r1 = calculate_next_review(score=75, current_interval=1)
print("After Day 1 pass:", r1)
assert r1["next_review_in_days"] == 3, "After 1 day pass -> 3 days"

r2 = calculate_next_review(score=80, current_interval=3)
print("After Day 3 pass:", r2)
assert r2["next_review_in_days"] == 7, "After 3 days pass -> 7 days"

r3 = calculate_next_review(score=90, current_interval=7)
print("After Day 7 pass:", r3)
assert r3["next_review_in_days"] == 30, "After 7 days pass -> 30 days"

r4 = calculate_next_review(score=95, current_interval=30)
print("After Day 30 pass:", r4)
assert r4["next_review_in_days"] == 30 and r4["is_mastered"] is True, "After 30 days pass -> Mastered"

print("\n--- 3. Failing Regression (Go back to previous interval) ---")
# Failed at 30 days -> drop back to 7 days
f30 = calculate_next_review(score=45, current_interval=30)
print("Failed at Day 30:", f30)
assert f30["next_review_in_days"] == 7, "Failed at 30 days must drop back to 7 days"

# Failed at 7 days -> drop back to 3 days
f7 = calculate_next_review(score=50, current_interval=7)
print("Failed at Day 7:", f7)
assert f7["next_review_in_days"] == 3, "Failed at 7 days must drop back to 3 days"

# Failed at 3 days -> drop back to 1 day (tomorrow)
f3 = calculate_next_review(score=35, current_interval=3)
print("Failed at Day 3:", f3)
assert f3["next_review_in_days"] == 1, "Failed at 3 days must drop back to 1 day (tomorrow)"

# Failed at 1 day -> stays at 1 day (tomorrow)
f1 = calculate_next_review(score=20, current_interval=1)
print("Failed at Day 1:", f1)
assert f1["next_review_in_days"] == 1, "Failed at 1 day must stay at 1 day (tomorrow)"

print("\nAll spaced repetition ladder tests passed successfully!")
