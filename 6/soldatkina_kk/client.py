import requests

s = requests.Session()

server_link = "http://127.0.0.1:8000"
entity = input('Введите Японию или Монтсеррат для выборки: ')
if entity == 'Япония':
    entity = 'Japan'
elif entity == 'Монтсеррат':
    entity = 'Montserrat'
try:
    r = s.get(server_link, params={"entity": entity})
    if r.json():
        print(r.json())
    else:
        print("Попробуйте сделать правильно.")
except:
    print("Результата нет.")
finally:
    pass