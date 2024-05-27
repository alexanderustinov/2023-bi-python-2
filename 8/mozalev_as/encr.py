import jwt
import openssh_key.private_key_list as pkl
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from pathlib import Path

home = Path.home()
pk_sk_pair = pkl.PrivateKeyList.from_string(open(home / '.ssh' / 'id_rsa').read())
own_private_key = pk_sk_pair[0].private.params.convert_to(rsa.RSAPrivateKey)
own_pub_key = pk_sk_pair[0].public.params.convert_to(rsa.RSAPublicKey)

correspondent_pubkey = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC4OQ9pOjjdJGqqQEwVYLqqbvNRWiFYVXqjMACm72tJJQwd9WrRDIbmMYxjkYgCQ7i0FTTpvipaZjLz+aI0Be7Y77JL6N7URr0E7+J8VzTBDugkSArjcPj8WA2ecNaDcyJ/TeNc5+KPPDYTTpJX5WUVlIJNK/I0aNHYwuBaQdo9tDmnrqlsisuv9SnZLCI0OLFbH7k11/xyoAzQjJsEdxrjYC3Q1Yc/+f6FvKBFECXhKBZZFeRW19WnYJdABpmGgBaGSsDk19tQIq5GHV/vo4049SMG2kkLh6umY6Va8qFNVZKxQb1EC2rANncvINejPh7BYeQPSJYSGO5FIsVR/emThMzwh1TR8+UhbuzawI+I/p87d+yphFCQ/4+aA3nw/OjTjHH3wQJLs9Cp/6Go0yHZmuDksCaaFYeP/WCThlUG2sI5KkkfqXk95vi0BsMCv+lZmZSPoTP2WBAU8uWf7sW2aMztxk44dWGwoNxDmVhhAMPemKMQW04v6AhCRFs2EHU="
public_key = pkl.PublicKey.from_string(correspondent_pubkey).params.convert_to(rsa.RSAPublicKey)

question = "Кто?"
answer = "answer"
data = {"question": question, "answer": answer}

jwt_token = jwt.encode(data, own_private_key, algorithm='RS512')

jwt_token_b = jwt_token.encode()
chunk_size=318

for chunk in [jwt_token_b[i:i+chunk_size] for i in range(0, len(jwt_token_b), chunk_size)]:
    # print(chunk)
    encrypted_jwt = public_key.encrypt(
        chunk,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print("Зашифрованный JWT:", encrypted_jwt)

