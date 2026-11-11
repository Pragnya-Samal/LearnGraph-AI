import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import { useLearning } from '../contexts/LearningContext';
import { SUBJECTS, TOPICS_BY_SUBJECT } from '../data/mockData';
import Card, { CardHeader, CardTitle, CardBody } from '../components/Card';
import Button from '../components/Button';
import {
  ArrowRightIcon,
  BookOpenIcon,
  BarChartIcon,
  TargetIcon,
  ClockIcon,
  FileTextIcon,
  CheckCircleIcon,
  RefreshCwIcon,
} from '../components/Icons';
import { fetchStudentProgress } from '../services/api';

export default function Dashboard() {
  const { user } = useAuth();
  const navigate = useNavigate();
  const { assessmentResults, lastTopic, totalAssessments, avgScore, recommendations, subjectProgressList } = useLearning();

  const [selectedSubject, setSelectedSubject] = useState('');
  const [selectedTopic, setSelectedTopic] = useState('');
  const [revisions, setRevisions] = useState([]);
  const [loadingRevisions, setLoadingRevisions] = useState(false);

  const topics = selectedSubject ? TOPICS_BY_SUBJECT[selectedSubject] || [] : [];

  useEffect(() => {
    let isMounted = true;
    setLoadingRevisions(true);
    fetchStudentProgress(1)
      .then((res) => {
        if (isMounted && res.success) {
          setRevisions(res.upcomingRevisions || []);
        }
      })
      .finally(() => {
        if (isMounted) setLoadingRevisions(false);
      });
    return () => {
      isMounted = false;
    };
  }, [totalAssessments]);

  function handleStartAssessment() {
    if (!selectedSubject) {
      alert('Please select a course before starting the assessment.');
      return;
    }
    if (selectedTopic) {
      navigate('/assessment', { state: { subject: selectedSubject, topic: selectedTopic, mode: 'quiz' } });
    } else {
      navigate('/assessment', { state: { subject: selectedSubject, mode: 'subject' } });
    }
  }

  function handleContinueLearning() {
    if (lastTopic) {
      navigate('/assessment', { state: { subject: lastTopic.subject, topic: lastTopic.topic } });
    } else {
      navigate('/learning');
    }
  }

  return (
    <div className="dashboard-page">
      <div className="container">
        <section className="dashboard-welcome">
          <div className="welcome-greeting">
            <h1>Welcome back, {user?.name?.split(' ')[0]}</h1>
            <p>Track your verified competence and discover recommended next topics.</p>
          </div>
          <div className="welcome-badge">
            <span className="learner-level-badge">
              <TargetIcon size={16} />
              <span>{totalAssessments === 0 ? 'Not Assessed' : avgScore >= 70 ? 'Advanced Learner' : avgScore >= 40 ? 'Intermediate Learner' : 'Beginner Learner'}</span>
            </span>
          </div>
        </section>

        <Card className="continue-learning-hero" hover>
          <CardBody>
            <div className="hero-content-grid">
              <div className="hero-text">
                <span className="badge badge-primary" style={{ marginBottom: '0.5rem' }}>Active Focus</span>
                <div className="hero-topic-info">
                  <h3>{lastTopic ? lastTopic.topic : 'Start Your First Assessment'}</h3>
                  <p className="hero-subject">{lastTopic ? lastTopic.subject : 'Select a topic to begin'}</p>
                </div>
                {lastTopic && (
                  <div className="hero-progress">
                    <div className="progress-bar-hero">
                      <div className="progress-fill-hero" style={{ width: `${lastTopic.percentage}%` }}></div>
                    </div>
                    <span className="progress-label-hero">{lastTopic.percentage}% Score</span>
                  </div>
                )}
                <p className="hero-description">
                  {lastTopic
                    ? `Latest score: ${lastTopic.percentage}% (${lastTopic.knowledge_level}). Continue practicing to strengthen this topic.`
                    : 'You have no assessments yet. Select a topic from the Learning page to get started.'}
                </p>
                <Button variant="primary" onClick={handleContinueLearning}>
                  <span>{lastTopic ? 'Continue Learning' : 'Start Learning'}</span>
                  <ArrowRightIcon size={16} />
                </Button>
              </div>
              <div className="hero-visual">
                <svg viewBox="0 0 200 180" className="hero-illustration" style={{ width: '100%', maxWidth: '180px' }}>
                  <defs>
                    <linearGradient id="heroNodeG" x1="0%" y1="0%" x2="100%" y2="100%">
                      <stop offset="0%" stopColor="#4f46e5" />
                      <stop offset="100%" stopColor="#8b5cf6" />
                    </linearGradient>
                  </defs>
                  <line x1="100" y1="40" x2="60" y2="90" stroke="var(--border-medium)" strokeWidth="2" />
                  <line x1="100" y1="40" x2="140" y2="90" stroke="var(--border-medium)" strokeWidth="2" />
                  <line x1="60" y1="90" x2="40" y2="140" stroke="var(--border-medium)" strokeWidth="1.5" />
                  <line x1="60" y1="90" x2="80" y2="140" stroke="var(--border-medium)" strokeWidth="1.5" />
                  <circle cx="100" cy="40" r="16" fill="url(#heroNodeG)" />
                  <circle cx="60" cy="90" r="14" fill="#4f46e5" opacity="0.85" />
                  <circle cx="140" cy="90" r="14" fill="#4f46e5" opacity="0.85" />
                  <circle cx="40" cy="140" r="10" fill="#10b981" />
                  <circle cx="80" cy="140" r="10" fill="#f59e0b" />
                </svg>
              </div>
            </div>
          </CardBody>
        </Card>

        <div className="quick-stats">
          <div className="stat-box">
            <div className="stat-box-icon"><BarChartIcon size={20} /></div>
            <div className="stat-number">{totalAssessments > 0 ? `${avgScore}%` : '0%'}</div>
            <div className="stat-name">Overall Knowledge</div>
          </div>
          <div className="stat-box">
            <div className="stat-box-icon"><BookOpenIcon size={20} /></div>
            <div className="stat-number">{totalAssessments}</div>
            <div className="stat-name">Topics Completed</div>
          </div>
          <div className="stat-box">
            <div className="stat-box-icon"><FileTextIcon size={20} /></div>
            <div className="stat-number">{totalAssessments}</div>
            <div className="stat-name">Assessments Taken</div>
          </div>
          <div className="stat-box">
            <div className="stat-box-icon"><TargetIcon size={20} /></div>
            <div className="stat-number">{totalAssessments > 0 ? `${avgScore}%` : '0%'}</div>
            <div className="stat-name">Average Score</div>
          </div>
        </div>

        <div className="dashboard-content">
          <div className="dashboard-column-left">
            <Card style={{ marginBottom: 'var(--space-6)' }}>
              <CardHeader><CardTitle>Select Course & Topic</CardTitle></CardHeader>
              <CardBody>
                <p style={{ fontSize: '0.875rem', color: 'var(--text-secondary)', marginBottom: 'var(--space-4)' }}>
                  Choose a subject to take a comprehensive 10-topic assessment, or select a topic for a targeted spaced repetition quiz.
                </p>
                <div className="form-group">
                  <label htmlFor="course-select">Course / Subject</label>
                  <select id="course-select" value={selectedSubject} onChange={(e) => { setSelectedSubject(e.target.value); setSelectedTopic(''); }} className="form-select">
                    <option value="">-- Select Course --</option>
                    {SUBJECTS.map((s) => <option key={s.id} value={s.id}>{s.name}</option>)}
                  </select>
                </div>
                <div className="form-group">
                  <label htmlFor="topic-select">Topic (Optional - for direct quiz)</label>
                  <select id="topic-select" value={selectedTopic} onChange={(e) => setSelectedTopic(e.target.value)} disabled={!selectedSubject} className="form-select">
                    <option value="">-- All Topics (Subject Assessment) --</option>
                    {topics.map((t) => <option key={t} value={t}>{t}</option>)}
                  </select>
                </div>
                <Button variant="primary" className="btn-full" onClick={handleStartAssessment} disabled={!selectedSubject}>
                  <span>{selectedTopic ? `Start ${selectedTopic} Quiz` : `Start ${selectedSubject || 'Subject'} Assessment`}</span>
                  <ArrowRightIcon size={16} />
                </Button>
              </CardBody>
            </Card>

            <Card>
              <CardHeader><CardTitle>Subject Performance</CardTitle></CardHeader>
              <CardBody>
                <div className="progress-list">
                  {subjectProgressList.length > 0 ? subjectProgressList.map((item) => (
                    <div key={item.subject} className="progress-item-dashboard">
                      <div className="progress-header-dashboard">
                        <span className="progress-subject-dashboard">{item.subject}</span>
                        <span className="progress-value-dashboard">{item.progress > 0 ? `${item.progress}%` : 'Not Assessed'}</span>
                      </div>
                      <div className="progress-bar-dashboard">
                        <div className="progress-fill-dashboard" style={{ width: `${item.progress}%` }}></div>
                      </div>
                    </div>
                  )) : (
                    <p style={{ color: 'var(--text-muted)', fontSize: '0.875rem' }}>No assessments taken yet. Complete assessments to see your subject performance.</p>
                  )}
                </div>
              </CardBody>
            </Card>
          </div>

          <div className="dashboard-column-right">
            <Card style={{ marginBottom: 'var(--space-6)' }}>
              <CardHeader><CardTitle>Your Knowledge Profile</CardTitle></CardHeader>
              <CardBody>
                <div className="knowledge-profile-list">
                  {assessmentResults.length > 0 ? (
                    assessmentResults.map((r) => (
                      <div key={`${r.subject}-${r.topic}`} className="knowledge-item">
                        <div className="knowledge-header">
                          <span className="knowledge-topic">{r.topic}</span>
                          <span className={`badge ${r.percentage >= 70 ? 'badge-success' : r.percentage >= 40 ? 'badge-primary' : 'badge-warning'}`}>
                            {r.knowledge_level}
                          </span>
                        </div>
                        <div className="knowledge-bar">
                          <div className="knowledge-fill" style={{ width: `${r.percentage}%`, backgroundColor: r.percentage >= 70 ? 'var(--status-success)' : r.percentage >= 40 ? 'var(--primary)' : 'var(--status-warning)' }}></div>
                        </div>
                      </div>
                    ))
                  ) : (
                    <p style={{ color: 'var(--text-muted)', fontSize: '0.875rem' }}>No assessments completed yet. Your knowledge profile will appear here after your first assessment.</p>
                  )}
                </div>
              </CardBody>
            </Card>

            <Card className="assessment-cta-card">
              <div className="cta-content">
                <h3>Adaptive Topic Assessment</h3>
                <p>Validate your understanding to update your verified profile.</p>
                <div className="cta-details">
                  <div className="cta-detail-item"><FileTextIcon size={14} /><span>Multiple Choice</span></div>
                  <div className="cta-detail-item"><ClockIcon size={14} /><span>Self-Paced</span></div>
                  <div className="cta-detail-item"><CheckCircleIcon size={14} /><span>Instant Evaluation</span></div>
                </div>
                <Button variant="primary" className="btn-full" onClick={() => navigate('/learning')}>
                  <span>Explore All Assessments</span>
                  <ArrowRightIcon size={16} />
                </Button>
              </div>
            </Card>
          </div>
        </div>

        {/* Spaced Repetition Quizzes Section */}
        <section className="spaced-repetition-section" style={{ marginTop: 'var(--space-6)', marginBottom: 'var(--space-6)' }}>
          <div className="page-header" style={{ marginBottom: 'var(--space-3)' }}>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: 'var(--space-2)' }}>
              <div>
                <h2>Spaced Repetition Review Schedule</h2>
                <p>
                  Active revision ladder: <strong>Tomorrow (1d) ➔ 3 Days Later ➔ 7 Days Later ➔ 30 Days Later</strong>. Pass to advance; fail to drop back.
                </p>
              </div>
              <span className="badge badge-primary">
                {revisions.length} Active Topic Schedules
              </span>
            </div>
          </div>

          {revisions.length > 0 ? (
            <div className="recommendations-grid">
              {revisions.map((rev) => (
                <Card key={rev.revision_id} className="rec-card" hover>
                  <div className="rec-header">
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 'var(--space-2)' }}>
                      <span className="rec-subject">{rev.subject_name}</span>
                      <span className="badge badge-secondary" style={{ fontSize: '0.6875rem' }}>
                        {rev.interval_label}
                      </span>
                    </div>
                    <h3>{rev.topic_name}</h3>
                    <p style={{ fontSize: '0.8125rem', color: 'var(--text-secondary)', margin: '4px 0 8px' }}>
                      Last Score: <strong>{rev.score}%</strong> • Next Review: <strong>{new Date(rev.next_review).toLocaleDateString()}</strong>
                    </p>
                    <div style={{ display: 'flex', gap: '4px', margin: '8px 0' }}>
                      {[1, 3, 7, 30].map((step) => {
                        const isCurrent = rev.current_interval_days === step;
                        return (
                          <div
                            key={step}
                            style={{
                              flex: 1,
                              padding: '2px 4px',
                              textAlign: 'center',
                              borderRadius: '3px',
                              fontSize: '0.625rem',
                              fontWeight: isCurrent ? '700' : '400',
                              backgroundColor: isCurrent ? 'var(--primary)' : 'var(--bg-surface-subtle)',
                              color: isCurrent ? '#fff' : 'var(--text-muted)',
                              border: `1px solid ${isCurrent ? 'var(--primary)' : 'var(--border-subtle)'}`
                            }}
                          >
                            {step === 1 ? '1d' : `${step}d`}
                          </div>
                        );
                      })}
                    </div>
                  </div>
                  <Button
                    variant="primary"
                    size="sm"
                    className="btn-full"
                    onClick={() => navigate('/assessment', { state: { subject: rev.subject_name, topic: rev.topic_name } })}
                  >
                    <span>Take 30Q Review Quiz</span>
                    <ArrowRightIcon size={14} />
                  </Button>
                </Card>
              ))}
            </div>
          ) : (
            <Card>
              <CardBody>
                <div style={{ textAlign: 'center', padding: 'var(--space-4)' }}>
                  <p style={{ color: 'var(--text-muted)', fontSize: '0.875rem', margin: 0 }}>
                    No topic reviews scheduled yet. Complete your first topic assessment to start your spaced repetition ladder (1d ➔ 3d ➔ 7d ➔ 30d).
                  </p>
                </div>
              </CardBody>
            </Card>
          )}
        </section>

        <section className="recommendations-section">
          <div className="page-header" style={{ marginBottom: 'var(--space-4)' }}>
            <h2>Recommended Topics</h2>
            <p>{recommendations.length > 0 ? 'Personalized based on your assessment history and concept prerequisites.' : 'Complete assessments to receive personalized recommendations.'}</p>
          </div>
          {recommendations.length > 0 ? (
            <div className="recommendations-grid">
              {recommendations.map((rec, i) => (
                <Card key={i} className="rec-card" hover>
                  <div className="rec-header">
                    <span className="rec-subject">{rec.subject}</span>
                    <h3>{rec.topic}</h3>
                    <p className="rec-reason">{rec.reason}</p>
                  </div>
                  <Button variant="outline" size="sm" onClick={() => navigate('/assessment', { state: { subject: rec.subject, topic: rec.topic } })}>
                    <span>Start Topic</span>
                    <ArrowRightIcon size={14} />
                  </Button>
                </Card>
              ))}
            </div>
          ) : (
            <Card>
              <CardBody>
                <p style={{ color: 'var(--text-muted)', textAlign: 'center', padding: 'var(--space-6)' }}>
                  Take your first assessment to unlock personalized topic recommendations.
                </p>
              </CardBody>
            </Card>
          )}
        </section>
      </div>
    </div>
  );
}
