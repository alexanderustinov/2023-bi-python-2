import csv
from sqlalchemy.orm import Session
from models import Population, engine


with open('Capital city population - UN Urbanization Prospects (2018).csv', encoding='utf-8', mode='r') as file:
    data = csv.reader(file, delimiter=',')
    data.__next__()


    with Session(engine) as s:
        for i in data:
            new = Population(entity=i[0], year=int(i[1]), people=int(i[2]))
            s.add(new)
        s.commit()