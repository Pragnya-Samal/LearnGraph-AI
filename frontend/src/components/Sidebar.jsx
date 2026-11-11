import { Link, useLocation } from 'react-router-dom';
import {
  TargetIcon,
  BookOpenIcon,
  FileTextIcon,
  BarChartIcon,
  CompassIcon,
  UserIcon,
  LogOutIcon,
  BrainIcon,
} from './Icons';

export default function Sidebar({ onLogout }) {
  const location = useLocation();

  const navItems = [
    { path: '/dashboard', label: 'Dashboard', icon: <TargetIcon size={18} /> },
    { path: '/learning', label: 'Learning', icon: <BookOpenIcon size={18} /> },
    { path: '/assessment', label: 'Assessments', icon: <FileTextIcon size={18} /> },
    { path: '/progress', label: 'Progress', icon: <BarChartIcon size={18} /> },
    { path: '/knowledge-map', label: 'Knowledge Map', icon: <CompassIcon size={18} /> },
    { path: '/profile', label: 'Profile', icon: <UserIcon size={18} /> },
  ];

  return (
    <aside className="sidebar">
      <div className="sidebar-header">
        <Link to="/" className="sidebar-logo">
          <div className="navbar-logo-icon-wrapper">
            <BrainIcon size={20} />
          </div>
          <span>LearnGraph AI</span>
        </Link>
      </div>

      <nav className="sidebar-nav">
        {navItems.map((item) => (
          <Link
            key={item.label}
            to={item.path}
            className={`sidebar-link ${location.pathname === item.path ? 'active' : ''}`}
          >
            <span className="sidebar-icon">{item.icon}</span>
            <span>{item.label}</span>
          </Link>
        ))}
      </nav>

      {onLogout && (
        <div className="sidebar-footer">
          <button onClick={onLogout} className="sidebar-link logout">
            <span className="sidebar-icon">
              <LogOutIcon size={18} />
            </span>
            <span>Logout</span>
          </button>
        </div>
      )}
    </aside>
  );
}
