from pydantic import BaseModel
from typing import Optional

class CancerDeathBase(BaseModel):
    entity: str
    year: int
    lip_and_oral_cavity_cancer_deaths: Optional[int] = None
    other_pharynx_cancer_deaths: Optional[int] = None
    esophageal_cancer_deaths: Optional[int] = None
    stomach_cancer_deaths: Optional[int] = None
    colon_and_rectum_cancer_deaths: Optional[int] = None
    liver_cancer_deaths: Optional[int] = None
    gallbladder_cancer_deaths: Optional[int] = None
    pancreatic_cancer_deaths: Optional[int] = None
    larynx_cancer_deaths: Optional[int] = None
    tracheal_bronchus_and_lung_cancer_deaths: Optional[int] = None
    breast_cancer_deaths: Optional[int] = None
    cervical_cancer_deaths: Optional[int] = None
    ovarian_cancer_deaths: Optional[int] = None
    prostate_cancer_deaths: Optional[int] = None
    kidney_cancer_deaths: Optional[int] = None
    bladder_cancer_deaths: Optional[int] = None
    brain_and_nervous_system_cancer_deaths: Optional[int] = None
    non_hodgkin_lymphoma_deaths: Optional[int] = None
    leukemia_deaths: Optional[int] = None
    other_cancers_deaths: Optional[int] = None

class CancerDeathCreate(CancerDeathBase):
    pass

class CancerDeath(CancerDeathBase):
    id: int

    class Config:
        orm_mode = True
