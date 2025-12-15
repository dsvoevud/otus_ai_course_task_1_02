"""Repository interfaces for data access."""
from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Question, Answer


class QuestionRepository(ABC):
    """Abstract repository for question data."""
    
    @abstractmethod
    def get_all_questions(self) -> List[Question]:
        """Retrieve all questions."""
        pass


class AnswerRepository(ABC):
    """Abstract repository for answer storage."""
    
    @abstractmethod
    def save_answers(self, answers: List[Answer]) -> None:
        """Save answers."""
        pass
    
    @abstractmethod
    def get_all_answers(self) -> List[Answer]:
        """Retrieve all answers."""
        pass
