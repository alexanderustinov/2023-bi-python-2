from sqlalchemy.orm import Session
import csv
from models import engine, GDPPC

GDPPC.metadata.create_all(engine)


with Session(engine) as s:
    with open('Real GDP per capita, London and Delhi - OWID.csv', newline='') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
                data = GDPPC(city=row[0],year=row[1],value=row[2])
                s.add(data)
                s.commit()
