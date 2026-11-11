import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import Input from '../components/Input';
import Button from '../components/Button';
import { BrainIcon, ArrowRightIcon, CheckIcon, AlertCircleIcon } from '../components/Icons';

const INITIAL = { name: '', email: '', password: '', confirmPassword: '', rollNumber: '', branch: '' };

export default function Register() {
  const { register } = useAuth();
  const navigate = useNavigate();
  const [form, setForm] = useState(INITIAL);
  const [errors, setErrors] = useState({});

  function validate() {
    const e = {};
    if (!form.name.trim()) e.name = 'Name is required.';
    if (!form.email.trim()) e.email = 'Email is required.';
    else if (!/\S+@\S+\.\S+/.test(form.email)) e.email = 'Enter a valid email.';
    if (!form.password) e.password = 'Password is required.';
    else if (form.password.length < 6) e.password = 'Password must be at least 6 characters.';
    if (!form.confirmPassword) e.confirmPassword = 'Please confirm your password.';
    else if (form.password !== form.confirmPassword) e.confirmPassword = 'Passwords do not match.';
    if (!form.rollNumber.trim()) e.rollNumber = 'Roll number is required.';
    if (!form.branch.trim()) e.branch = 'Branch is required.';
    return e;
  }

  function handleSubmit(e) {
    e.preventDefault();
    const validationErrors = validate();
    if (Object.keys(validationErrors).length > 0) {
      setErrors(validationErrors);
      return;
    }
    const result = register({
      name: form.name,
      email: form.email,
      password: form.password,
      rollNumber: form.rollNumber,
      branch: form.branch,
    });
    if (!result.success) {
      setErrors({ email: result.message });
      return;
    }
    navigate('/dashboard');
  }

  function handleChange(e) {
    setForm((prev) => ({ ...prev, [e.target.name]: e.target.value }));
    setErrors((prev) => ({ ...prev, [e.target.name]: '' }));
  }

  return (
    <div className="auth-page register-page">
      <div className="auth-left">
        <div className="auth-left-content">
          <div className="auth-logo">
            <div className="navbar-logo-icon-wrapper">
              <BrainIcon size={24} />
            </div>
            <h2>LearnGraph AI</h2>
          </div>
          <p className="auth-tagline">
            Join learners advancing their mastery in core computer science.
          </p>
          <div className="auth-benefits">
            <div className="benefit-item">
              <span className="benefit-check"><CheckIcon size={16} /></span>
              <span>Adaptive Skill Assessments</span>
            </div>
            <div className="benefit-item">
              <span className="benefit-check"><CheckIcon size={16} /></span>
              <span>Intelligent Topic Recommendations</span>
            </div>
            <div className="benefit-item">
              <span className="benefit-check"><CheckIcon size={16} /></span>
              <span>Interactive Knowledge Map</span>
            </div>
            <div className="benefit-item">
              <span className="benefit-check"><CheckIcon size={16} /></span>
              <span>Subject Performance Tracking</span>
            </div>
          </div>
        </div>
      </div>

      <div className="auth-right">
        <div className="auth-form-wrapper">
          <h1>Create Account</h1>
          <p className="auth-subtitle">Set up your profile to start personalized learning.</p>

          <form onSubmit={handleSubmit} noValidate>
            <div className="form-row">
              <Input
                id="name"
                name="name"
                type="text"
                label="Full Name"
                value={form.name}
                onChange={handleChange}
                placeholder="John Doe"
                error={errors.name}
                required
              />
              <Input
                id="email"
                name="email"
                type="email"
                label="Email Address"
                value={form.email}
                onChange={handleChange}
                placeholder="you@example.com"
                error={errors.email}
                required
              />
            </div>

            <div className="form-row">
              <Input
                id="rollNumber"
                name="rollNumber"
                type="text"
                label="Roll Number"
                value={form.rollNumber}
                onChange={handleChange}
                placeholder="CS202401"
                error={errors.rollNumber}
                required
              />
              <div className="form-group">
                <label htmlFor="branch">
                  Branch <span style={{ color: 'var(--status-danger)' }}>*</span>
                </label>
                <select
                  id="branch"
                  name="branch"
                  value={form.branch}
                  onChange={handleChange}
                  className="form-select"
                >
                  <option value="">Select branch</option>
                  <option value="Computer Science">Computer Science</option>
                  <option value="Information Technology">Information Technology</option>
                  <option value="Electronics">Electronics</option>
                  <option value="Mechanical">Mechanical</option>
                  <option value="Civil">Civil</option>
                </select>
                {errors.branch && <span className="form-error">{errors.branch}</span>}
              </div>
            </div>

            <div className="form-row">
              <Input
                id="password"
                name="password"
                type="password"
                label="Password"
                value={form.password}
                onChange={handleChange}
                placeholder="Min. 6 chars"
                error={errors.password}
                required
              />
              <Input
                id="confirmPassword"
                name="confirmPassword"
                type="password"
                label="Confirm Password"
                value={form.confirmPassword}
                onChange={handleChange}
                placeholder="Re-enter"
                error={errors.confirmPassword}
                required
              />
            </div>

            <Button variant="primary" className="btn-full" type="submit">
              <span>Create Account</span>
              <ArrowRightIcon size={16} />
            </Button>
          </form>

          <p className="auth-switch">
            Already have an account? <Link to="/login">Sign in</Link>
          </p>
        </div>
      </div>
    </div>
  );
}
