// Centralized API Client Service for Backend Interaction

const API_BASE_URL =
  import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000';


/**
 * Check backend health status
 */
export async function checkBackendHealth() {
  try {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 3000);

    const response = await fetch(`${API_BASE_URL}/`, {
      signal: controller.signal,
    });
    clearTimeout(timeoutId);
    return response.ok;
  } catch {
    return false;
  }
}


/**
 * Generate a Subject-Level Assessment
 * Generates randomized, unique questions testing across the hierarchical topics in the subject.
 */
export async function generateSubjectAssessment(subject, count = 10) {
  try {
    const cleanSubject = encodeURIComponent((subject || '').trim());
    const response = await fetch(`${API_BASE_URL}/assessment/generate/subject/${cleanSubject}?count=${count}`);

    if (!response.ok) {
      throw new Error(`Failed to generate subject assessment (${response.status})`);
    }

    const data = await response.json();
    return {
      success: true,
      data,
    };
  } catch (error) {
    console.error('generateSubjectAssessment Error:', error);
    return {
      success: false,
      error: error.message || 'Unable to generate subject assessment.',
    };
  }
}


/**
 * Generate a Topic-Level Spaced Repetition Quiz
 * Generates unique, randomized questions for a specific learned topic.
 */
export async function generateTopicQuiz(subject, topic, count = 5) {
  try {
    const cleanSubject = encodeURIComponent((subject || '').trim());
    const cleanTopic = encodeURIComponent((topic || '').trim());
    const response = await fetch(`${API_BASE_URL}/assessment/generate/${cleanSubject}/${cleanTopic}?count=${count}`);

    if (!response.ok) {
      throw new Error(`Failed to generate topic quiz (${response.status})`);
    }

    const data = await response.json();
    return {
      success: true,
      data,
    };
  } catch (error) {
    console.error('generateTopicQuiz Error:', error);
    return {
      success: false,
      error: error.message || 'Unable to generate topic quiz.',
    };
  }
}


/**
 * Compatibility wrapper for generateAssessment
 */
export async function generateAssessment(subject, topic) {
  if (!topic || topic === 'Subject Assessment' || topic === 'all') {
    return generateSubjectAssessment(subject);
  }
  return generateTopicQuiz(subject, topic);
}


/**
 * Submit AI-generated assessment or Spaced Repetition Quiz
 */
export async function submitGeneratedAssessment(assessmentId, answers) {
  try {
    const response = await fetch(`${API_BASE_URL}/assessment/submit`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        assessment_id: assessmentId,
        answers,
      }),
    });

    if (!response.ok) {
      throw new Error(`Failed to submit assessment (${response.status})`);
    }

    const data = await response.json();
    return {
      success: true,
      data,
    };
  } catch (error) {
    console.error('Submit Assessment Error:', error);
    return {
      success: false,
      error: error.message || 'Unable to submit assessment.',
    };
  }
}


/**
 * Fetch topic study materials from database (YouTube video links & reference websites only)
 */
export async function fetchStudyMaterials(subject, topic) {
  try {
    const cleanSubject = encodeURIComponent((subject || '').trim());
    const cleanTopic = encodeURIComponent((topic || '').trim());

    const response = await fetch(`${API_BASE_URL}/study-materials/${cleanSubject}/${cleanTopic}`);

    if (!response.ok) {
      throw new Error(`Failed to load study materials (${response.status})`);
    }

    const data = await response.json();
    return {
      success: true,
      materials: data.materials || [],
      count: data.count || 0,
    };
  } catch (error) {
    return {
      success: false,
      materials: [],
      error: error.message || 'Unable to load study materials.',
    };
  }
}


/**
 * Fetch all subjects with hierarchical topics from database
 */
export async function fetchDatabaseSubjects() {
  try {
    const response = await fetch(`${API_BASE_URL}/subjects/database`);
    if (!response.ok) {
      throw new Error(`Failed to fetch database subjects (${response.status})`);
    }
    const data = await response.json();
    return {
      success: true,
      subjects: data || [],
    };
  } catch (error) {
    return {
      success: false,
      subjects: [],
      error: error.message,
    };
  }
}


/**
 * Fetch next topic in subject hierarchy
 */
export async function fetchNextTopic(subject, topic) {
  try {
    const cleanSubject = encodeURIComponent((subject || '').trim());
    const cleanTopic = encodeURIComponent((topic || '').trim());
    const response = await fetch(`${API_BASE_URL}/subjects/${cleanSubject}/next-topic/${cleanTopic}`);
    if (!response.ok) {
      throw new Error(`Failed to fetch next topic (${response.status})`);
    }
    const data = await response.json();
    return {
      success: true,
      nextTopic: data.next_topic,
    };
  } catch (error) {
    return {
      success: false,
      nextTopic: null,
      error: error.message,
    };
  }
}


/**
 * Fetch learner topic progress and spaced repetition reviews from SQL database
 */
export async function fetchStudentProgress(studentId = 1) {
  try {
    const response = await fetch(`${API_BASE_URL}/student/${studentId}/progress`);
    if (!response.ok) {
      throw new Error(`Failed to load student progress (${response.status})`);
    }
    const data = await response.json();
    return {
      success: true,
      progress: data.progress || [],
      upcomingRevisions: data.upcoming_revisions || [],
    };
  } catch (error) {
    return {
      success: false,
      progress: [],
      upcomingRevisions: [],
      error: error.message || 'Unable to load student progress.',
    };
  }
}


/**
 * Fetch old/static assessment questions (Kept for backwards compatibility)
 */
export async function fetchAssessmentQuestions(subject, topic) {
  return generateTopicQuiz(subject, topic);
}

/**
 * Submit old/static assessment answers (Kept for backwards compatibility)
 */
export async function submitAssessmentAnswers(subject, topic, answers, attemptNumber = 1) {
  try {
    const response = await fetch(`${API_BASE_URL}/assessment`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        subject,
        topic,
        answers,
        attempt_number: attemptNumber,
      }),
    });
    const data = await response.json();
    return { success: response.ok, data };
  } catch (error) {
    return { success: false, error: error.message };
  }
}
