import requests

s = requests.Session()
api_base = 'http://127.0.0.1:8000'

def main():
    stars = [{"name": "Sun", "distance": "149.6*(10**6)"},
             {"name": "Alpha Centauri", "distance": "41.3*(10**12)"},
             {"name": "Proxima Centauri", "distance": "39.9*(10**12)"},
             {"name": "Sirius", "distance": "81*(10**12)"}]

    for _ in stars:
        a = s.put(f"{api_base}/add", json=_)
        print(a.text)

    #r = s.get(api_base)

    star_name = "Sun"
    res = requests.get(f"{api_base}/{star_name}")
    print(f"Your star is {star_name}, and it's distance from the Earth is {res.text}")

    star_name_ = "Sirius"
    res_ = requests.get(f"{api_base}/{star_name_}/dis")
    print(f"Your star is {star_name_}, and it's distance from the Earth is {res_.text}")

if __name__ == '__main__':
    main()
