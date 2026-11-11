import { Outlet } from 'react-router-dom';
import Navbar from '../components/Navbar';
import AIAssistant from '../components/AIAssistant';
import { useAuth } from '../contexts/AuthContext';

export default function Layout() {
  const { user } = useAuth();

  return (
    <div className="app-wrapper">
      <Navbar />
      <main className="main-content">
        <Outlet />
      </main>
      {user && <AIAssistant />}
    </div>
  );
}
