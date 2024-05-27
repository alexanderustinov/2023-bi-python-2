from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_engine("sqlite:///data.db", echo=False)

class Base(DeclarativeBase):
    pass

class Population(Base):
    __tablename__ = 'Capital city population - UN Urbanization Prospects (2018)'

    id: Mapped[int] = mapped_column(primary_key=True)
    entity: Mapped[str] = mapped_column()
    year: Mapped[int] = mapped_column()
    people: Mapped[int] = mapped_column()


Base.metadata.create_all(engine)