from db import async_session
from models import Question
from sqlalchemy import select
from schemas import PostResponse



class QuizRepository:

    """
    Repository for incapsulate work with Database (QUIZ MODEL)
    """

    @classmethod
    async def get_last_question(cls) -> PostResponse:
        """ 
        gets last question from bd
        """
        async with async_session() as session:
            stmt = (
                select(Question).order_by(Question.created_at.desc)
            )
            res = await session.execute(stmt)
            lastest_question = res.scalar_one()
            return PostResponse.model_validate(lastest_question, from_attributes=True)



    @classmethod
    async def set_values_from_request(cls, questions: list, answers: list) -> None:
        async with async_session() as session: 
            pass
