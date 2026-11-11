-- ============================================================================
-- SQL Database Schema for Personalized Learning System
-- Based on the Entity-Relationship (ER) Diagram
-- ============================================================================

PRAGMA foreign_keys = ON;

-- ----------------------------------------------------------------------------
-- 1. SUBJECT Table
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS subject (
    subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    code TEXT NOT NULL UNIQUE,
    description TEXT
);

-- ----------------------------------------------------------------------------
-- 2. TOPIC Table (Contained within Subject)
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS topic (
    topic_id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    difficulty TEXT DEFAULT 'Intermediate', -- Beginner, Intermediate, Advanced
    display_order INTEGER DEFAULT 1,
    FOREIGN KEY (subject_id) REFERENCES subject(subject_id) ON DELETE CASCADE,
    UNIQUE(subject_id, name)
);

-- ----------------------------------------------------------------------------
-- 3. STUDENT Table
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS student (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joined_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ----------------------------------------------------------------------------
-- 4. STUDY_MATERIAL Table (Only YouTube links and Websites)
-- Restricted to types: 'youtube' and 'website' (No PDFs or raw video files)
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS study_material (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    type TEXT NOT NULL CHECK(type IN ('youtube', 'website')),
    url TEXT NOT NULL,
    description TEXT,
    FOREIGN KEY (topic_id) REFERENCES topic(topic_id) ON DELETE CASCADE
);

-- ----------------------------------------------------------------------------
-- 5. QUIZ Table (Tests Topic)
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS quiz (
    quiz_id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    difficulty_marks INTEGER DEFAULT 30, -- 30 questions/marks
    FOREIGN KEY (topic_id) REFERENCES topic(topic_id) ON DELETE CASCADE
);

-- ----------------------------------------------------------------------------
-- 6. LEARNER_TOPIC_PROGRESS Table
-- Tracks student topic mastery and completion status
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS learner_topic_progress (
    progress_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    topic_id INTEGER NOT NULL,
    score REAL DEFAULT 0.0,
    status TEXT DEFAULT 'Not Started', -- Not Started, In Progress, Needs Review, Mastered
    last_reviewed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    mastered_on TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE,
    FOREIGN KEY (topic_id) REFERENCES topic(topic_id) ON DELETE CASCADE,
    UNIQUE(student_id, topic_id)
);

-- ----------------------------------------------------------------------------
-- 7. REVISION_RECORD Table
-- Spaced repetition records for quizzes and topic reviews
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS revision_record (
    revision_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    topic_id INTEGER NOT NULL,
    quiz_id INTEGER,
    progress_id INTEGER,
    score REAL NOT NULL,
    current_interval_days INTEGER DEFAULT 1,
    last_reviewed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    next_review TIMESTAMP NOT NULL,
    FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE,
    FOREIGN KEY (topic_id) REFERENCES topic(topic_id) ON DELETE CASCADE,
    FOREIGN KEY (quiz_id) REFERENCES quiz(quiz_id) ON DELETE SET NULL,
    FOREIGN KEY (progress_id) REFERENCES learner_topic_progress(progress_id) ON DELETE SET NULL
);

-- ----------------------------------------------------------------------------
-- Indexes for Performance Tuning
-- ----------------------------------------------------------------------------
CREATE INDEX IF NOT EXISTS idx_topic_subject ON topic(subject_id);
CREATE INDEX IF NOT EXISTS idx_material_topic ON study_material(topic_id);
CREATE INDEX IF NOT EXISTS idx_material_type ON study_material(type);
CREATE INDEX IF NOT EXISTS idx_quiz_topic ON quiz(topic_id);
CREATE INDEX IF NOT EXISTS idx_progress_student ON learner_topic_progress(student_id);
CREATE INDEX IF NOT EXISTS idx_progress_topic ON learner_topic_progress(topic_id);
CREATE INDEX IF NOT EXISTS idx_revision_student ON revision_record(student_id);
CREATE INDEX IF NOT EXISTS idx_revision_next ON revision_record(next_review);
