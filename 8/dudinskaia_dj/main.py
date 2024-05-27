import jwt
import openssh_key.private_key_list as pkl
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey
from pathlib import Path


def load_ssh_keys():
    home = Path.home()
    with open(home / '.ssh' / 'id_rsa', 'r') as key_file:
        pk_sk_pair = pkl.PrivateKeyList.from_string(key_file.read())
        private_key = pk_sk_pair[0].private.params.convert_to(RSAPrivateKey)
        public_key = pk_sk_pair[0].public.params.convert_to(RSAPublicKey)
    return private_key, public_key


def encode_jwt(private_key, payload):
    return jwt.encode(payload, private_key, algorithm='RS512')


def convert_public_key_from_string(public_key_str):
    return pkl.PublicKey.from_string(public_key_str).params.convert_to(RSAPublicKey)


def encrypt_message(public_key, message):
    encoded_message = message.encode()
    chunk_size = 318
    encrypted_chunks = []
    for i in range(0, len(encoded_message), chunk_size):
        chunk = encoded_message[i:i + chunk_size]
        ciphertext = public_key.encrypt(
            chunk,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        encrypted_chunks.append(ciphertext)
    return encrypted_chunks


def main():
    private_key, public_key = load_ssh_keys()

    payload = {"Question": "Для чего?", "Answer": "Чтоб не принимать смерть как то, что должно быть"}
    jwt_encoded = encode_jwt(private_key, payload)


    correspondent_pubkey = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC4OQ9pOjjdJGqqQEwVYLqqbvNRWiFYVXqjMACm72tJJQwd9WrRDIbmMYxjkYgCQ7i0FTTpvipaZjLz+aI0Be7Y77JL6N7URr0E7+J8VzTBDugkSArjcPj8WA2ecNaDcyJ/TeNc5+KPPDYTTpJX5WUVlIJNK/I0aNHYwuBaQdo9tDmnrqlsisuv9SnZLCI0OLFbH7k11/xyoAzQjJsEdxrjYC3Q1Yc/+f6FvKBFECXhKBZZFeRW19WnYJdABpmGgBaGSsDk19tQIq5GHV/vo4049SMG2kkLh6umY6Va8qFNVZKxQb1EC2rANncvINejPh7BYeQPSJYSGO5FIsVR/emThMzwh1TR8+UhbuzawI+I/p87d+yphFCQ/4+aA3nw/OjTjHH3wQJLs9Cp/6Go0yHZmuDksCaaFYeP/WCThlUG2sI5KkkfqXk95vi0BsMCv+lZmZSPoTP2WBAU8uWf7sW2aMztxk44dWGwoNxDmVhhAMPemKMQW04v6AhCRFs2EHU= 79814@AsusLaptop"
    public_key = convert_public_key_from_string(correspondent_pubkey)

    encrypted_messages = encrypt_message(public_key, jwt_encoded)
    for encrypted in encrypted_messages:
        print(encrypted)


if __name__ == "__main__":
    main()
