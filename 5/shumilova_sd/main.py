import csv
from sqlalchemy.orm import Session
from models import engine, Deaths

Deaths.metadata.create_all(engine)

with Session(engine) as s:
    with open('Malaria deaths - IHME (2016).csv', newline='') as f:
        reader = csv.reader(f)
        next(reader)
        for r in reader:
                data = Deaths(entity=r[0], year=int(r[1]), deaths=float(r[2]))
                s.add(data)
                s.commit()
