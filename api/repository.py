from db import async_session
from models import Question
from sqlalchemy import desc, insert, select
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
            stmt = select(Question).order_by(desc(Question.created_at))
            res = await session.execute(stmt)
            lastest_question = res.scalar()
            if not lastest_question:
                return {}
            return PostResponse.model_validate(lastest_question, from_attributes=True)

    @classmethod
    async def set_values_from_request(cls, questions: list, answers: list | None) -> None:
        """
        sets questions and answers into question_table
        """
        async with async_session() as session:
            for i in range(0, len(questions)):
                stmt = insert(Question).values(
                    question_body=questions[i], answer_body=answers[i]
                )
                res = await session.execute(stmt)
                await session.commit()

    @classmethod
    async def is_unique_question(cls, questions: list) -> bool:
        async with async_session() as session:
            for question in questions:
                stmt = select(Question).where(Question.question_body == question)
                res = await session.execute(stmt)
                target = res.scalar()
                if target != None:
                    return False
            return True
