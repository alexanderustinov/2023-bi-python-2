from classes import name_and_element
import requests

s = requests.Session()
api_base = "http://127.0.0.1:8000"

def main():
    characters = [{"name": "Furina", "element": "Hydro"},
                  {"name": "Gaming", "element": "Pyro"},
                  {"name": "Rosaria", "element": "Cryo"},
                  {"name": "Razor", "element": "Electro"},
                  {"name": "Navia", "element": "Geo"},
                  {"name": "Kazuha", "element": "Anemo"},
                  {"name": "Baizhu", "element": "Dendro"}]

    for i in characters:
        nah = s.put(f"{api_base}/add", json=i)
        print(nah.text)

    r = s.get(api_base)

    character_name = "Kazuha"
    res = requests.get(f"{api_base}/{character_name}")
    print(f"Name is {character_name}, element is {res.text}")

    character_name_2 = "Rosaria"
    res2 = requests.get(f"{api_base}/{character_name}/archon")
    print(f"Name is {character_name_2}, archon of my element is {res2.text}")

if __name__ == '__main__':
    main()



