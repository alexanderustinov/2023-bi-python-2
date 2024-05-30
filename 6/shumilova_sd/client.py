import requests
from random import randrange
from schemas import StarsTest


s = requests.Session()
api_base = 'http://127.0.0.1:8000'


def main():
    names = ["Sun", "Alpha Centauri", "Proxima Centauri", "Sirius"]
    stars = []
    for i in names:
        cls = StarsTest(name=i, radius=randrange(1000, 5000), mass=randrange(5000, 100000),
                        distance=randrange(10000, 1000000))
        stars.append(cls)
    for i in stars:
        s.put(f"{api_base}/add", i.model_dump_json())

    for i in names:
        res = s.get(f"{api_base}/stars/{i}/dis")
        print(f"Your star is {i}, and it's distance from the Earth is {res.json()}")


if __name__ == '__main__':
    main()
