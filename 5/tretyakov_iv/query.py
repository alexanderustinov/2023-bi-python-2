from sqlalchemy import select, and_, or_
from sqlalchemy.orm import Session
from models import engine, GDPPC

with Session(engine) as s:

    results_1 = select(GDPPC).where(GDPPC.year==1998)
    results_2 = select(GDPPC).where(GDPPC.value>37000)
    results_3 = select(GDPPC).where(and_(GDPPC.city=='London',or_(GDPPC.year==1812, GDPPC.year==1912)))

for r in s.scalars(results_1):
    print(f"ВВП на душу населения в 1998 в {"Дели"if(r.city == "Delhi")else "Лондоне"} составил {r.value}$")

print("-"*58)

for r in s.scalars(results_2):
    print(f"ВВП на душу населения в {r.year} в {"Дели"if(r.city == "Delhi")else "Лондоне"} превысил 37000$")

print("-"*58)

for r in s.scalars(results_3):
    print(f"ВВП на душу населения в {r.year} в Лондоне составил {r.value}$")
