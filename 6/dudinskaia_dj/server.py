from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import List
import schemas
import uvicorn
import pandas as pd

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def load_data_to_db(db: Session, csv_file_path: str = './cancer_deaths.csv'):
    data = pd.read_csv(csv_file_path)
    db.query(CancerDeath).delete()
    for _, row in data.iterrows():
        db_cancer_death = CancerDeath(
            entity=row['Entity'],
            year=row['Year'],
            lip_and_oral_cavity_cancer_deaths=row['Lip and oral cavity cancer (deaths)'],
            other_pharynx_cancer_deaths=row['Other pharynx cancer (deaths)'],
            esophageal_cancer_deaths=row['Esophageal cancer (deaths)'],
            stomach_cancer_deaths=row['Stomach cancer (deaths)'],
            colon_and_rectum_cancer_deaths=row['Colon and rectum cancer (deaths)'],
            liver_cancer_deaths=row['Liver cancer (deaths)'],
            gallbladder_cancer_deaths=row['Gallbladder cancer (deaths)'],
            pancreatic_cancer_deaths=row['Pancreatic cancer (deaths)'],
            larynx_cancer_deaths=row['Larynx cancer (deaths)'],
            tracheal_bronchus_and_lung_cancer_deaths=row['Tracheal, bronchus, and lung cancer (deaths)'],
            breast_cancer_deaths=row['Breast cancer (deaths)'],
            cervical_cancer_deaths=row['Cervical cancer (deaths)'],
            ovarian_cancer_deaths=row['Ovarian cancer (deaths)'],
            prostate_cancer_deaths=row['Prostate cancer (deaths)'],
            kidney_cancer_deaths=row['Kidney cancer (deaths)'],
            bladder_cancer_deaths=row['Bladder cancer (deaths)'],
            brain_and_nervous_system_cancer_deaths=row['Brain and nervous system cancer (deaths)'],
            non_hodgkin_lymphoma_deaths=row['Non-Hodgkin lymphoma (deaths)'],
            leukemia_deaths=row['Leukemia (deaths)'],
            other_cancers_deaths=row['Other cancers (deaths)']
        )
        db.add(db_cancer_death)
    db.commit()

def init_db():
    db = SessionLocal()
    if db.query(CancerDeath).count() == 0:
        load_data_to_db(db)
    db.close()




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class CancerDeath(Base):
    __tablename__ = "cancer_deaths"
    id = Column(Integer, primary_key=True, index=True)
    entity = Column(String, index=True)
    year = Column(Integer, index=True)
    lip_and_oral_cavity_cancer_deaths = Column(Integer)
    other_pharynx_cancer_deaths = Column(Integer)
    esophageal_cancer_deaths = Column(Integer)
    stomach_cancer_deaths = Column(Integer)
    colon_and_rectum_cancer_deaths = Column(Integer)
    liver_cancer_deaths = Column(Integer)
    gallbladder_cancer_deaths = Column(Integer)
    pancreatic_cancer_deaths = Column(Integer)
    larynx_cancer_deaths = Column(Integer)
    tracheal_bronchus_and_lung_cancer_deaths = Column(Integer)
    breast_cancer_deaths = Column(Integer)
    cervical_cancer_deaths = Column(Integer)
    ovarian_cancer_deaths = Column(Integer)
    prostate_cancer_deaths = Column(Integer)
    kidney_cancer_deaths = Column(Integer)
    bladder_cancer_deaths = Column(Integer)
    brain_and_nervous_system_cancer_deaths = Column(Integer)
    non_hodgkin_lymphoma_deaths = Column(Integer)
    leukemia_deaths = Column(Integer)
    other_cancers_deaths = Column(Integer)

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.post("/cancer-deaths/", response_model=schemas.CancerDeath)
def create_cancer_death(cancer_death: schemas.CancerDeathCreate, db: Session = Depends(get_db)):
    db_cancer_death = CancerDeath(**cancer_death.dict())
    db.add(db_cancer_death)
    db.commit()
    db.refresh(db_cancer_death)
    return db_cancer_death

@app.get("/cancer-deaths/", response_model=List[schemas.CancerDeath])
def read_cancer_deaths(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(CancerDeath).offset(skip).limit(limit).all()

@app.get("/cancer-deaths/{year}", response_model=List[schemas.CancerDeath])
def read_cancer_deaths_by_year(year: int, db: Session = Depends(get_db)):
    return db.query(CancerDeath).filter(CancerDeath.year == year).all()

if __name__ == '__main__':
    init_db()
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
