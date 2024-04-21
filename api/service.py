from repository import QuizRepository
import requests
from config import settings


class QuizService:
    def __init__(self, repository: QuizRepository) -> None:
        self.repository = repository
        self.__URL = "https://quizapi.io/api/v1/questions"
        self.__API_KEY = settings.API_KEY

    @property
    def url(cls) -> str:
        return cls.__URL

    @property.setter
    def url(cls, url) -> None:
        cls.__URL == url

    @property
    def api_key(cls) -> str:
        return cls.__API_KEY

    @classmethod
    async def create_request(cls, question_num: int) -> dict:

        """ 
        Creates request to API and returns API^s response. 
        """

        payload = {"limit": question_num, "apiKey": cls.api_key}
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/71.0.3578.98 Safari/537.36"
        }
        response = requests.get(cls.url, headers=headers, params=payload)
        return response.json()

    @classmethod
    async def get_questions(cls, response: dict) -> list:
        """ 
        From API^s response, gets only questions 
        """
        questions = []
        for item in response:
            questions.append(item['question'])
        return questions

    @classmethod
    async def get_answers(cls, response: dict) -> list:
        """ 
        From API^s response, gets only answers
        """
        answers = []
        for item in response:
            correct_answer = item['correct_answer']
            answers_keys = item['answers']
            value_of_correct_answer = answers_keys[correct_answer]
            answers.append(value_of_correct_answer)
        return answers
    
    @classmethod
    async def create_question(cls, question_num) -> str | None:
        """ TO DO """
        response = cls.create_request(question_num)
        questions = cls.get_questions(response)
        answers = cls.get_answers(response)
        pass 
