import { Link } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import {
  ArrowRightIcon,
  BrainIcon,
  BookOpenIcon,
  BarChartIcon,
  TargetIcon,
  LayersIcon,
} from '../components/Icons';

export default function Home() {
  const { user } = useAuth();

  return (
    <div className="home-page">
      {/* Hero Section */}
      <section className="hero">
        <div className="container">
          <div className="hero-content">
            <div className="hero-text">
              <h1>Learn Smarter. Understand Deeper.</h1>
              <p className="hero-subtitle">
                An adaptive learning platform that analyzes your knowledge, visualizes concept relationships, and helps you discover what to learn next.
              </p>
              <div className="hero-cta">
                {user ? (
                  <Link to="/dashboard" className="btn btn-primary btn-lg">
                    <span>Go to Dashboard</span>
                    <ArrowRightIcon size={18} />
                  </Link>
                ) : (
                  <>
                    <Link to="/register" className="btn btn-primary btn-lg">
                      <span>Start Learning</span>
                      <ArrowRightIcon size={18} />
                    </Link>
                    <a href="#how-it-works" className="btn btn-secondary btn-lg">
                      Explore How It Works
                    </a>
                  </>
                )}
              </div>
            </div>
            <div className="hero-visual">
              <KnowledgeGraphViz />
            </div>
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section className="how-it-works" id="how-it-works">
        <div className="container">
          <div className="page-header" style={{ textAlign: 'center' }}>
            <h2>How LearnGraph Works</h2>
            <p>A systematic cycle designed to reinforce mastery and bridge knowledge gaps.</p>
          </div>
          <div className="steps-grid">
            <div className="step-card">
              <div className="step-number">01</div>
              <h3>Assess</h3>
              <p>Take focused assessments to evaluate your current understanding across computer science topics.</p>
            </div>
            <div className="step-card">
              <div className="step-number">02</div>
              <h3>Understand</h3>
              <p>The system evaluates your answers and classifies your knowledge level into actionable feedback.</p>
            </div>
            <div className="step-card">
              <div className="step-number">03</div>
              <h3>Connect</h3>
              <p>Explore your interactive Knowledge Map to see prerequisites and relationships between concepts.</p>
            </div>
            <div className="step-card">
              <div className="step-number">04</div>
              <h3>Recommend</h3>
              <p>Receive tailored topic suggestions that build directly on concepts you have already mastered.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="features" id="features">
        <div className="container">
          <div className="page-header" style={{ textAlign: 'center' }}>
            <h2>Platform Capabilities</h2>
            <p>Engineered to accelerate concept comprehension and retention.</p>
          </div>
          <div className="features-grid">
            <div className="feature-card">
              <div className="feature-icon-wrapper">
                <TargetIcon size={24} />
              </div>
              <h3>Personalized Paths</h3>
              <p>Targeted learning paths mapped to your verified subject competence.</p>
            </div>
            <div className="feature-card">
              <div className="feature-icon-wrapper">
                <BrainIcon size={24} />
              </div>
              <h3>Knowledge Graph</h3>
              <p>Explore inter-connected concept nodes, dependencies, and mastery ratings.</p>
            </div>
            <div className="feature-card">
              <div className="feature-icon-wrapper">
                <BookOpenIcon size={24} />
              </div>
              <h3>Curriculum Hub</h3>
              <p>Comprehensive coverage of Data Structures, Algorithms, DBMS, ML, and OOPS.</p>
            </div>
            <div className="feature-card">
              <div className="feature-icon-wrapper">
                <BarChartIcon size={24} />
              </div>
              <h3>Progress Analytics</h3>
              <p>Gain visibility into strengths and topics requiring immediate attention.</p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}

function KnowledgeGraphViz() {
  return (
    <svg viewBox="0 0 300 300" className="knowledge-graph-svg">
      <defs>
        <linearGradient id="heroNodeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="#4f46e5" />
          <stop offset="100%" stopColor="#8b5cf6" />
        </linearGradient>
      </defs>

      {/* Connecting Edges */}
      <line x1="150" y1="50" x2="90" y2="120" stroke="var(--border-medium)" strokeWidth="2" strokeDasharray="3 3" />
      <line x1="150" y1="50" x2="210" y2="120" stroke="var(--border-medium)" strokeWidth="2" strokeDasharray="3 3" />
      <line x1="90" y1="120" x2="150" y2="190" stroke="var(--border-medium)" strokeWidth="2" />
      <line x1="210" y1="120" x2="150" y2="190" stroke="var(--border-medium)" strokeWidth="2" />
      <line x1="150" y1="190" x2="150" y2="260" stroke="var(--border-medium)" strokeWidth="2" />

      {/* Nodes */}
      <circle cx="150" cy="50" r="22" fill="url(#heroNodeGrad)" />
      <text x="150" y="55" textAnchor="middle" fill="#ffffff" fontSize="11" fontWeight="700">
        Course
      </text>

      <circle cx="90" cy="120" r="18" fill="#4f46e5" opacity="0.9" />
      <text x="90" y="124" textAnchor="middle" fill="#ffffff" fontSize="10" fontWeight="600">
        Topic A
      </text>

      <circle cx="210" cy="120" r="18" fill="#4f46e5" opacity="0.9" />
      <text x="210" y="124" textAnchor="middle" fill="#ffffff" fontSize="10" fontWeight="600">
        Topic B
      </text>

      <circle cx="150" cy="190" r="20" fill="#8b5cf6" opacity="0.9" />
      <text x="150" y="195" textAnchor="middle" fill="#ffffff" fontSize="10" fontWeight="600">
        Concept
      </text>

      <circle cx="150" cy="260" r="16" fill="#10b981" opacity="0.95" />
      <text x="150" y="264" textAnchor="middle" fill="#ffffff" fontSize="9" fontWeight="700">
        Mastery
      </text>
    </svg>
  );
}
