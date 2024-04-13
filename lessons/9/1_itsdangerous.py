from itsdangerous import Signer, Serializer, URLSafeTimedSerializer
from time import sleep
from common import secret, something

#from secrets import token_hex
#secret = token_hex()

# print(secret)
# s = Serializer(secret)
s = URLSafeTimedSerializer(secret)


signed_data = s.dumps(something)
# signed_data_changed = signed_data.replace('true', 'false')
signed_data_changed = signed_data
signed_data_changed+='a'

sleep(3)

print(signed_data, signed_data_changed)
print(s.loads(signed_data, return_timestamp=True, max_age=2))
# print(s.loads(signed_data_changed))