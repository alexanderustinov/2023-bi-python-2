import requests
import argparse


s = requests.Session()
s.trust_env = False

api_base = 'http://127.0.0.1:8000/'

parser = argparse.ArgumentParser(prog='client')
parser.add_argument('req', action='store', help='arg for API request (for example: all_table)'
                    ' all requests: all_table, avg, country_info, create_rating')
parser.add_argument('args_country', action='store', nargs='?', default='', help='country')
parser.add_argument('args_year', action='store', nargs='?', default='', help='year')

args = parser.parse_args()
print('/'.join([args.req, args.args_country, args.args_year]))
request = s.get(api_base + '/'.join([args.req, args.args_country, args.args_year]))
print(request.json())
