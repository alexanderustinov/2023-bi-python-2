import jwt

from common import something
from _2_rsa_keys import private_key, public_key

data_encoded = jwt.encode(something, private_key, 'RS512')
print(data_encoded)
print(jwt.decode(data_encoded, public_key, ['RS512']))