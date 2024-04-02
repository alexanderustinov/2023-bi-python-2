import csv
import sqlalchemy
from sqlalchemy import Column, Integer, String, create_engine, select
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

class AviationAccidents(Base):
    __tablename__ = 'accidents aviation'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Entity = Column(String)
    Year = Column(Integer)
    En_route_accidents = Column(Integer)
    En_route_casualties = Column(Integer)
    Take_off_accidents = Column(Integer)
    Take_off_casualties = Column(Integer)
    Initial_climb_accidents = Column(Integer)
    Initial_climb_casualties = Column(Integer)
    Approach_accidents = Column(Integer)
    Approach_fatalities = Column(Integer)
    Landing_accidents = Column(Integer)
    Landing_fatalities = Column(Integer)

engine = sqlalchemy.create_engine('sqlite:///idk.db', echo=False)

with open('Aviation accidents and fatalities by flight phase (ASN, 2019).csv', encoding='utf-8', mode='r') as file:
    data = csv.reader(file, delimiter=',')
    data.__next__()

    with Session(engine) as sess:
        for i in data:
            new = AviationAccidents(
                Entity=i[0],
                Year=int(i[1]),
                En_route_accidents=int(i[2]),
                En_route_casualties=int(i[3]),
                Take_off_accidents=int(i[4]),
                Take_off_casualties=int(i[5]),
                Initial_climb_accidents=int(i[6]),
                Initial_climb_casualties=int(i[7]),
                Approach_accidents=int(i[8]),
                Approach_fatalities=int(i[9]),
                Landing_accidents=int(i[10]),
                Landing_fatalities=int(i[11])
            )
            sess.add(new)
        sess.commit()

Base.metadata.create_all(engine)

#запрос выдаёт количество смертей при посадке (2 число) за год (1 чилсо)
with Session(engine) as sess2:
    q_1 = sess2.execute(
        select(AviationAccidents.Year, AviationAccidents.Landing_fatalities)
        .where(AviationAccidents.Entity == 'World') # -_-
        .order_by(AviationAccidents.Year.desc()))
    print(q_1.all())

