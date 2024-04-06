from sqlalchemy.orm import Session
import csv
from models import engine, GDPPC

GDPPC.metadata.create_all(engine)

with Session(engine) as s:
    with open('Mental health as risk factor for substance use.csv', newline='') as f:
        reader = csv.reader(f)
        next(reader)
        check_id_limit = 19
        for row in reader:
            if check_id_limit == 0:
                exit()
                data = GDPPC(id=check_id_limit, entity=row[0], year=row[1], nicotine=row[2], alcohol=row[3], drug=row[4])
                s.add(data)
                s.commit()
            check_id_limit -= 1
