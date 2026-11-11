import sys
sys.path.insert(0, "Backend")
from AI.Assessment.questions import questions

for subj, topics in questions.items():
    print(f"Subject: {subj}")
    for t_name, q_list in topics.items():
        print(f"  Topic: {t_name} -> {len(q_list)} questions")

