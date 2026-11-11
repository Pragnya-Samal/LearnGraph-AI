import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { SUBJECTS, TOPICS_BY_SUBJECT } from '../data/mockData';
import Card, { CardHeader, CardTitle, CardBody } from '../components/Card';
import Button from '../components/Button';
import {
  BookOpenIcon,
  CheckIcon,
  ArrowRightIcon,
  LayersIcon,
  YouTubeIcon,
  GlobeIcon,
  ExternalLinkIcon,
  TargetIcon,
  SparklesIcon,
} from '../components/Icons';
import { fetchStudyMaterials, fetchDatabaseSubjects } from '../services/api';

export default function Learning() {
  const navigate = useNavigate();
  const [selectedSubject, setSelectedSubject] = useState('OOPS');
  const [selectedTopic, setSelectedTopic] = useState('');
  const [studyMaterials, setStudyMaterials] = useState([]);
  const [loadingMaterials, setLoadingMaterials] = useState(false);
  const [dbSubjects, setDbSubjects] = useState([]);

  // Fetch all 10 topics per subject dynamically from DB
  useEffect(() => {
    let isMounted = true;
    fetchDatabaseSubjects().then((res) => {
      if (isMounted && res.success && res.subjects.length > 0) {
        setDbSubjects(res.subjects);
      }
    });
    return () => {
      isMounted = false;
    };
  }, []);

  // Determine current topics list in hierarchical order
  const activeSubjectData = dbSubjects.find((s) => s.name === selectedSubject);
  const topicsList = activeSubjectData?.topics || (TOPICS_BY_SUBJECT[selectedSubject] || []).map((t, idx) => ({
    name: t,
    display_order: idx + 1,
    difficulty: idx < 3 ? 'Beginner' : idx < 7 ? 'Intermediate' : 'Advanced',
    description: `Concept and applied fundamentals of ${t}`,
  }));

  // Fetch materials when subject & topic are chosen
  useEffect(() => {
    if (selectedSubject && selectedTopic) {
      let isMounted = true;
      setLoadingMaterials(true);
      fetchStudyMaterials(selectedSubject, selectedTopic)
        .then((res) => {
          if (isMounted) {
            setStudyMaterials(res.materials || []);
          }
        })
        .finally(() => {
          if (isMounted) setLoadingMaterials(false);
        });
      return () => {
        isMounted = false;
      };
    } else {
      setStudyMaterials([]);
    }
  }, [selectedSubject, selectedTopic]);

  // Start Subject-Level Assessment
  function handleStartSubjectAssessment(subjectName) {
    const subj = subjectName || selectedSubject;
    navigate('/assessment', { state: { subject: subj, mode: 'subject' } });
  }

  // Start Topic-Level Spaced Repetition Quiz
  function handleStartTopicQuiz(topicName) {
    const top = topicName || selectedTopic;
    navigate('/assessment', { state: { subject: selectedSubject, topic: top, mode: 'quiz' } });
  }

  return (
    <div className="learning-page">
      <div className="container" style={{ maxWidth: '1000px', margin: '0 auto', padding: 'var(--space-6) 0' }}>
        <div className="page-header" style={{ marginBottom: 'var(--space-6)' }}>
          <span className="badge badge-primary" style={{ marginBottom: 'var(--space-2)' }}>
            Curriculum & Knowledge Tracks
          </span>
          <h1 style={{ fontSize: '2.25rem', fontWeight: '800' }}>Hierarchical Learning Tracks</h1>
          <p style={{ color: 'var(--text-secondary)' }}>
            Each subject features 10 ordered topics from Easy to Hard. Take a <strong>Subject Assessment</strong> to identify
            knowledge gaps and receive recommendations, or explore specific topics and their spaced repetition quizzes.
          </p>
        </div>

        <div className="learning-container" style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-6)' }}>
          {/* Course Selection */}
          <Card>
            <CardHeader>
              <CardTitle>1. Choose a Subject Track</CardTitle>
            </CardHeader>
            <CardBody>
              <div className="courses-grid" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))', gap: 'var(--space-4)' }}>
                {SUBJECTS.map((subject) => {
                  const isSelected = selectedSubject === subject.id || selectedSubject === subject.name;
                  return (
                    <div
                      key={subject.id}
                      className={`course-card ${isSelected ? 'active' : ''}`}
                      onClick={() => {
                        setSelectedSubject(subject.name);
                        setSelectedTopic('');
                      }}
                      style={{
                        padding: 'var(--space-5)',
                        borderRadius: 'var(--radius-lg)',
                        border: isSelected ? '2px solid var(--primary)' : '1px solid var(--border-medium)',
                        backgroundColor: isSelected ? 'var(--primary-subtle, rgba(99, 102, 241, 0.08))' : 'var(--bg-surface)',
                        cursor: 'pointer',
                        transition: 'all 0.2s ease',
                      }}
                    >
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 'var(--space-2)' }}>
                        <div className="course-card-icon" style={{ color: isSelected ? 'var(--primary)' : 'var(--text-muted)' }}>
                          <BookOpenIcon size={24} />
                        </div>
                        <span className="badge badge-secondary" style={{ fontSize: '0.75rem' }}>10 Topics</span>
                      </div>
                      <h3 style={{ fontSize: '1.125rem', fontWeight: '700', margin: '0 0 var(--space-1)' }}>{subject.name}</h3>
                      <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', margin: '0 0 var(--space-4)', minHeight: '38px' }}>
                        {subject.description}
                      </p>
                      <Button
                        variant={isSelected ? 'primary' : 'outline'}
                        size="sm"
                        className="btn-full"
                        onClick={(e) => {
                          e.stopPropagation();
                          handleStartSubjectAssessment(subject.name);
                        }}
                      >
                        <TargetIcon size={14} />
                        <span>Take Subject Assessment</span>
                      </Button>
                    </div>
                  );
                })}
              </div>
            </CardBody>
          </Card>

          {/* Hierarchical Topics List (1 to 10 from Easy to Hard) */}
          {selectedSubject && (
            <Card className="animate-fade-in">
              <CardHeader style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: 'var(--space-3)' }}>
                <div>
                  <CardTitle>
                    2. Hierarchical Topics in {selectedSubject} (Easy → Hard)
                  </CardTitle>
                  <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', margin: '0.25rem 0 0' }}>
                    Topics are arranged in difficulty order. Clear one topic to unlock progression to the next.
                  </p>
                </div>
                <Button
                  variant="primary"
                  size="sm"
                  onClick={() => handleStartSubjectAssessment(selectedSubject)}
                >
                  <TargetIcon size={16} />
                  <span>Start {selectedSubject} Assessment</span>
                </Button>
              </CardHeader>
              <CardBody>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-2)' }}>
                  {topicsList.map((top, idx) => {
                    const topName = typeof top === 'string' ? top : top.name;
                    const diff = typeof top === 'object' ? top.difficulty : (idx < 3 ? 'Beginner' : idx < 7 ? 'Intermediate' : 'Advanced');
                    const order = typeof top === 'object' ? top.display_order : idx + 1;
                    const isSelected = selectedTopic === topName;

                    const diffBadgeClass =
                      diff === 'Beginner' ? 'badge-success' : diff === 'Intermediate' ? 'badge-primary' : 'badge-warning';

                    return (
                      <div
                        key={topName}
                        onClick={() => setSelectedTopic(topName)}
                        style={{
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'space-between',
                          padding: 'var(--space-3) var(--space-4)',
                          borderRadius: 'var(--radius-md)',
                          border: isSelected ? '2px solid var(--primary)' : '1px solid var(--border-subtle)',
                          backgroundColor: isSelected ? 'var(--primary-subtle, rgba(99, 102, 241, 0.08))' : 'var(--bg-surface)',
                          cursor: 'pointer',
                          transition: 'all 0.15s ease',
                        }}
                      >
                        <div style={{ display: 'flex', alignItems: 'center', gap: 'var(--space-3)' }}>
                          <span
                            style={{
                              width: '26px',
                              height: '26px',
                              borderRadius: '50%',
                              backgroundColor: isSelected ? 'var(--primary)' : 'var(--bg-surface-subtle)',
                              color: isSelected ? '#fff' : 'var(--text-muted)',
                              display: 'flex',
                              alignItems: 'center',
                              justifyContent: 'center',
                              fontSize: '0.8rem',
                              fontWeight: '700',
                            }}
                          >
                            {order}
                          </span>
                          <div>
                            <span style={{ fontWeight: '600', fontSize: '0.95rem', color: isSelected ? 'var(--primary)' : 'inherit' }}>
                              {topName}
                            </span>
                            {top.description && (
                              <p style={{ fontSize: '0.78rem', color: 'var(--text-muted)', margin: '0.1rem 0 0' }}>
                                {top.description}
                              </p>
                            )}
                          </div>
                        </div>

                        <div style={{ display: 'flex', alignItems: 'center', gap: 'var(--space-3)' }}>
                          <span className={`badge ${diffBadgeClass}`} style={{ fontSize: '0.75rem' }}>
                            {diff}
                          </span>
                          <Button
                            variant="ghost"
                            size="sm"
                            onClick={(e) => {
                              e.stopPropagation();
                              handleStartTopicQuiz(topName);
                            }}
                            title="Take Spaced Repetition Quiz for this topic"
                          >
                            <span>Quiz</span>
                            <ArrowRightIcon size={14} />
                          </Button>
                        </div>
                      </div>
                    );
                  })}
                </div>
              </CardBody>
            </Card>
          )}

          {/* Curated Study Materials Card */}
          {selectedSubject && selectedTopic && (
            <Card className="animate-fade-in" style={{ border: '1px solid var(--primary)' }}>
              <CardHeader>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: 'var(--space-2)' }}>
                  <div>
                    <span className="badge badge-primary" style={{ marginBottom: 'var(--space-1)' }}>Study Resources</span>
                    <CardTitle>Study Materials for {selectedTopic}</CardTitle>
                    <p style={{ fontSize: '0.8125rem', color: 'var(--text-secondary)', marginTop: '0.25rem' }}>
                      Curated YouTube video tutorials & documentation websites
                    </p>
                  </div>
                  <Button
                    variant="primary"
                    onClick={() => handleStartTopicQuiz(selectedTopic)}
                  >
                    <span>Start Spaced Repetition Quiz</span>
                    <ArrowRightIcon size={16} />
                  </Button>
                </div>
              </CardHeader>
              <CardBody>
                {loadingMaterials ? (
                  <p style={{ color: 'var(--text-muted)', fontSize: '0.875rem' }}>Loading study materials from database...</p>
                ) : studyMaterials.length > 0 ? (
                  <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: 'var(--space-3)' }}>
                    {studyMaterials.map((mat) => {
                      const isVideo = mat.type === 'youtube';
                      return (
                        <a
                          key={mat.material_id}
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
                            backgroundColor: 'var(--bg-surface-subtle)',
                            textDecoration: 'none',
                            color: 'inherit',
                            transition: 'all 0.2s ease',
                          }}
                        >
                          <div style={{ marginTop: '2px', color: isVideo ? '#ef4444' : 'var(--primary)', flexShrink: 0 }}>
                            {isVideo ? <YouTubeIcon size={24} /> : <GlobeIcon size={24} />}
                          </div>
                          <div style={{ flex: 1, minWidth: 0 }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: '0.35rem' }}>
                              <h4 style={{ fontSize: '0.9rem', fontWeight: '600', margin: 0 }}>{mat.title}</h4>
                              <ExternalLinkIcon size={12} />
                            </div>
                            <span
                              style={{
                                fontSize: '0.6875rem',
                                textTransform: 'uppercase',
                                fontWeight: '700',
                                padding: '1px 6px',
                                borderRadius: '4px',
                                backgroundColor: isVideo ? 'rgba(239, 68, 68, 0.15)' : 'rgba(99, 102, 241, 0.15)',
                                color: isVideo ? '#ef4444' : 'var(--primary)',
                                display: 'inline-block',
                                marginTop: '4px',
                              }}
                            >
                              {isVideo ? 'YouTube Tutorial' : 'Website Reference'}
                            </span>
                            <p style={{ fontSize: '0.8rem', color: 'var(--text-secondary)', margin: '4px 0 0' }}>
                              {mat.description}
                            </p>
                          </div>
                        </a>
                      );
                    })}
                  </div>
                ) : (
                  <p style={{ color: 'var(--text-muted)', fontSize: '0.875rem' }}>
                    No external links recorded yet for this topic. Review concept notes or proceed directly to the assessment.
                  </p>
                )}
              </CardBody>
            </Card>
          )}
        </div>
      </div>
    </div>
  );
}
