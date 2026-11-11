import os
import random
import copy
from typing import Dict, Any, List, Optional
from .questions import questions

# Alias / Substring normalizer
def find_subject_key(subject: str) -> Optional[str]:
    sub_lower = subject.strip().lower()
    for s in questions.keys():
        if s.lower() == sub_lower or sub_lower in s.lower() or s.lower() in sub_lower:
            return s
    return "OOPS"


def find_topic_questions(subject_key: str, topic_name: str) -> List[Dict[str, Any]]:
    subj_data = questions.get(subject_key, {})
    if topic_name in subj_data:
        return subj_data[topic_name]

    top_lower = topic_name.strip().lower()
    for t_name, q_list in subj_data.items():
        if t_name.lower() == top_lower or top_lower in t_name.lower() or t_name.lower() in top_lower:
            return q_list

    # Fallback to any topic list in subject
    for q_list in subj_data.values():
        if q_list:
            return q_list

    return []


def randomize_question(raw_q: Dict[str, Any], topic_name: str) -> Dict[str, Any]:
    """Create a randomized copy of a question with shuffled options and topic tag."""
    options = list(raw_q["options"])
    random.shuffle(options)

    return {
        "question": raw_q["question"],
        "options": options,
        "correct_answer": raw_q["correct_answer"],
        "explanation": raw_q.get("explanation", ""),
        "topic": topic_name,
        "difficulty": raw_q.get("difficulty", "Easy")
    }


DIFFICULTY_RANK = {"Easy": 0, "Medium": 1, "Hard": 2}


def generate_subject_assessment(
    subject: str,
    number_of_questions: int = 30
) -> Dict[str, Any]:
    """
    Generate a Subject-level assessment testing across all hierarchical topics in the subject.
    Questions are selected across topics and strictly ordered from Easy to Hard (questions 1 to 30).
    Option choices are shuffled uniquely on every request.
    """
    subject_key = find_subject_key(subject)

    # Attempt to retrieve ordered hierarchical topics from the database
    topic_names = []
    try:
        from database import get_subject_hierarchy
        hierarchy = get_subject_hierarchy(subject_key)
        topic_names = [t["name"] for t in hierarchy]
    except Exception:
        pass

    if not topic_names:
        # Fallback to keys in questions bank, excluding aliases
        raw_keys = list(questions.get(subject_key, {}).keys())
        alias_names = {"Inheritance", "Encapsulation", "Polymorphism", "Abstraction", "Arrays", "Linked Lists", "SQL Basics"}
        topic_names = [k for k in raw_keys if k not in alias_names]
        if not topic_names:
            topic_names = raw_keys

    # Divide requested count into Easy, Medium, Hard tiers
    n_easy = number_of_questions // 3
    n_med = number_of_questions // 3
    n_hard = number_of_questions - n_easy - n_med

    easy_pool = []
    med_pool = []
    hard_pool = []

    for t_name in topic_names:
        t_qs = find_topic_questions(subject_key, t_name)
        for q in t_qs:
            diff = q.get("difficulty", "Easy")
            if diff == "Easy":
                easy_pool.append((t_name, q))
            elif diff == "Medium":
                med_pool.append((t_name, q))
            else:
                hard_pool.append((t_name, q))

    def sample_tier(tier_pool, count):
        if not tier_pool:
            return []
        # Ensure breadth across different topics first
        by_topic = {}
        for t_name, q in tier_pool:
            by_topic.setdefault(t_name, []).append(q)
        picked = []
        topic_keys = list(by_topic.keys())
        random.shuffle(topic_keys)
        for t_name in topic_keys:
            if len(picked) >= count:
                break
            picked.append(randomize_question(random.choice(by_topic[t_name]), t_name))
        # If more are needed, sample from the remaining pool
        while len(picked) < count and tier_pool:
            t_name, q = random.choice(tier_pool)
            picked.append(randomize_question(q, t_name))
        random.shuffle(picked)
        return picked[:count]

    chosen_easy = sample_tier(easy_pool, n_easy)
    chosen_med = sample_tier(med_pool, n_med)
    chosen_hard = sample_tier(hard_pool, n_hard)

    # Strict ordering: Easy (0..9), Medium (10..19), Hard (20..29)
    selected_questions = chosen_easy + chosen_med + chosen_hard

    # Sort strictly by difficulty rank to guarantee questions 1 to 30 are easy to hard
    selected_questions.sort(key=lambda q: DIFFICULTY_RANK.get(q.get("difficulty", "Easy"), 0))

    return {
        "subject": subject_key,
        "is_subject_level": True,
        "questions": selected_questions
    }


def generate_topic_quiz(
    subject: str,
    topic: str,
    number_of_questions: int = 30
) -> Dict[str, Any]:
    """
    Generate a Spaced Repetition Quiz for a specific learned topic.
    Questions are strictly ordered from Easy to Hard (questions 1 to 30).
    Option choices are shuffled uniquely on every request.
    """
    subject_key = find_subject_key(subject)
    pool = find_topic_questions(subject_key, topic)

    if not pool:
        pool = find_topic_questions("OOPS", "Classes and Objects")

    easy_pool = [q for q in pool if q.get("difficulty") == "Easy"]
    med_pool = [q for q in pool if q.get("difficulty") == "Medium"]
    hard_pool = [q for q in pool if q.get("difficulty") == "Hard"]

    # Fallback if pools are empty
    if not easy_pool:
        easy_pool = pool[:len(pool)//3] or pool
    if not med_pool:
        med_pool = pool[len(pool)//3:2*len(pool)//3] or pool
    if not hard_pool:
        hard_pool = pool[2*len(pool)//3:] or pool

    n_easy = number_of_questions // 3
    n_med = number_of_questions // 3
    n_hard = number_of_questions - n_easy - n_med

    def sample_from_pool(sub_pool, count):
        if not sub_pool:
            return []
        sample_size = min(count, len(sub_pool))
        picked = random.sample(sub_pool, sample_size)
        while len(picked) < count:
            picked.append(random.choice(sub_pool))
        random.shuffle(picked)
        return [randomize_question(q, topic) for q in picked]

    chosen_easy = sample_from_pool(easy_pool, n_easy)
    chosen_med = sample_from_pool(med_pool, n_med)
    chosen_hard = sample_from_pool(hard_pool, n_hard)

    # Combine in strict Easy -> Medium -> Hard sequence
    selected_questions = chosen_easy + chosen_med + chosen_hard
    selected_questions.sort(key=lambda q: DIFFICULTY_RANK.get(q.get("difficulty", "Easy"), 0))

    return {
        "subject": subject_key,
        "topic": topic,
        "is_subject_level": False,
        "questions": selected_questions
    }


def generate_assessment(
    subject: str,
    topic: str,
    number_of_questions: int = 30
) -> Dict[str, Any]:
    """Compatibility wrapper for topic-level assessment."""
    return generate_topic_quiz(subject, topic, number_of_questions)
