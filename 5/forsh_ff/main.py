import csv
from sqlalchemy.orm import Session
from models import Rating, engine


with open('World Happiness Report (2022).csv', encoding='utf-8', mode='r') as file:
    data = csv.reader(file, delimiter=',')
    data.__next__()


    with Session(engine) as s:
        for i in data:
            new = Rating(country=i[0], year=i[1], rating=float(i[2]))
            s.add(new)
            s.commit()
