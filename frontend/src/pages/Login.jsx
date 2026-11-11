import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import Input from '../components/Input';
import Button from '../components/Button';
import { BrainIcon, ArrowRightIcon, AlertCircleIcon } from '../components/Icons';

export default function Login() {
  const { login } = useAuth();
  const navigate = useNavigate();
  const [form, setForm] = useState({ email: '', password: '' });
  const [error, setError] = useState('');
  const [rememberMe, setRememberMe] = useState(false);

  function validate() {
    if (!form.email.trim()) return 'Email is required.';
    if (!/\S+@\S+\.\S+/.test(form.email)) return 'Enter a valid email address.';
    if (!form.password) return 'Password is required.';
    return null;
  }

  function handleSubmit(e) {
    e.preventDefault();
    const validationError = validate();
    if (validationError) {
      setError(validationError);
      return;
    }
    const result = login(form.email, form.password);
    if (!result.success) {
      setError(result.message);
      return;
    }
    navigate('/dashboard');
  }

  function handleChange(e) {
    setForm((prev) => ({ ...prev, [e.target.name]: e.target.value }));
    setError('');
  }

  return (
    <div className="auth-page login-page">
      <div className="auth-left">
        <div className="auth-left-content">
          <div className="auth-logo">
            <div className="navbar-logo-icon-wrapper">
              <BrainIcon size={24} />
            </div>
            <h2>LearnGraph AI</h2>
          </div>
          <p className="auth-tagline">
            Understand what you know.<br />
            Discover what to learn next.
          </p>
          <div className="auth-visual">
            <KnowledgeGraphMini />
          </div>
        </div>
      </div>

      <div className="auth-right">
        <div className="auth-form-wrapper">
          <h1>Welcome Back</h1>
          <p className="auth-subtitle">Sign in to resume your learning pathway.</p>

          <form onSubmit={handleSubmit} noValidate>
            <Input
              id="email"
              name="email"
              type="email"
              label="Email Address"
              value={form.email}
              onChange={handleChange}
              placeholder="name@example.com"
              autoComplete="email"
            />

            <Input
              id="password"
              name="password"
              type="password"
              label="Password"
              value={form.password}
              onChange={handleChange}
              placeholder="Enter your password"
              autoComplete="current-password"
            />

            <div className="form-options">
              <label className="checkbox-label">
                <input
                  type="checkbox"
                  checked={rememberMe}
                  onChange={(e) => setRememberMe(e.target.checked)}
                />
                <span>Remember me</span>
              </label>
              <a href="#forgot" className="forgot-link">
                Forgot password?
              </a>
            </div>

            {error && (
              <div className="alert alert-error">
                <AlertCircleIcon size={18} />
                <span>{error}</span>
              </div>
            )}

            <Button variant="primary" className="btn-full" type="submit">
              <span>Sign In</span>
              <ArrowRightIcon size={16} />
            </Button>
          </form>

          <p className="auth-switch">
            Don&apos;t have an account? <Link to="/register">Create one</Link>
          </p>
        </div>
      </div>
    </div>
  );
}

function KnowledgeGraphMini() {
  return (
    <svg viewBox="0 0 200 160" className="knowledge-graph-mini" style={{ width: '100%', maxWidth: '220px' }}>
      <defs>
        <linearGradient id="miniGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="#818cf8" />
          <stop offset="100%" stopColor="#c084fc" />
        </linearGradient>
      </defs>
      <line x1="100" y1="30" x2="60" y2="80" stroke="rgba(255,255,255,0.2)" strokeWidth="1.5" />
      <line x1="100" y1="30" x2="140" y2="80" stroke="rgba(255,255,255,0.2)" strokeWidth="1.5" />
      <line x1="60" y1="80" x2="100" y2="130" stroke="rgba(255,255,255,0.2)" strokeWidth="1.5" />
      <line x1="140" y1="80" x2="100" y2="130" stroke="rgba(255,255,255,0.2)" strokeWidth="1.5" />
      <circle cx="100" cy="30" r="14" fill="url(#miniGrad)" />
      <circle cx="60" cy="80" r="12" fill="#6366f1" />
      <circle cx="140" cy="80" r="12" fill="#6366f1" />
      <circle cx="100" cy="130" r="12" fill="#a855f7" />
    </svg>
  );
}
