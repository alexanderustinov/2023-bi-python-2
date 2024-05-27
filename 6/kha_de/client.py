import requests
from penguin import Penguin

s = requests.Session()
api_base = 'http://127.0.0.1:8000'

def main():
    birds = [
        {'species': 'Emperor Penguin', 'height': 130, 'weight': [35, 40], 'age': 25},
        {'species': 'Rockhopper Penguin', 'height': 60, 'weight': [2, 3], 'age': 25}
    ]

    for p in birds:
        bird = s.put(f"{api_base}/add", json = p)
        print(bird.text)

    r = s.get(api_base)

    penguin_species = 'Emperor Penguin'
    res = requests.get(f"{api_base}/penguins/{penguin_species}")
    print(f"The average height of {penguin_species} is {res.text}.")

if __name__ == '__main__':
    main()