import random
import requests
from classes import B

s = requests.Session()

api_base = 'http://127.0.0.1:8000'

for _ in range(5):
    n=random.choice(["красный", "желтый", "синий", "зеленый", "фиолетовый", "белый", "черный", "оранжевый"])
    b = random.choice(["крошечный","оч маленький","маленький","средний","небольшой","большой","огромный"])
    c = B(name="Фруктик",size=b, color=n, taste="все вкусно")
    s.put(f"{api_base}/add", json=c.model_dump())
print("Неизвестные фрукты и их характеристики")
r = s.get(api_base)
for c_json in r.json():
    c = B.model_validate(c_json)
    print(c)

res = requests.get(f"{api_base}/f/?color=синий")
fil = res.json()
print(fil)
