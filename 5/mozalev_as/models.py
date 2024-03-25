from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class AntibioticUse(Base):
    __tablename__ = 'antibiotic_use'

    id = Column(Integer, primary_key=True)
    entity = Column(String)
    year = Column(Integer)
    antibiotic_use = Column(Float)
