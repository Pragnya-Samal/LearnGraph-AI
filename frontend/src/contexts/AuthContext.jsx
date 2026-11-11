import { createContext, useContext, useState } from 'react';

const AuthContext = createContext(null);

// Persistent user store — saved in localStorage so users survive page refresh
// Replace with real backend API calls in Phase 3
function getStoredUsers() {
  try {
    return JSON.parse(localStorage.getItem('lg_users') || '[]');
  } catch {
    return [];
  }
}

function saveStoredUsers(users) {
  localStorage.setItem('lg_users', JSON.stringify(users));
}

export function AuthProvider({ children }) {
  const [user, setUser] = useState(() => {
    try {
      const saved = localStorage.getItem('lg_user');
      return saved ? JSON.parse(saved) : null;
    } catch {
      return null;
    }
  });

  function login(email, password) {
    const users = getStoredUsers();
    const found = users.find(u => u.email === email && u.password === password);
    if (!found) return { success: false, message: 'Invalid email or password.' };
    const { password: _, ...safeUser } = found;
    setUser(safeUser);
    localStorage.setItem('lg_user', JSON.stringify(safeUser));
    return { success: true };
  }

  function register(data) {
    const users = getStoredUsers();
    const exists = users.find(u => u.email === data.email);
    if (exists) return { success: false, message: 'Email already registered.' };
    const newUser = { id: Date.now(), ...data };
    saveStoredUsers([...users, newUser]);
    const { password: _, ...safeUser } = newUser;
    setUser(safeUser);
    localStorage.setItem('lg_user', JSON.stringify(safeUser));
    return { success: true };
  }

  function logout() {
    setUser(null);
    localStorage.removeItem('lg_user');
  }

  return (
    <AuthContext.Provider value={{ user, login, register, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}
