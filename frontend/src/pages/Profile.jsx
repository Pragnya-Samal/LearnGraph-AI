import { useAuth } from '../contexts/AuthContext';
import { useLearning } from '../contexts/LearningContext';
import Card, { CardHeader, CardTitle, CardBody } from '../components/Card';
import Button from '../components/Button';
import { UserIcon, BookOpenIcon, FileTextIcon, TargetIcon, BarChartIcon } from '../components/Icons';

export default function Profile() {
  const { user } = useAuth();
  const { totalAssessments, avgScore } = useLearning();

  const stats = [
    { label: 'Topics Completed', value: String(totalAssessments) },
    { label: 'Assessments Taken', value: String(totalAssessments) },
    { label: 'Average Score', value: totalAssessments > 0 ? `${avgScore}%` : '0%' },
    { label: 'Overall Competence', value: totalAssessments > 0 ? `${avgScore}%` : '0%' },
  ];

  return (
    <div className="profile-page">
      <div className="container">
        <div className="page-header">
          <h1>Learner Profile</h1>
          <p>Review your academic credentials and verified competence records.</p>
        </div>

        <div className="profile-container">
          {/* Profile Card Header */}
          <Card className="main-profile">
            <CardBody>
              <div className="profile-header-content">
                <div className="profile-avatar-large">
                  {user?.name?.[0]?.toUpperCase() || 'U'}
                </div>
                <div className="profile-header-info">
                  <h2>{user?.name || 'Student Learner'}</h2>
                  <p className="profile-branch">{user?.branch || 'Computer Science'}</p>
                  <p className="profile-email">{user?.email}</p>
                </div>
              </div>
            </CardBody>
          </Card>

          {/* Account Information */}
          <Card>
            <CardHeader>
              <CardTitle>Academic & Account Details</CardTitle>
            </CardHeader>
            <CardBody>
              <div className="profile-info-grid">
                <div className="info-item">
                  <label>Full Name</label>
                  <p>{user?.name || 'N/A'}</p>
                </div>
                <div className="info-item">
                  <label>Email Address</label>
                  <p>{user?.email || 'N/A'}</p>
                </div>
                <div className="info-item">
                  <label>Roll / Student ID</label>
                  <p>{user?.rollNumber || 'CS202401'}</p>
                </div>
                <div className="info-item">
                  <label>Department / Branch</label>
                  <p>{user?.branch || 'Computer Science'}</p>
                </div>
              </div>
            </CardBody>
          </Card>

          {/* Learning Statistics */}
          <Card>
            <CardHeader>
              <CardTitle>Performance Records</CardTitle>
            </CardHeader>
            <CardBody>
              <div className="stats-grid-profile">
                {stats.map((stat) => (
                  <div key={stat.label} className="stat-card-profile">
                    <div className="stat-value-profile">{stat.value}</div>
                    <div className="stat-label-profile">{stat.label}</div>
                  </div>
                ))}
              </div>
            </CardBody>
          </Card>

          {/* Learning Pathway Level */}
          <Card>
            <CardHeader>
              <CardTitle>Evaluated Pathway Classification</CardTitle>
            </CardHeader>
            <CardBody>
              <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-2)' }}>
                <span className="badge badge-primary" style={{ width: 'fit-content', fontSize: '0.875rem', padding: '0.375rem 0.875rem' }}>
                  {totalAssessments === 0 ? 'Not Assessed' : avgScore >= 70 ? 'Advanced Learner' : avgScore >= 40 ? 'Intermediate Learner' : 'Beginner Learner'}
                </span>
                <p style={{ color: 'var(--text-secondary)', fontSize: '0.9375rem', lineHeight: 1.5, marginTop: 'var(--space-1)' }}>
                  {totalAssessments === 0
                    ? 'Complete assessments to receive your pathway classification.'
                    : avgScore >= 70
                    ? 'Outstanding performance! You have demonstrated advanced competence across assessed topics.'
                    : avgScore >= 40
                    ? 'Solid foundation established. Continue assessments to advance your classification.'
                    : 'Keep practicing. Revisit core concepts to improve your knowledge level.'}
                </p>
              </div>
            </CardBody>
          </Card>
        </div>
      </div>
    </div>
  );
}
