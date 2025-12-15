import { Question, AnswerSubmission, SubmissionResponse } from '../types/api';

const API_BASE_URL = '/api/v1';

class ApiService {
  private async fetchApi<T>(endpoint: string, options?: RequestInit): Promise<T> {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      headers: {
        'Content-Type': 'application/json',
        ...options?.headers,
      },
      ...options,
    });

    if (!response.ok) {
      const error = await response.json().catch(() => ({ detail: 'An error occurred' }));
      throw new Error(error.detail || `HTTP error! status: ${response.status}`);
    }

    return response.json();
  }

  async getQuestions(): Promise<Question[]> {
    return this.fetchApi<Question[]>('/questions');
  }

  async submitAnswers(submission: AnswerSubmission): Promise<SubmissionResponse> {
    return this.fetchApi<SubmissionResponse>('/answers', {
      method: 'POST',
      body: JSON.stringify(submission),
    });
  }
}

export const apiService = new ApiService();
