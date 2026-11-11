def analyze_performance(subject: str, topics: dict[str, float]):

    if not topics:
        return {
            "subject": subject,
            "overall_performance": 0,
            "strong_concepts": [],
            "weak_concepts": [],
            "topics_requiring_attention": []
        }

    overall_performance = round(
        sum(topics.values()) / len(topics), 1
    )

    strong_concepts = []
    weak_concepts = []
    topics_requiring_attention = []

    for topic, score in topics.items():

        if score >= 70:
            strong_concepts.append(topic)

        if score < 40:
            weak_concepts.append(topic)

        if score < 70:
            topics_requiring_attention.append(topic)

    return {
        "subject": subject,
        "overall_performance": overall_performance,
        "strong_concepts": strong_concepts,
        "weak_concepts": weak_concepts,
        "topics_requiring_attention": topics_requiring_attention
    }