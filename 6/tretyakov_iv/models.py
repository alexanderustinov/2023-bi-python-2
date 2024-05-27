from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_engine("sqlite:///data.db", echo=False)


class Base(DeclarativeBase):
    pass


class GDPPC(Base):
    __tablename__ = 'GDP per capita'

    id: Mapped[int] = mapped_column(primary_key=True)
    city: Mapped[str] = mapped_column(String(10))
    year: Mapped[int] = mapped_column()
    value: Mapped[float] = mapped_column()