"""Infrastructure implementations of repositories."""
import json
from pathlib import Path
from typing import List
from src.domain.models import Question, Answer
from src.domain.repositories import QuestionRepository, AnswerRepository


class JsonQuestionRepository(QuestionRepository):
    """Repository that reads questions from a JSON file."""
    
    def __init__(self, config_path: str = "config/questions.json"):
        self._config_path = Path(config_path)
    
    def get_all_questions(self) -> List[Question]:
        """Load questions from JSON file."""
        if not self._config_path.exists():
            raise FileNotFoundError(f"Questions file not found: {self._config_path}")
        
        with open(self._config_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        return [Question(**q) for q in data.get("questions", [])]


class InMemoryAnswerRepository(AnswerRepository):
    """Repository that stores answers in memory."""
    
    def __init__(self):
        self._answers: List[Answer] = []
    
    def save_answers(self, answers: List[Answer]) -> None:
        """Store answers in memory."""
        self._answers.extend(answers)
    
    def get_all_answers(self) -> List[Answer]:
        """Retrieve all stored answers."""
        return self._answers.copy()