from sqlalchemy import select
from sqlalchemy.orm import Session
from models import Deaths, engine

with Session(engine) as s:
    res = select(Deaths).where(Deaths.entity == 'Afghanistan')

    for s in s.scalars(res):
        print(f"In Afghanistan number of deaths from malaria in {s.year} is {s.deaths}")

