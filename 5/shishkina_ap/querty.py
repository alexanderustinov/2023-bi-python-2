from sqlalchemy import select, and_, or_
from sqlalchemy.orm import Session
from models import engine, GDPPC

with Session(engine) as s:

    results_1 = select(GDPPC).where(GDPPC.Deep_Seafloor > GDPPC.Nearshore_Seafloor)

    for r in s.scalars(results_1):
        print(f'Коэффициент отходов типа {r.entity} в глубоководье больше, чем в мелководье.')