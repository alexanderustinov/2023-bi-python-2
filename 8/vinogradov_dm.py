import jwt
import openssh_key.private_key_list as pkl
import cryptography.hazmat.primitives.asymmetric.rsa as rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from pathlib import Path
answer=input("Введите ответ на вопрос:")
home = Path.home()

pk_sk_pair = pkl.PrivateKeyList.from_string(open(home / '.ssh' / 'id_rsa').read())
private_key = pk_sk_pair[0].private.params.convert_to(rsa.RSAPrivateKey)
public_key = pk_sk_pair[0].public.params.convert_to(rsa.RSAPublicKey)

quest = {"Question" : "C кем?", "Answer" : answer}

correspondent_pubkey = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC4OQ9pOjjdJGqqQEwVYLqqbvNRWiFYVXqjMACm72tJJQwd9WrRDIbmMYxjkYgCQ7i0FTTpvipaZjLz+aI0Be7Y77JL6N7URr0E7+J8VzTBDugkSArjcPj8WA2ecNaDcyJ/TeNc5+KPPDYTTpJX5WUVlIJNK/I0aNHYwuBaQdo9tDmnrqlsisuv9SnZLCI0OLFbH7k11/xyoAzQjJsEdxrjYC3Q1Yc/+f6FvKBFECXhKBZZFeRW19WnYJdABpmGgBaGSsDk19tQIq5GHV/vo4049SMG2kkLh6umY6Va8qFNVZKxQb1EC2rANncvINejPh7BYeQPSJYSGO5FIsVR/emThMzwh1TR8+UhbuzawI+I/p87d+yphFCQ/4+aA3nw/OjTjHH3wQJLs9Cp/6Go0yHZmuDksCaaFYeP/WCThlUG2sI5KkkfqXk95vi0BsMCv+lZmZSPoTP2WBAU8uWf7sW2aMztxk44dWGwoNxDmVhhAMPemKMQW04v6AhCRFs2EHU= 79814@AsusLaptop"
public_key = pkl.PublicKey.from_string(correspondent_pubkey).params.convert_to(rsa.RSAPublicKey)

message = jwt.encode(quest, private_key, 'RS512').encode()
chunk_size = 318

for chunk in [message[i:i+chunk_size] for i in range(0, len(message), chunk_size)]:
    ciphertext = public_key.encrypt(
    chunk,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
    print(' variation: ', ciphertext)
    
