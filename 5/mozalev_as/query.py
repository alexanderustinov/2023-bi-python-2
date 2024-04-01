from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import AntibioticUse

engine = create_engine('sqlite:///antibiotics.db')

Session = sessionmaker(bind=engine)
session = Session()

average_world = session.query(func.avg(AntibioticUse.antibiotic_use)).scalar()

print("Среднее значение потребления антибиотиков по всем странам:", average_world)

session.close()
