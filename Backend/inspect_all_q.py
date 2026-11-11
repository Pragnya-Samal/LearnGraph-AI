import sys
sys.path.insert(0, "Backend")
from AI.Assessment.questions import questions

for s, topics in questions.items():
    print(f"=== {s} ===")
    for t, qs in topics.items():
        print(f"[{t}] {len(qs)} questions")

