from sqlalchemy import select
from sqlalchemy.orm import Session
from models import engine, Population

with Session(engine) as s:
    res1 = select(Population).order_by(Population.people.desc()).limit(1)
    res2 = select(Population).order_by(Population.people.asc()).limit(1)

    for r in s.scalars(res1):
        print(f"Первая столица по населению на 2018 год - это {r.entity}. В этом городе насчитывается {r.people} жителей.")

    for r in s.scalars(res2):
        print(f"Последняя столица по населению на 2018 год - это {r.entity}. В этом городе насчитывается {r.people} жителей.")
