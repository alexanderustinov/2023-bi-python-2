from sqlalchemy.orm import Session
import csv
from models import engine, GDPPC

GDPPC.metadata.create_all(engine)

with Session(engine) as s:
    with open('Mental health as risk factor for substance use.csv', newline = '') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
                data = GDPPC(entity = row[0], year = row[1], nicotine = row[2], alcohol = row[3], drug = row[4])
                s.add(data)
                s.commit()
