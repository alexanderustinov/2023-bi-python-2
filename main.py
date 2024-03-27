import pandas
from sqlalchemy import *
from sqlalchemy.orm import *

engine = create_engine("sqlite:///data.db", echo=False)
Base = declarative_base()

class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    country = Column(String)
    year = Column(Float)
    hunger_index_change = Column(Float)

    def __repr__(self):
        return f"Country(country={self.country}, year={self.year}, hunger_index_change={self.hunger_index_change})"

Base.metadata.create_all(engine)
data = pandas.read_csv('Index.csv')
with Session(engine) as s:
    for index, i in data.iterrows():
        c = Country(country=i['Entity'], year=i['Year'], hunger_index_change=i['Change in Global Hunger Index, 1992-2017 (Global Hunger Index 2017)'])
        s.add(c)
    s.commit()

with Session(engine) as s:
    res = s.query(Country).all()
    for res in res:
        print(res.country, res.year, res.hunger_index_change)