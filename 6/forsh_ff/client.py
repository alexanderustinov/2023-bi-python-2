import requests

s = requests.Session()
s.trust_env = False  # spbau proxy

api_base = 'http://127.0.0.1:8000/all_table'

print(s.get(api_base))
