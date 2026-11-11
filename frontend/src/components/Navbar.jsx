import { useState } from 'react';
import { Link, useNavigate, useLocation } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import { useTheme } from '../contexts/ThemeContext';
import {
  SunIcon,
  MoonIcon,
  BellIcon,
  MenuIcon,
  CloseIcon,
  BrainIcon,
  BookOpenIcon,
  BarChartIcon,
  CompassIcon,
  UserIcon,
  LogOutIcon,
  TargetIcon,
} from './Icons';

export default function Navbar() {
  const { user, logout } = useAuth();
  const { isDark, toggleTheme } = useTheme();
  const navigate = useNavigate();
  const location = useLocation();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [profileDropdownOpen, setProfileDropdownOpen] = useState(false);

  function handleLogout() {
    logout();
    navigate('/login');
    setMobileMenuOpen(false);
    setProfileDropdownOpen(false);
  }

  const isActive = (path) => location.pathname === path;

  return (
    <header className="navbar">
      <div className="navbar-container">
        {/* Logo */}
        <Link to="/" className="navbar-logo" onClick={() => setMobileMenuOpen(false)}>
          <div className="navbar-logo-icon-wrapper">
            <BrainIcon size={20} />
          </div>
          <span className="navbar-brand-text">LearnGraph AI</span>
        </Link>

        {/* Desktop Navigation Links */}
        {user && (
          <nav className="navbar-nav-desktop" aria-label="Main Navigation">
            <Link to="/dashboard" className={`nav-link ${isActive('/dashboard') ? 'active' : ''}`}>
              <TargetIcon size={16} />
              <span>Dashboard</span>
            </Link>
            <Link to="/learning" className={`nav-link ${isActive('/learning') ? 'active' : ''}`}>
              <BookOpenIcon size={16} />
              <span>Learning</span>
            </Link>
            <Link to="/assessment" className={`nav-link ${isActive('/assessment') ? 'active' : ''}`}>
              <TargetIcon size={16} />
              <span>Assessments</span>
            </Link>
            <Link to="/progress" className={`nav-link ${isActive('/progress') ? 'active' : ''}`}>
              <BarChartIcon size={16} />
              <span>Progress</span>
            </Link>
            <Link to="/knowledge-map" className={`nav-link ${isActive('/knowledge-map') ? 'active' : ''}`}>
              <CompassIcon size={16} />
              <span>Knowledge Map</span>
            </Link>
          </nav>
        )}

        {/* Right Section */}
        <div className="navbar-right">
          {/* Theme Toggle Button */}
          <button
            className="navbar-icon-btn"
            onClick={toggleTheme}
            aria-label="Toggle theme"
            title={isDark ? 'Switch to Light Mode' : 'Switch to Dark Mode'}
          >
            {isDark ? <SunIcon size={18} /> : <MoonIcon size={18} />}
          </button>

          {user ? (
            <>
              <button className="navbar-icon-btn" aria-label="Notifications" title="Notifications">
                <BellIcon size={18} />
              </button>

              <div className="navbar-profile-dropdown">
                <button
                  className="navbar-profile-button"
                  onClick={() => setProfileDropdownOpen(!profileDropdownOpen)}
                  aria-label="User menu"
                >
                  <div className="navbar-avatar">
                    {user.name?.[0]?.toUpperCase() || 'U'}
                  </div>
                  <span className="navbar-user-name">{user.name?.split(' ')[0]}</span>
                </button>

                {profileDropdownOpen && (
                  <div className="navbar-dropdown-menu">
                    <Link
                      to="/profile"
                      className="dropdown-item"
                      onClick={() => setProfileDropdownOpen(false)}
                    >
                      <UserIcon size={16} />
                      <span>Profile</span>
                    </Link>
                    <hr className="dropdown-divider" />
                    <button onClick={handleLogout} className="dropdown-item logout">
                      <LogOutIcon size={16} />
                      <span>Logout</span>
                    </button>
                  </div>
                )}
              </div>
            </>
          ) : (
            <div className="navbar-auth-links">
              <Link to="/login" className="btn btn-ghost btn-sm">
                Login
              </Link>
              <Link to="/register" className="btn btn-primary btn-sm">
                Get Started
              </Link>
            </div>
          )}

          {/* Mobile Menu Toggle Button */}
          <button
            className="navbar-icon-btn navbar-mobile-toggle"
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            aria-label="Toggle mobile menu"
          >
            {mobileMenuOpen ? <CloseIcon size={20} /> : <MenuIcon size={20} />}
          </button>
        </div>
      </div>

      {/* Mobile Drawer */}
      {mobileMenuOpen && user && (
        <div className="navbar-mobile-menu">
          <Link
            to="/dashboard"
            className={`mobile-nav-link ${isActive('/dashboard') ? 'active' : ''}`}
            onClick={() => setMobileMenuOpen(false)}
          >
            <TargetIcon size={18} />
            <span>Dashboard</span>
          </Link>
          <Link
            to="/learning"
            className={`mobile-nav-link ${isActive('/learning') ? 'active' : ''}`}
            onClick={() => setMobileMenuOpen(false)}
          >
            <BookOpenIcon size={18} />
            <span>Learning</span>
          </Link>
          <Link
            to="/assessment"
            className={`mobile-nav-link ${isActive('/assessment') ? 'active' : ''}`}
            onClick={() => setMobileMenuOpen(false)}
          >
            <TargetIcon size={18} />
            <span>Assessments</span>
          </Link>
          <Link
            to="/progress"
            className={`mobile-nav-link ${isActive('/progress') ? 'active' : ''}`}
            onClick={() => setMobileMenuOpen(false)}
          >
            <BarChartIcon size={18} />
            <span>Progress</span>
          </Link>
          <Link
            to="/knowledge-map"
            className={`mobile-nav-link ${isActive('/knowledge-map') ? 'active' : ''}`}
            onClick={() => setMobileMenuOpen(false)}
          >
            <CompassIcon size={18} />
            <span>Knowledge Map</span>
          </Link>
          <hr className="dropdown-divider" />
          <Link
            to="/profile"
            className="mobile-nav-link"
            onClick={() => setMobileMenuOpen(false)}
          >
            <UserIcon size={18} />
            <span>Profile</span>
          </Link>
          <button onClick={handleLogout} className="mobile-nav-link logout">
            <LogOutIcon size={18} />
            <span>Logout</span>
          </button>
        </div>
      )}
    </header>
  );
}
