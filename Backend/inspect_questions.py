import sys
sys.path.insert(0, "Backend")
from AI.Assessment.questions import questions

for s, topics in questions.items():
    print(f"=== {s} ===")
    for t, qs in list(topics.items())[:2]:
        print(f"  Topic: {t} ({len(qs)} questions)")
        for i, q in enumerate(qs[:3]):
            print(f"    Q{i+1}: {q['question']}")

