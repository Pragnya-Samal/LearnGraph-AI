import { createContext, useContext, useState, useEffect } from 'react';

const LearningContext = createContext(null);

// --- Prerequisite map for recommendation logic ---
const PREREQUISITES = {
  'Linked Lists': ['Arrays'],
  'Trees': ['Arrays', 'Linked Lists'],
  'Graphs': ['Arrays', 'Linked Lists'],
  'Searching': ['Arrays', 'Sorting'],
  'Dynamic Programming': ['Sorting', 'Searching'],
  'Backtracking': ['Dynamic Programming'],
  'Normalization': ['SQL Basics'],
  'Transactions': ['SQL Basics', 'Normalization'],
  'Indexing': ['SQL Basics', 'Normalization'],
  'Classification': ['Linear Regression'],
  'Clustering': ['Linear Regression'],
  'Neural Networks': ['Classification'],
  'Evaluation Metrics': ['Classification', 'Clustering'],
  'Polymorphism': ['Inheritance'],
  'Abstraction': ['Encapsulation'],
};

// --- Adaptive knowledge state from multiple assessment signals ---
function computeKnowledgeState(history) {
  if (!history || history.length === 0) return { status: 'Not Assessed', confidence: 0, score: 0 };

  const count = history.length;
  const avg = history.reduce((s, r) => s + r.percentage, 0) / count;
  const latest = history[0].percentage;
  const trend = count >= 2 ? latest - history[1].percentage : 0;

  // Weighted score: 50% latest, 30% avg, 20% trend bonus
  const weighted = latest * 0.5 + avg * 0.3 + Math.max(0, trend) * 0.2;

  let status;
  if (count === 1 && latest >= 70) status = 'Uncertain'; // only 1 attempt, even if high
  else if (weighted >= 70 && count >= 2) status = 'Strong';
  else if (weighted >= 40) status = 'Weak';
  else status = 'Weak';

  if (count === 1) status = latest >= 70 ? 'Uncertain' : 'Weak';

  return { status, confidence: Math.round(weighted), score: Math.round(avg), count };
}

// --- Generate personalized recommendations with explanations ---
function generateRecommendations(conceptMap) {
  const recs = [];

  for (const [topic, state] of Object.entries(conceptMap)) {
    const prereqs = PREREQUISITES[topic] || [];
    const prereqsMet = prereqs.every((p) => {
      const ps = conceptMap[p];
      return ps && (ps.status === 'Strong' || ps.status === 'Uncertain');
    });

    if (state.status === 'Not Assessed' && prereqsMet) {
      const prereqNames = prereqs.join(' and ');
      recs.push({
        topic,
        subject: state.subject,
        reason: prereqs.length > 0
          ? `${topic} is recommended because your performance in ${prereqNames} is strong, and ${prereqNames} is a prerequisite for ${topic}.`
          : `${topic} has not been assessed yet. Start here to build your knowledge profile.`,
        priority: 1,
      });
    } else if (state.status === 'Weak') {
      recs.push({
        topic,
        subject: state.subject,
        reason: `${topic} is recommended for revision because your assessments show difficulty with this concept (avg score: ${state.score}%).`,
        priority: 0,
      });
    }
  }

  return recs.sort((a, b) => b.priority - a.priority).slice(0, 5);
}

function getUserKey(userId, key) {
  return `lg_${userId}_${key}`;
}

