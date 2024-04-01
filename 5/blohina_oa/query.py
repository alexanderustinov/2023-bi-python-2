from sqlalchemy import select, and_, or_
from sqlalchemy.orm import Session
from models import engine, GDPPC

with Session(engine) as s:
    results_1 = select(GDPPC).where(GDPPC.nicotine > 2)
    results_2 = select(GDPPC).where(GDPPC.alcohol > 5)
    results_3 = select(GDPPC).where(GDPPC.drug > 4)

    for r in s.scalars(results_1):
        print(f'Риск употребления никотина у лиц с {r.entity} в {r.nicotine} раза больше, чем у лиц, которые не имеют {r.entity}.')
    print()
    for r in s.scalars(results_2):
        print(f'Риск употребления алкоголя у лиц с {r.entity} в {r.alcohol} раза больше, чем у лиц, которые не имеют {r.entity}.')
    print()
    for r in s.scalars(results_3):
        print(f'Риск употребления наркотиков у лиц с {r.entity} в {r.drug} раза больше, чем у лиц, которые не имеют {r.entity}.')
    print()
