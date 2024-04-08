import requests

def add_cancer_death(api_url, cancer_death_data):
    response = requests.post(f"{api_url}/cancer-deaths/", json=cancer_death_data)
    print(response.json())

def get_cancer_deaths(api_url):
    response = requests.get(f"{api_url}/cancer-deaths/")
    print(response.json())

def get_cancer_deaths_by_year(api_url, year):
    response = requests.get(f"{api_url}/cancer-deaths/{year}")
    print(response.json())

api_url = "http://127.0.0.1:8000"
cancer_death_data = {
    "entity": "NAN",
    "year": 0,
    "lip_and_oral_cavity_cancer_deaths": 0,
    "other_pharynx_cancer_deaths": 0,
    "esophageal_cancer_deaths": 0,
    "stomach_cancer_deaths": 0,
    "colon_and_rectum_cancer_deaths": 0,
    "liver_cancer_deaths": 0,
    "gallbladder_cancer_deaths": 0,
    "pancreatic_cancer_deaths": 0,
    "larynx_cancer_deaths": 0,
    "tracheal_bronchus_and_lung_cancer_deaths": 0,
    "breast_cancer_deaths": 0,
    "cervical_cancer_deaths": 0,
    "ovarian_cancer_deaths": 0,
    "prostate_cancer_deaths": 0,
    "kidney_cancer_deaths": 0,
    "bladder_cancer_deaths": 0,
    "brain_and_nervous_system_cancer_deaths": 0,
    "non_hodgkin_lymphoma_deaths": 0,
    "leukemia_deaths": 0,
    "other_cancers_deaths": 0
}
# add_cancer_death(api_url, cancer_death_data)
# get_cancer_deaths(api_url)
get_cancer_deaths_by_year(api_url, 2015)
