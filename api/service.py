from repository import QuizRepository
import requests
from config import settings
import httpx


class QuizService:
    def __init__(self, repository: QuizRepository) -> None:
        QuizService.repository = repository
        QuizService.URL = "https://quizapi.io/api/v1/questions"
        QuizService.API_KEY = settings.API_KEY

    # @property
    # def url(cls) -> str:
    #     return cls.__URL

    # @url.setter
    # def url(cls, url) -> None:
    #     cls.__URL == url

    # @property
    # def api_key(cls) -> str:
    #     return cls.__API_KEY

    @classmethod
    async def create_request(cls, question_num: int) -> dict:
        """
        Creates request to API and returns API^s response.
        """

        payload = {"limit": question_num, "apiKey": cls.API_KEY}
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/71.0.3578.98 Safari/537.36"
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(cls.URL, headers=headers, params=payload)
        return response.json()

    @classmethod
    async def get_questions(cls, response: dict) -> list:
        """
        From API^s response, gets only questions
        """
        questions = []
        for item in response:

            questions.append(item["question"])
        print(questions)
        return questions

    @classmethod
    async def get_answers(cls, response: dict) -> list | None:
        """
        From API^s response, gets only answers

        response could be None because not every API^s responses storage a right answer
        """
        answers = []
        for item in response:
            correct_answer = item["correct_answer"]
            answers_keys = item["answers"]
            if answers_keys == None or correct_answer == None:
                answers.append(None)
            else:
                value_of_correct_answer = answers_keys[correct_answer]
                answers.append(value_of_correct_answer)
        return answers

    @classmethod
    async def is_unique_question(cls, questions: list) -> bool:
        """
        checks the storage of such a question in the database
        """
        is_unique = await cls.repository.is_unique_question(questions)
        return is_unique

    @classmethod
    async def create_question(cls, question_num: int) -> str | None:
        """returns last question and adding all objects into a database"""

        response = await cls.create_request(question_num)

        questions = await cls.get_questions(response)
        answers = await cls.get_answers(response)

        is_unique = await cls.is_unique_question(questions)
        if not is_unique:
            await cls.create_question(question_num)

        client_response = await cls.repository.get_last_question()

        await cls.repository.set_values_from_request(questions, answers)
        return client_response
