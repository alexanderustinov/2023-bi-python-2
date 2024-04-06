from sqlalchemy import create_engine, String, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
engine = create_engine('sqlite:///data.db', echo=False)

class Base(DeclarativeBase):
    pass

class GDPPC(Base):
    __tablename__ = 'Mental_health_as_risk_factor_for_substance_use'

    id: Mapped[int] = mapped_column(primary_key=True)
    entity: Mapped[str] = mapped_column(String(40))
    year: Mapped[int] = mapped_column()
    nicotine: Mapped[float] = mapped_column()
    alcohol: Mapped[float] = mapped_column()
    drug: Mapped[float] = mapped_column()
    __table_args__ = (
        CheckConstraint('id <= 19', name='check_id_limit'),
    )
