from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_engine("sqlite:///data.db", echo=False)

class Base(DeclarativeBase):
    pass

class Deaths(Base):
    __tablename__ = 'Malaria_deaths'

    id: Mapped[int] = mapped_column(primary_key=True)
    entity: Mapped[str] = mapped_column()
    year: Mapped[int] = mapped_column()
    deaths: Mapped[float] = mapped_column()


Base.metadata.create_all(engine)