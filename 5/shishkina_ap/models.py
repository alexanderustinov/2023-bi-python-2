from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
engine = create_engine('sqlite:///data.db', echo = False)

class Base(DeclarativeBase):
    pass

class GDPPC(Base):
    __tablename__ = 'ocean waste by item'

    id: Mapped[int] = mapped_column(primary_key = True)
    entity: Mapped[str] = mapped_column(String(40), default=None)
    year: Mapped[str] = mapped_column(default=None)

    Deep_Seafloor: Mapped[str] = mapped_column(default=None)
    Nearshore_Seafloor: Mapped[str] = mapped_column(default=None)
    Nearshore_Waters: Mapped[str] = mapped_column(default=None)
    Offshore_Waters: Mapped[str] = mapped_column(default=None)
    River_Waters: Mapped[str] = mapped_column(default=None)
    Riverbed: Mapped[str] = mapped_column(default=None)
    Shoreline: Mapped[str] = mapped_column(default=None)