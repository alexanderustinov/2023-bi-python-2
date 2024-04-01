import csv
import os
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
current_dir = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
csv_file_path = os.path.join(current_dir, 'atnibioticsEC.csv')

class AntibioticUse(Base):
    __tablename__ = 'antibiotic_use'

    id = Column(Integer, primary_key=True)
    entity = Column(String)
    year = Column(Integer)
    antibiotic_use = Column(Float)


engine = create_engine('sqlite:///antibiotics.db')


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        antibiotic_use = AntibioticUse(entity=row['Entity'], year=int(row['Year']), antibiotic_use=float(row['Antibiotic use in livestock']))
        session.add(antibiotic_use)


session.commit()


session.close()
