import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class CancerDeaths(Base):
    __tablename__ = 'Cancer_deaths_grouped_OWID'
    id = Column(Integer, primary_key=True)
    entity = Column(String)
    year = Column(Integer)
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

engine = create_engine('sqlite:///cancer_deaths.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def load_data_to_db(data_path):
    data = pd.read_csv(data_path)
    for _, row in data.iterrows():
        record = CancerDeaths(
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
        session.add(record)
    session.commit()

load_data_to_db('cancer_deaths_data.csv')

# Получение данных о смертях от рака шейки матки в 2016 году
def test_query():
    result = session.query(CancerDeaths).filter_by(year=2016).all()
    for item in result:
        print(f"{item.entity}: {item.cervical_cancer_deaths} deaths")

test_query()
