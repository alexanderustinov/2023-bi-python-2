from sqlalchemy import create_engine, String, select, and_, or_
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
import csv

engine = create_engine("sqlite:///data.db", echo=False)


class Base(DeclarativeBase):
    pass


class GDPPC(Base):
    __tablename__ = 'GDP per capita'

    id: Mapped[int] = mapped_column(primary_key=True)
    city: Mapped[str] = mapped_column(String(10))
    year: Mapped[int] = mapped_column()
    value: Mapped[float] = mapped_column()


GDPPC.metadata.create_all(engine)

# Для того, чтобы создать таблицу:

with Session(engine) as s:
    with open('Real GDP per capita, London and Delhi - OWID.csv', newline='') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
                data = GDPPC(city=row[0],year=row[1],value=row[2])
                s.add(data)
                s.commit()


# Для тестового запроса:
#
# with Session(engine) as s:
#     results_1 = select(GDPPC).where(GDPPC.year==1998)
#     results_2 = select(GDPPC).where(GDPPC.value>37000)
#     results_3 = select(GDPPC).where(and_(GDPPC.city=='London',or_(GDPPC.year==1812, GDPPC.year==1912)))
#
# for r in s.scalars(results_1):
#     print(f"ВВП на душу населения в 1998 в {"Дели"if(r.city == "Delhi")else "Лондоне"} составил {r.value}$")
#
# print("-"*58)
#
# for r in s.scalars(results_2):
#     print(f"ВВП на душу населения в {r.year} в {"Дели"if(r.city == "Delhi")else "Лондоне"} превысил 37000$")
#
# print("-"*58)
#
# for r in s.scalars(results_3):
#     print(f"ВВП на душу населения в {r.year} в Лондоне составил {r.value}$")
