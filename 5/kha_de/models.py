from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_engine("sqlite:///data.db", echo = False)

class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = 'Reading and maths skills'

    id: Mapped[int] = mapped_column(primary_key = True)
    country: Mapped[str] = mapped_column(String(10))
    year: Mapped[int] = mapped_column()
    percent: Mapped[float] = mapped_column()