import requests

s = requests.Session()

server_link = "http://127.0.0.1:8000"
city = input('Введите Лондон или Дели для выборки: ')
if city == 'Лондон':
    city = 'London'
    year = int(input("Выберете год из диапазона: 1700-2015: "))
elif city == 'Дели':
    city = 'Delhi'
    year = int(input("Выберете год из диапазона: 1997-2010: "))
try:
    r = s.get(server_link, params={"city": city, "year": year})
    if r.json():
        print(r.json())
    else:
        print("Выберете верные даты")
except:
    print("Не смогли получить(")
finally:
    pass

