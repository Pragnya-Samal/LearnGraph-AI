# Personalized Learning Platform

A full-stack application featuring an AI-driven learning assessment backend and an interactive React frontend.

---

## 📁 Project Structure

```
Personalized_learning/
├── backend/                  # FastAPI Backend
│   ├── AI/                   # Assessment logic and question bank
│   ├── API/                  # Route handlers & endpoints
│   ├── Tests/                # Backend unit/integration tests
│   ├── main.py               # FastAPI application entrypoint
│   ├── pytest.ini            # Pytest configuration
│   └── requirements.txt      # Python dependencies
│
├── frontend/                 # Vite + React Frontend
│   ├── public/               # Static assets & icons
│   ├── src/                  # Components, pages, contexts, styles
│   ├── package.json          # Frontend dependencies & scripts
│   └── vite.config.js        # Vite configuration
│
├── venv/                     # Python virtual environment
├── requirements.txt          # Root Python dependencies
└── README.md                 # Project documentation
```

---

## 🚀 Getting Started

### 1. Backend Setup & Run

1. Navigate to the `backend/` directory (or workspace root):
   ```bash
   cd backend
   ```

2. Activate the virtual environment (Windows):
   ```powershell
   ..\venv\Scripts\activate
   ```

3. (Optional) Install dependencies if updating:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload --port 8000
   ```
   * Backend API: `http://127.0.0.1:8000`
   * Swagger Docs: `http://127.0.0.1:8000/docs`

---

### 2. Frontend Setup & Run

1. Navigate to the `frontend/` directory:
   ```bash
   cd frontend
   ```

2. Install dependencies (if needed):
   ```bash
   npm install
   ```

3. Start the Vite development server:
   ```bash
   npm run dev
   ```
   * Frontend App: `http://localhost:5173`

---

## 🧪 Testing

To run backend tests:
```powershell
cd backend
..\venv\Scripts\python.exe -m pytest Tests
```