export function LearningProvider({ children, userId }) {
  const [assessmentHistory, setAssessmentHistory] = useState(() => {
    if (!userId) return {};
    try {
      return JSON.parse(localStorage.getItem(getUserKey(userId, 'history')) || '{}');
    } catch { return {}; }
  });

  const [lastTopic, setLastTopic] = useState(() => {
    if (!userId) return null;
    try {
      return JSON.parse(localStorage.getItem(getUserKey(userId, 'lastTopic')) || 'null');
    } catch { return null; }
  });

  // Reload when userId changes (login/logout/switch user)
  useEffect(() => {
    if (!userId) {
      setAssessmentHistory({});
      setLastTopic(null);
      return;
    }
    try {
      setAssessmentHistory(JSON.parse(localStorage.getItem(getUserKey(userId, 'history')) || '{}'));
      setLastTopic(JSON.parse(localStorage.getItem(getUserKey(userId, 'lastTopic')) || 'null'));
    } catch {
      setAssessmentHistory({});
      setLastTopic(null);
    }
  }, [userId]);

  const saveAssessmentResult = (resultData) => {
    if (!userId) return;
    const { subject, topic, score, total_questions, knowledge_level } = resultData;
    const percentage = total_questions > 0 ? Math.round((score / total_questions) * 100) : 0;
    const entry = { subject, topic, score, total: total_questions, knowledge_level, percentage, date: new Date().toISOString() };

    setAssessmentHistory((prev) => {
      const topicHistory = [entry, ...(prev[topic] || [])].slice(0, 10);
      const updated = { ...prev, [topic]: topicHistory };
      localStorage.setItem(getUserKey(userId, 'history'), JSON.stringify(updated));
      return updated;
    });

    const newLastTopic = { subject, topic, percentage, knowledge_level };
    setLastTopic(newLastTopic);
    localStorage.setItem(getUserKey(userId, 'lastTopic'), JSON.stringify(newLastTopic));
  };

  // Build flat assessmentResults list (latest per topic) for backward compat
  const assessmentResults = Object.entries(assessmentHistory).map(([topic, history]) => ({
    ...history[0],
    topic,
  }));

  // Build concept mastery map
  const SUBJECT_MAP = {
    'Arrays': 'Data Structures', 'Linked Lists': 'Data Structures', 'Stacks & Queues': 'Data Structures',
    'Trees': 'Data Structures', 'Graphs': 'Data Structures', 'Hashing': 'Data Structures',
    'Sorting': 'Algorithms', 'Searching': 'Algorithms', 'Dynamic Programming': 'Algorithms',
    'Greedy': 'Algorithms', 'Backtracking': 'Algorithms',
    'ER Modeling': 'Database Systems', 'SQL Basics': 'Database Systems', 'Normalization': 'Database Systems',
    'Transactions': 'Database Systems', 'Indexing': 'Database Systems',
    'Linear Regression': 'Machine Learning', 'Classification': 'Machine Learning',
    'Clustering': 'Machine Learning', 'Neural Networks': 'Machine Learning', 'Evaluation Metrics': 'Machine Learning',
    'Inheritance': 'OOPS', 'Encapsulation': 'OOPS', 'Polymorphism': 'OOPS', 'Abstraction': 'OOPS',
  };

  const conceptMap = {};
  for (const [topic, subject] of Object.entries(SUBJECT_MAP)) {
    const history = assessmentHistory[topic] || [];
    const state = computeKnowledgeState(history);
    conceptMap[topic] = { ...state, subject };
  }

  const recommendations = userId ? generateRecommendations(conceptMap) : [];

  const totalAssessments = assessmentResults.length;
  const avgScore = totalAssessments > 0
    ? Math.round(assessmentResults.reduce((s, r) => s + r.percentage, 0) / totalAssessments)
    : 0;

  // Subject-level progress from real data
  const subjectProgress = {};
  for (const [topic, state] of Object.entries(conceptMap)) {
    const subj = state.subject;
    if (!subjectProgress[subj]) subjectProgress[subj] = { total: 0, sum: 0, count: 0 };
    subjectProgress[subj].total++;
    if (state.status !== 'Not Assessed') {
      subjectProgress[subj].sum += state.score;
      subjectProgress[subj].count++;
    }
  }
  const subjectProgressList = Object.entries(subjectProgress).map(([subject, data]) => ({
    subject,
    progress: data.count > 0 ? Math.round(data.sum / data.count) : 0,
  }));

  // Donut chart data: per-subject concept status counts
  // Maps existing statuses → 4 donut categories
  function getDonutData(subject) {
    const entries = Object.entries(conceptMap).filter(
      ([_, s]) => !subject || s.subject === subject
    );
    const counts = { Mastered: 0, 'In Progress': 0, 'Needs Revision': 0, 'Not Assessed': 0 };
    for (const [_, s] of entries) {
      if (s.status === 'Strong')           counts['Mastered']++;
      else if (s.status === 'Uncertain')   counts['In Progress']++;
      else if (s.status === 'Weak')        counts['Needs Revision']++;
      else                                 counts['Not Assessed']++;
    }
    const total = entries.length || 1;
    return [
      { label: 'Mastered',      count: counts['Mastered'],      pct: Math.round((counts['Mastered'] / total) * 100),      color: '#10b981' },
      { label: 'In Progress',   count: counts['In Progress'],   pct: Math.round((counts['In Progress'] / total) * 100),   color: '#4f46e5' },
      { label: 'Needs Revision',count: counts['Needs Revision'],pct: Math.round((counts['Needs Revision'] / total) * 100),color: '#f59e0b' },
      { label: 'Not Assessed',  count: counts['Not Assessed'],  pct: Math.round((counts['Not Assessed'] / total) * 100),  color: '#94a3b8' },
    ];
  }

  return (
    <LearningContext.Provider
      value={{
        assessmentResults,
        assessmentHistory,
        lastTopic,
        saveAssessmentResult,
        totalAssessments,
        avgScore,
        conceptMap,
        recommendations,
        subjectProgressList,
        getDonutData,
      }}
    >
      {children}
    </LearningContext.Provider>
  );
}

export function useLearning() {
  const context = useContext(LearningContext);
  if (!context) throw new Error('useLearning must be used within a LearningProvider');
  return context;
}
