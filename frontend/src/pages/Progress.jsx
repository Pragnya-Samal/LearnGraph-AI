import { useState } from 'react';
import { useLearning } from '../contexts/LearningContext';
import Card, { CardHeader, CardTitle, CardBody } from '../components/Card';
import ProgressCircle from '../components/ProgressCircle';
import DonutChart from '../components/DonutChart';
import { SUBJECTS } from '../data/mockData';
import { CheckCircleIcon, AlertTriangleIcon } from '../components/Icons';

export default function Progress() {
  const { totalAssessments, avgScore, conceptMap, subjectProgressList, getDonutData } = useLearning();
  const [donutSubject, setDonutSubject] = useState('');

  const strongConcepts = Object.entries(conceptMap)
    .filter(([_, s]) => s.status === 'Strong' || s.status === 'Uncertain')
    .map(([name]) => name);

  const weakConcepts = Object.entries(conceptMap)
    .filter(([_, s]) => s.status === 'Weak')
    .map(([name]) => name);

  return (
    <div className="progress-page">
      <div className="container">
        <div className="page-header">
          <h1>Learning Progress & Analytics</h1>
          <p>Evaluate your verified performance and identify areas to prioritize.</p>
        </div>

        <div className="progress-container">
          <Card>
            <CardHeader><CardTitle>Overall Subject Competence</CardTitle></CardHeader>
            <CardBody>
              <div className="overall-progress-display">
                <ProgressCircle percentage={totalAssessments > 0 ? avgScore : 0} size={150} label="Average Score" />
                <div className="progress-stats">
                  <div className="stat-item">
                    <span className="stat-label">Topics Assessed</span>
                    <span className="stat-value">{totalAssessments}</span>
                  </div>
                  <div className="stat-item">
                    <span className="stat-label">Assessments Taken</span>
                    <span className="stat-value">{totalAssessments}</span>
                  </div>
                  <div className="stat-item">
                    <span className="stat-label">Overall Average Score</span>
                    <span className="stat-value">{totalAssessments > 0 ? `${avgScore}%` : '0%'}</span>
                  </div>
                </div>
              </div>
            </CardBody>
          </Card>

          <Card>
            <CardHeader>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: 'var(--space-3)' }}>
                <CardTitle>Knowledge Progress</CardTitle>
                <select
                  value={donutSubject}
                  onChange={(e) => setDonutSubject(e.target.value)}
                  className="form-select"
                  style={{ width: 'auto', minWidth: '180px', fontSize: '0.875rem' }}
                >
                  <option value="">All Subjects</option>
                  {SUBJECTS.map((s) => <option key={s.id} value={s.id}>{s.name}</option>)}
                </select>
              </div>
            </CardHeader>
            <CardBody>
              <DonutChart
                data={getDonutData(donutSubject)}
                title={donutSubject ? `${donutSubject} Learning Progress` : 'Overall Learning Progress'}
                centerLabel="Mastered"
              />
            </CardBody>
          </Card>

          <Card>
            <CardHeader><CardTitle>Subject Performance Breakdown</CardTitle></CardHeader>
            <CardBody>
              {subjectProgressList.some(s => s.progress > 0) ? (
                <div className="subject-performance-list">
                  {subjectProgressList.map((item) => (
                    <div key={item.subject} className="performance-item">
                      <div className="performance-header">
                        <span className="performance-subject">{item.subject}</span>
                        <span className="performance-percent">{item.progress > 0 ? `${item.progress}%` : 'Not Assessed'}</span>
                      </div>
                      <div className="performance-bar">
                        <div className="performance-fill" style={{ width: `${item.progress}%` }}></div>
                      </div>
                    </div>
                  ))}
                </div>
              ) : (
                <p style={{ color: 'var(--text-muted)', fontSize: '0.875rem' }}>No assessments taken yet.</p>
              )}
            </CardBody>
          </Card>

          <Card>
            <CardHeader><CardTitle>Strong Concepts</CardTitle></CardHeader>
            <CardBody>
              {strongConcepts.length > 0 ? (
                <div className="concepts-grid">
                  {strongConcepts.map((concept) => (
                    <div key={concept} className="concept-badge strong">
                      <CheckCircleIcon size={18} />
                      <span>{concept}</span>
                    </div>
                  ))}
                </div>
              ) : (
                <p style={{ color: 'var(--text-muted)', fontSize: '0.875rem' }}>Complete assessments to identify your strong concepts.</p>
              )}
            </CardBody>
          </Card>

          <Card>
            <CardHeader><CardTitle>Concepts Needing Attention</CardTitle></CardHeader>
            <CardBody>
              {weakConcepts.length > 0 ? (
                <div className="concepts-grid">
                  {weakConcepts.map((concept) => (
                    <div key={concept} className="concept-badge attention">
                      <AlertTriangleIcon size={18} />
                      <span>{concept}</span>
                    </div>
                  ))}
                </div>
              ) : (
                <p style={{ color: 'var(--text-muted)', fontSize: '0.875rem' }}>
                  {totalAssessments === 0 ? 'Complete assessments to identify concepts needing attention.' : 'No weak concepts detected. Keep it up!'}
                </p>
              )}
            </CardBody>
          </Card>
        </div>
      </div>
    </div>
  );
}
