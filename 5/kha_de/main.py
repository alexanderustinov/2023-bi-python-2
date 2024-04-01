from sqlalchemy.orm import Session
import csv
from models import engine, Book

Book.metadata.create_all(engine)

with Session(engine) as s:
    with open('Basic reading and maths skills.csv', newline='') as f:
        r = csv.reader(f)
        next(r)
        for i in r:
            d = Book(country = i[0], year = i[1], percent = i[2])
            s.add(d)
        s.commit()