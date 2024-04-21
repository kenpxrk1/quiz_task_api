import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import text


class Base(DeclarativeBase):
    pass


class Question(Base):
    __tablename__ = "questions"

    question_id: Mapped[int] = mapped_column(primary_key=True)
    question_body: Mapped[str]
    response_body: Mapped[str]
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))

    