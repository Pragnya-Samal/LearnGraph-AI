import { useState, useEffect } from 'react';
import { useLocation, useNavigate, Link } from 'react-router-dom';

import Card, { CardHeader, CardTitle, CardBody } from '../components/Card';
import Button from '../components/Button';
import ProgressCircle from '../components/ProgressCircle';
import { SUBJECTS } from '../data/mockData';
import {
  generateSubjectAssessment,
  generateTopicQuiz,
  submitGeneratedAssessment,
  fetchStudyMaterials,
} from '../services/api';
import { useLearning } from '../contexts/LearningContext';
import {
  CheckCircleIcon,
  XCircleIcon,
  AlertCircleIcon,
  ArrowRightIcon,
  ArrowLeftIcon,
  TargetIcon,
  SparklesIcon,
  BookOpenIcon,
  YouTubeIcon,
  GlobeIcon,
  ExternalLinkIcon,
  RefreshCwIcon,
  ClockIcon,
} from '../components/Icons';

export default function Assessment() {
  const { state } = useLocation();
  const navigate = useNavigate();
  const { saveAssessmentResult } = useLearning();

  // Selected Subject and Topic
  const [selectedSubject, setSelectedSubject] = useState(state?.subject || '');
  const [selectedTopic, setSelectedTopic] = useState(state?.topic || '');
  const [assessmentMode, setAssessmentMode] = useState(state?.mode || 'subject'); // 'subject' or 'quiz'

  // Quiz Execution State
  const [questions, setQuestions] = useState([]);
  const [assessmentId, setAssessmentId] = useState(null);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [answers, setAnswers] = useState([]);
  const [loading, setLoading] = useState(false);
  const [started, setStarted] = useState(false);
  const [submitted, setSubmitted] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');

  // Auto-start if subject was passed through navigation
  useEffect(() => {
    if (state?.subject && !started && !submitted) {
      setSelectedSubject(state.subject);
      if (state.mode === 'quiz' && state.topic) {
        setSelectedTopic(state.topic);
        setAssessmentMode('quiz');
        startQuizSession(state.subject, state.topic);
      } else {
        setAssessmentMode('subject');
        startSubjectSession(state.subject);
      }
    }
  }, [state]);

  // Start Subject-Level Assessment
  const startSubjectSession = async (subjectToUse) => {
    const subj = subjectToUse || selectedSubject;
    if (!subj) return;

    try {
      setLoading(true);
      setError('');
      setSubmitted(false);
      setResult(null);

      const res = await generateSubjectAssessment(subj, 30);
      if (!res.success) {
        throw new Error(res.error || 'Failed to generate subject assessment.');
      }

      setAssessmentId(res.data.assessment_id);
      setQuestions(res.data.questions || []);
      setAnswers(new Array(res.data.questions?.length || 0).fill(null));
      setCurrentQuestionIndex(0);
      setAssessmentMode('subject');
      setStarted(true);
    } catch (err) {
      console.error(err);
      setError(err.message || 'Unable to generate assessment.');
    } finally {
      setLoading(false);
    }
  };

  // Start Topic-Level Spaced Repetition Quiz
  const startQuizSession = async (subjectToUse, topicToUse) => {
    const subj = subjectToUse || selectedSubject;
    const top = topicToUse || selectedTopic;
    if (!subj || !top) return;

    try {
      setLoading(true);
      setError('');
      setSubmitted(false);
      setResult(null);

      const res = await generateTopicQuiz(subj, top, 30);
      if (!res.success) {
        throw new Error(res.error || `Failed to generate quiz for ${top}.`);
      }

      setAssessmentId(res.data.assessment_id);
      setSelectedSubject(subj);
      setSelectedTopic(top);
      setQuestions(res.data.questions || []);
      setAnswers(new Array(res.data.questions?.length || 0).fill(null));
      setCurrentQuestionIndex(0);
      setAssessmentMode('quiz');
      setStarted(true);
    } catch (err) {
      console.error(err);
      setError(err.message || 'Unable to generate topic quiz.');
    } finally {
      setLoading(false);
    }
  };

  // Answer selection
  const handleSelectOption = (optionText) => {
    const nextAnswers = [...answers];
    nextAnswers[currentQuestionIndex] = optionText;
    setAnswers(nextAnswers);
    if (error) setError('');
  };

  // Submit Assessment
  const handleSubmit = async () => {
    const unansweredCount = answers.filter((a) => a === null).length;
    if (unansweredCount > 0) {
      setError(`Please answer all questions before submitting. (${unansweredCount} remaining)`);
      return;
    }

    try {
      setLoading(true);
      setError('');

      const res = await submitGeneratedAssessment(assessmentId, answers);
      if (!res.success) {
        throw new Error(res.error || 'Failed to submit assessment.');
      }

      const resData = res.data;
      setResult(resData);
      setSubmitted(true);
      setStarted(false);

      // Persist in Learning Context
      saveAssessmentResult({
        subject: resData.subject,
        topic: resData.topic || (resData.is_subject_level ? 'Subject Assessment' : selectedTopic),
        score: resData.score,
        total_questions: resData.total_questions,
        knowledge_level: resData.knowledge_level,
      });
    } catch (err) {
      console.error(err);
      setError(err.message || 'Unable to submit assessment.');
    } finally {
      setLoading(false);
    }
  };

  // ==========================================================================
  // VIEW 1: SUBJECT SELECTION (When no subject is loaded)
  // ==========================================================================
  if (!started && !submitted) {
    return (
      <div className="assessment-page">
        <div className="container" style={{ maxWidth: '900px', margin: '0 auto', padding: 'var(--space-8) 0' }}>
          <div className="page-header" style={{ textAlign: 'center', marginBottom: 'var(--space-8)' }}>
            <span className="badge badge-primary" style={{ marginBottom: 'var(--space-2)' }}>
              Subject-Level Assessment
            </span>
            <h1 style={{ fontSize: '2.25rem', fontWeight: '800' }}>Comprehensive Knowledge Assessment</h1>
            <p style={{ color: 'var(--text-secondary)', maxWidth: '650px', margin: '0 auto' }}>
              Assess your subject knowledge across 10 hierarchical topics (from Easy to Hard).
              Questions are randomized and unique every time. Based on your answers, weak topics will be identified
              and recommended with curated study materials for spaced repetition.
            </p>
          </div>

          <Card>
            <CardHeader>
              <CardTitle>Select a Subject for Assessment</CardTitle>
            </CardHeader>
            <CardBody>
              {error && (
                <div className="alert alert-danger" style={{ marginBottom: 'var(--space-4)', padding: 'var(--space-3)', backgroundColor: 'var(--status-danger-subtle)', borderRadius: 'var(--radius-md)', color: 'var(--status-danger)' }}>
                  <AlertCircleIcon size={16} />
                  <span>{error}</span>
                </div>
              )}

              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: 'var(--space-4)', marginBottom: 'var(--space-6)' }}>
                {SUBJECTS.map((subj) => {
                  const isSelected = selectedSubject === subj.name || selectedSubject === subj.id;
                  return (
                    <div
                      key={subj.id}
                      onClick={() => setSelectedSubject(subj.name)}
                      style={{
                        padding: 'var(--space-5)',
                        border: isSelected ? '2px solid var(--primary)' : '1px solid var(--border-medium)',
                        backgroundColor: isSelected ? 'var(--primary-subtle, rgba(99, 102, 241, 0.08))' : 'var(--bg-surface)',
                        borderRadius: 'var(--radius-lg)',
                        cursor: 'pointer',
                        transition: 'all 0.2s ease',
                      }}
                    >
                      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 'var(--space-2)' }}>
                        <span style={{ fontWeight: '700', fontSize: '1.125rem' }}>{subj.name}</span>
                        <span className="badge badge-secondary" style={{ fontSize: '0.75rem' }}>10 Topics</span>
                      </div>
                      <p style={{ fontSize: '0.875rem', color: 'var(--text-secondary)', marginBottom: 'var(--space-3)' }}>
                        {subj.description}
                      </p>
                      <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                        Hierarchical progression • Easy to Hard
                      </div>
                    </div>
                  );
                })}
              </div>

              <div style={{ display: 'flex', justifyContent: 'center' }}>
                <Button
                  variant="primary"
                  size="lg"
                  disabled={!selectedSubject || loading}
                  onClick={() => startSubjectSession(selectedSubject)}
                  style={{ minWidth: '240px' }}
                >
                  {loading ? (
                    <span>Generating Unique Assessment...</span>
                  ) : (
                    <>
                      <span>Start {selectedSubject || 'Subject'} Assessment</span>
                      <ArrowRightIcon size={18} />
                    </>
                  )}
                </Button>
              </div>
            </CardBody>
          </Card>
        </div>
      </div>
    );
  }

  // ==========================================================================
  // VIEW 2: TAKING ASSESSMENT (Question by Question with randomized questions)
  // ==========================================================================
  if (started && questions.length > 0) {
    const currentQuestion = questions[currentQuestionIndex];
    const totalQ = questions.length;
    const progressPercent = Math.round(((currentQuestionIndex + 1) / totalQ) * 100);
    const selectedAnswerForCurrent = answers[currentQuestionIndex];

    return (
      <div className="assessment-page">
        <div className="container" style={{ maxWidth: '850px', margin: '0 auto', padding: 'var(--space-6) 0' }}>
          {/* Header Bar */}
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 'var(--space-4)' }}>
            <div>
              <span className="badge badge-primary" style={{ marginRight: 'var(--space-2)' }}>
                {assessmentMode === 'quiz' ? 'Spaced Repetition Quiz' : 'Subject Assessment'}
              </span>
              <span style={{ fontWeight: '600', color: 'var(--text-secondary)' }}>
                {selectedSubject} {assessmentMode === 'quiz' && `• ${selectedTopic}`}
              </span>
            </div>
            <div style={{ fontSize: '0.875rem', color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: '0.35rem' }}>
              <ClockIcon size={16} />
              <span>Question {currentQuestionIndex + 1} of {totalQ}</span>
            </div>
          </div>

          {/* Progress Bar */}
          <div style={{ height: '6px', width: '100%', backgroundColor: 'var(--border-subtle)', borderRadius: '999px', overflow: 'hidden', marginBottom: 'var(--space-6)' }}>
            <div style={{ height: '100%', width: `${progressPercent}%`, backgroundColor: 'var(--primary)', transition: 'width 0.3s ease' }}></div>
          </div>

          {error && (
            <div className="alert alert-danger" style={{ marginBottom: 'var(--space-4)', padding: 'var(--space-3)', backgroundColor: 'var(--status-danger-subtle)', borderRadius: 'var(--radius-md)', color: 'var(--status-danger)' }}>
              <AlertCircleIcon size={16} />
              <span>{error}</span>
            </div>
          )}

          {/* Question Card */}
          <Card>
            <CardHeader style={{ borderBottom: '1px solid var(--border-subtle)', paddingBottom: 'var(--space-4)' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <span className="badge badge-secondary" style={{ fontSize: '0.8rem', padding: '0.2rem 0.6rem' }}>
                  Topic: {currentQuestion.topic || selectedTopic || selectedSubject}
                </span>
                <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>
                  {answers.filter((a) => a !== null).length} of {totalQ} Answered
                </span>
              </div>
              <h2 style={{ fontSize: '1.25rem', fontWeight: '700', marginTop: 'var(--space-3)', lineHeight: '1.5' }}>
                {currentQuestion.question}
              </h2>
            </CardHeader>
            <CardBody>
              <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-3)' }}>
                {currentQuestion.options.map((opt, optIdx) => {
                  const letter = String.fromCharCode(65 + optIdx);
                  const isChosen = selectedAnswerForCurrent === opt;
                  return (
                    <div
                      key={optIdx}
                      onClick={() => handleSelectOption(opt)}
                      style={{
                        display: 'flex',
                        alignItems: 'center',
                        gap: 'var(--space-3)',
                        padding: 'var(--space-4)',
                        border: isChosen ? '2px solid var(--primary)' : '1px solid var(--border-medium)',
                        backgroundColor: isChosen ? 'var(--primary-subtle, rgba(99, 102, 241, 0.08))' : 'var(--bg-surface)',
                        borderRadius: 'var(--radius-md)',
                        cursor: 'pointer',
                        transition: 'all 0.15s ease',
                      }}
                    >
                      <div
                        style={{
                          width: '28px',
                          height: '28px',
                          borderRadius: '50%',
                          border: isChosen ? '2px solid var(--primary)' : '1px solid var(--border-medium)',
                          backgroundColor: isChosen ? 'var(--primary)' : 'transparent',
                          color: isChosen ? '#fff' : 'var(--text-secondary)',
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'center',
                          fontWeight: '700',
                          fontSize: '0.85rem',
                          flexShrink: 0,
                        }}
                      >
                        {letter}
                      </div>
                      <span style={{ fontSize: '1rem', color: isChosen ? 'var(--text-primary)' : 'var(--text-secondary)', fontWeight: isChosen ? '600' : '400' }}>
                        {opt}
                      </span>
                    </div>
                  );
                })}
              </div>

              {/* Question Navigation Matrix */}
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.5rem', marginTop: 'var(--space-6)', paddingTop: 'var(--space-4)', borderTop: '1px solid var(--border-subtle)' }}>
                {questions.map((_, qIdx) => {
                  const isCurrent = qIdx === currentQuestionIndex;
                  const isAnswered = answers[qIdx] !== null;
                  return (
                    <button
                      key={qIdx}
                      onClick={() => setCurrentQuestionIndex(qIdx)}
                      style={{
                        width: '32px',
                        height: '32px',
                        borderRadius: 'var(--radius-sm)',
                        border: isCurrent ? '2px solid var(--primary)' : '1px solid var(--border-medium)',
                        backgroundColor: isCurrent ? 'var(--primary)' : isAnswered ? 'var(--bg-surface-subtle)' : 'transparent',
                        color: isCurrent ? '#fff' : isAnswered ? 'var(--primary)' : 'var(--text-muted)',
                        fontWeight: '600',
                        fontSize: '0.8rem',
                        cursor: 'pointer',
                      }}
                    >
                      {qIdx + 1}
                    </button>
                  );
                })}
              </div>

              {/* Action Buttons */}
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: 'var(--space-6)' }}>
                <Button
                  variant="outline"
                  disabled={currentQuestionIndex === 0}
                  onClick={() => setCurrentQuestionIndex((prev) => Math.max(0, prev - 1))}
                >
                  <ArrowLeftIcon size={16} />
                  <span>Previous</span>
                </Button>

                {currentQuestionIndex < totalQ - 1 ? (
                  <Button
                    variant="primary"
                    onClick={() => setCurrentQuestionIndex((prev) => Math.min(totalQ - 1, prev + 1))}
                  >
                    <span>Next</span>
                    <ArrowRightIcon size={16} />
                  </Button>
                ) : (
                  <Button
                    variant="success"
                    disabled={loading}
                    onClick={handleSubmit}
                    style={{ minWidth: '150px' }}
                  >
                    {loading ? <span>Submitting...</span> : <span>Submit Assessment</span>}
                  </Button>
                )}
              </div>
            </CardBody>
          </Card>
        </div>
      </div>
    );
  }

  // ==========================================================================
  // VIEW 3: RESULTS, TOPIC ANALYSIS, STUDY MATERIALS, AND SPACED REPETITION
  // ==========================================================================
  if (submitted && result) {
    const isSubjectLevel = result.is_subject_level;
    const recommendedTopic = result.recommended_topic;
    const topicBreakdown = result.topic_breakdown || {};
    const topicEntries = Object.values(topicBreakdown);
    const weakCount = result.weak_topics?.length || 0;
    const passedCount = result.passed_topics?.length || 0;

    return (
      <div className="assessment-page">
        <div className="container" style={{ maxWidth: '900px', margin: '0 auto', padding: 'var(--space-6) 0' }}>
          {/* Header Celebration/Summary */}
          <div className="page-header" style={{ textAlign: 'center', marginBottom: 'var(--space-6)' }}>
            <span className="badge badge-primary" style={{ marginBottom: 'var(--space-2)' }}>
              {isSubjectLevel ? 'Subject Assessment Complete' : 'Topic Quiz Complete'}
            </span>
            <h1 style={{ fontSize: '2.25rem', fontWeight: '800' }}>
              {isSubjectLevel ? `${result.subject} Performance Report` : `${result.topic} Quiz Result`}
            </h1>
            <p style={{ color: 'var(--text-secondary)' }}>
              {isSubjectLevel
                ? 'Your answers were analyzed across all tested topics to identify strengths and learning recommendations.'
                : 'Spaced repetition retention evaluation.'}
            </p>
          </div>

          {/* Cleared Topic Celebration Banner (For Spaced Repetition Quiz) */}
          {result.topic_cleared && (
            <div
              style={{
                backgroundColor: 'rgba(16, 185, 129, 0.1)',
                border: '2px solid var(--status-success, #10b981)',
                borderRadius: 'var(--radius-lg)',
                padding: 'var(--space-5)',
                marginBottom: 'var(--space-6)',
                display: 'flex',
                alignItems: 'center',
                gap: 'var(--space-4)',
              }}
            >
              <div style={{ color: 'var(--status-success, #10b981)' }}>
                <CheckCircleIcon size={36} />
              </div>
              <div style={{ flex: 1 }}>
                <h3 style={{ color: 'var(--status-success, #10b981)', margin: 0, fontSize: '1.25rem' }}>
                  Topic Cleared! Retention Verified!
                </h3>
                <p style={{ margin: '0.25rem 0 0', color: 'var(--text-secondary)', fontSize: '0.95rem' }}>
                  You cleared <strong>{result.topic}</strong> with {result.percentage}%. Scheduled for next spaced review in {result.next_review_in_days} day(s).
                </p>
              </div>
              {result.next_topic && (
                <Button
                  variant="primary"
                  onClick={() => {
                    startQuizSession(result.subject, result.next_topic.name);
                  }}
                >
                  <span>Advance to {result.next_topic.name}</span>
                  <ArrowRightIcon size={16} />
                </Button>
              )}
            </div>
          )}

          {/* Score Overview Card */}
          <Card style={{ marginBottom: 'var(--space-6)' }}>
            <CardBody>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: 'var(--space-6)', alignItems: 'center' }}>
                <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center' }}>
                  <ProgressCircle percentage={result.percentage} size={130} strokeWidth={10} />
                  <div style={{ marginTop: 'var(--space-3)' }}>
                    <span className={`badge ${result.percentage >= 70 ? 'badge-success' : result.percentage >= 40 ? 'badge-primary' : 'badge-warning'}`}>
                      {result.knowledge_level} Level
                    </span>
                  </div>
                </div>

                <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-3)' }}>
                  <div>
                    <span style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>Score</span>
                    <h3 style={{ fontSize: '1.75rem', fontWeight: '800', margin: 0 }}>
                      {result.score} / {result.total_questions} ({result.percentage}%)
                    </h3>
                  </div>

                  {isSubjectLevel && (
                    <div style={{ display: 'flex', gap: 'var(--space-4)', marginTop: 'var(--space-2)' }}>
                      <div style={{ padding: 'var(--space-3)', backgroundColor: 'var(--bg-surface-subtle)', borderRadius: 'var(--radius-md)', flex: 1 }}>
                        <div style={{ fontSize: '0.75rem', color: 'var(--status-success)' }}>Cleared Topics</div>
                        <div style={{ fontSize: '1.25rem', fontWeight: '700', color: 'var(--status-success)' }}>{passedCount}</div>
                      </div>
                      <div style={{ padding: 'var(--space-3)', backgroundColor: 'var(--bg-surface-subtle)', borderRadius: 'var(--radius-md)', flex: 1 }}>
                        <div style={{ fontSize: '0.75rem', color: 'var(--status-warning)' }}>Needs Review</div>
                        <div style={{ fontSize: '1.25rem', fontWeight: '700', color: 'var(--status-warning)' }}>{weakCount}</div>
                      </div>
                    </div>
                  )}

                  {result.next_review_in_days && (
                    <div style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
                      Spaced repetition interval: <strong>{result.next_review_in_days} day(s)</strong>
                    </div>
                  )}
                </div>
              </div>
            </CardBody>
          </Card>

          {/* Topic-by-Topic Breakdown (For Subject Assessment) */}
          {isSubjectLevel && topicEntries.length > 0 && (
            <Card style={{ marginBottom: 'var(--space-6)' }}>
              <CardHeader>
                <CardTitle>Topic Performance Breakdown</CardTitle>
              </CardHeader>
              <CardBody>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-4)' }}>
                  {topicEntries.map((t) => {
                    const isPassed = t.passed;
                    return (
                      <div
                        key={t.topic}
                        style={{
                          padding: 'var(--space-3) var(--space-4)',
                          borderRadius: 'var(--radius-md)',
                          border: '1px solid var(--border-subtle)',
                          backgroundColor: 'var(--bg-surface)',
                        }}
                      >
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 'var(--space-2)' }}>
                          <div>
                            <span style={{ fontWeight: '600' }}>{t.topic}</span>
                            <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)', marginLeft: 'var(--space-2)' }}>
                              ({t.correct}/{t.total} correct)
                            </span>
                          </div>
                          <span
                            className={`badge ${isPassed ? 'badge-success' : 'badge-warning'}`}
                            style={{ fontSize: '0.75rem' }}
                          >
                            {isPassed ? 'Mastered' : 'Needs Review'}
                          </span>
                        </div>

                        {/* Accuracy bar */}
                        <div style={{ height: '6px', width: '100%', backgroundColor: 'var(--border-subtle)', borderRadius: '999px', overflow: 'hidden' }}>
                          <div
                            style={{
                              height: '100%',
                              width: `${t.percentage}%`,
                              backgroundColor: isPassed ? 'var(--status-success, #10b981)' : 'var(--status-warning, #f59e0b)',
                            }}
                          ></div>
                        </div>
                      </div>
                    );
                  })}
                </div>
              </CardBody>
            </Card>
          )}

          {/* RECOMMENDED TOPIC & STUDY MATERIALS & READY PROMPT */}
          {recommendedTopic && (
            <Card
              style={{
                marginBottom: 'var(--space-6)',
                border: '2px solid var(--primary)',
                boxShadow: 'var(--shadow-md)',
              }}
            >
              <CardHeader style={{ backgroundColor: 'var(--primary-subtle, rgba(99, 102, 241, 0.05))', borderBottom: '1px solid var(--border-subtle)' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 'var(--space-2)' }}>
                  <SparklesIcon size={20} className="text-primary" />
                  <CardTitle style={{ color: 'var(--primary)' }}>Recommended Topic for Learning</CardTitle>
                </div>
              </CardHeader>
              <CardBody>
                <div style={{ marginBottom: 'var(--space-4)' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: 'var(--space-2)', marginBottom: 'var(--space-1)' }}>
                    <h3 style={{ fontSize: '1.35rem', fontWeight: '800', margin: 0 }}>
                      {recommendedTopic.name}
                    </h3>
                    <span className="badge badge-secondary" style={{ fontSize: '0.75rem' }}>
                      {recommendedTopic.difficulty}
                    </span>
                  </div>
                  <p style={{ color: 'var(--text-secondary)', fontSize: '0.95rem', margin: '0.25rem 0' }}>
                    {recommendedTopic.reason}
                  </p>
                </div>

                {/* Curated Study Materials */}
                <div style={{ marginTop: 'var(--space-5)' }}>
                  <h4 style={{ fontSize: '1rem', fontWeight: '700', marginBottom: 'var(--space-3)' }}>
                    Suggested Study Material (YouTube & Websites)
                  </h4>
                  {recommendedTopic.materials && recommendedTopic.materials.length > 0 ? (
                    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: 'var(--space-3)' }}>
                      {recommendedTopic.materials.map((mat, mIdx) => {
                        const isVideo = mat.type === 'youtube';
                        return (
                          <a
                            key={mIdx}
                            href={mat.url}
                            target="_blank"
                            rel="noopener noreferrer"
                            style={{
                              display: 'flex',
                              alignItems: 'flex-start',
                              gap: 'var(--space-3)',
                              padding: 'var(--space-4)',
                              borderRadius: 'var(--radius-md)',
                              border: '1px solid var(--border-medium)',
                              backgroundColor: 'var(--bg-surface)',
                              textDecoration: 'none',
                              color: 'inherit',
                              transition: 'all 0.15s ease',
                            }}
                          >
                            <div
                              style={{
                                color: isVideo ? '#ef4444' : 'var(--primary)',
                                marginTop: '2px',
                                flexShrink: 0,
                              }}
                            >
                              {isVideo ? <YouTubeIcon size={24} /> : <GlobeIcon size={24} />}
                            </div>
                            <div style={{ flex: 1, minWidth: 0 }}>
                              <div style={{ fontWeight: '600', fontSize: '0.9rem', display: 'flex', alignItems: 'center', gap: '0.35rem' }}>
                                <span>{mat.title}</span>
                                <ExternalLinkIcon size={12} />
                              </div>
                              <p style={{ fontSize: '0.8rem', color: 'var(--text-muted)', margin: '0.2rem 0 0' }}>
                                {mat.description}
                              </p>
                            </div>
                          </a>
                        );
                      })}
                    </div>
                  ) : (
                    <p style={{ color: 'var(--text-muted)', fontSize: '0.875rem' }}>
                      Study materials are being indexed for this topic.
                    </p>
                  )}
                </div>

                {/* READINESS CONFIRMATION PROMPT */}
                <div
                  style={{
                    marginTop: 'var(--space-6)',
                    padding: 'var(--space-5)',
                    backgroundColor: 'var(--bg-surface-subtle)',
                    borderRadius: 'var(--radius-lg)',
                    textAlign: 'center',
                    border: '1px dashed var(--border-medium)',
                  }}
                >
                  <h4 style={{ fontSize: '1.1rem', fontWeight: '700', marginBottom: 'var(--space-2)' }}>
                    Are you ready for the assessment?
                  </h4>
                  <p style={{ color: 'var(--text-secondary)', fontSize: '0.875rem', maxWidth: '500px', margin: '0 auto var(--space-4)' }}>
                    Once you have reviewed the study material above, test your understanding and begin your spaced repetition cycle on <strong>{recommendedTopic.name}</strong>.
                  </p>
                  <Button
                    variant="primary"
                    size="lg"
                    onClick={() => {
                      startQuizSession(result.subject, recommendedTopic.name);
                    }}
                  >
                    <span>I'm Ready - Start Spaced Repetition Quiz</span>
                    <ArrowRightIcon size={18} />
                  </Button>
                </div>
              </CardBody>
            </Card>
          )}

          {/* Question Review Section with Explanations */}
          {result.question_results && result.question_results.length > 0 && (
            <Card style={{ marginBottom: 'var(--space-6)' }}>
              <CardHeader>
                <CardTitle>Detailed Question Review</CardTitle>
              </CardHeader>
              <CardBody>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-4)' }}>
                  {result.question_results.map((qr, idx) => (
                    <div
                      key={idx}
                      style={{
                        padding: 'var(--space-4)',
                        borderRadius: 'var(--radius-md)',
                        borderLeft: qr.is_correct ? '4px solid var(--status-success)' : '4px solid var(--status-danger)',
                        backgroundColor: 'var(--bg-surface-subtle)',
                      }}
                    >
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 'var(--space-2)' }}>
                        <span style={{ fontWeight: '700', fontSize: '0.95rem' }}>
                          {idx + 1}. {qr.question}
                        </span>
                        <span className={`badge ${qr.is_correct ? 'badge-success' : 'badge-danger'}`} style={{ fontSize: '0.75rem', flexShrink: 0 }}>
                          {qr.is_correct ? 'Correct' : 'Incorrect'}
                        </span>
                      </div>
                      <div style={{ fontSize: '0.85rem', marginBottom: 'var(--space-1)' }}>
                        <span style={{ color: 'var(--text-muted)' }}>Your Answer: </span>
                        <strong style={{ color: qr.is_correct ? 'var(--status-success)' : 'var(--status-danger)' }}>
                          {qr.your_answer || '(No answer)'}
                        </strong>
                      </div>
                      {!qr.is_correct && (
                        <div style={{ fontSize: '0.85rem', marginBottom: 'var(--space-2)' }}>
                          <span style={{ color: 'var(--text-muted)' }}>Correct Answer: </span>
                          <strong style={{ color: 'var(--status-success)' }}>{qr.correct_answer}</strong>
                        </div>
                      )}
                      {qr.explanation && (
                        <p style={{ fontSize: '0.8rem', color: 'var(--text-secondary)', margin: 'var(--space-2) 0 0', fontStyle: 'italic' }}>
                          💡 {qr.explanation}
                        </p>
                      )}
                    </div>
                  ))}
                </div>
              </CardBody>
            </Card>
          )}

          {/* Action Footer */}
          <div style={{ display: 'flex', justifyContent: 'center', gap: 'var(--space-4)', marginTop: 'var(--space-6)' }}>
            <Button
              variant="outline"
              onClick={() => {
                setSubmitted(false);
                setStarted(false);
                setResult(null);
                startSubjectSession(result.subject);
              }}
            >
              <RefreshCwIcon size={16} />
              <span>Retake {result.subject} Assessment</span>
            </Button>
            <Button variant="primary" onClick={() => navigate('/learning')}>
              <BookOpenIcon size={16} />
              <span>View Curriculum</span>
            </Button>
          </div>
        </div>
      </div>
    );
  }

  return null;
}
