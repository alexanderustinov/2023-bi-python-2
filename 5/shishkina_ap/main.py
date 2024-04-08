from sqlalchemy.orm import Session
import csv
from models import engine, GDPPC

GDPPC.metadata.create_all(engine)

with Session(engine) as s:
    with open('ocean_waste_by_item.csv') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        for row in reader:
            data = GDPPC(entity = row[0], year = row[1], Deep_Seafloor = row[2], \
                        Nearshore_Seafloor = row[3], Nearshore_Waters = row[4], \
                        Offshore_Waters=row[5], River_Waters=row[6], Riverbed=row[7],\
                        Shoreline=row[8])
            s.add(data)
        s.commit()