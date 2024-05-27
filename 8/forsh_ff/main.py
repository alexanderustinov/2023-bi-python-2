import os
import jwt
import openssh_key.private_key_list as pkl
import cryptography.hazmat.primitives.asymmetric.rsa as rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from pathlib import Path
from dotenv import load_dotenv



load_dotenv()

anw = input("Введите ответ на вопрос:")
pk_sk_pair = pkl.PrivateKeyList.from_string(open(Path.home() / '.ssh' / 'id_rsa').read())
private_key = pk_sk_pair[0].private.params.convert_to(rsa.RSAPrivateKey)
public_key = pk_sk_pair[0].public.params.convert_to(rsa.RSAPublicKey)

q = {"Question": "Как?", "Answer": anw}

public_key = pkl.PublicKey.from_string(os.getenv('correspondent_pubkey')).params.convert_to(rsa.RSAPublicKey)

mes = jwt.encode(q, private_key, 'RS512').encode()
chunk_size = 318

for chunk in [mes[i:i+chunk_size] for i in range(0, len(mes), chunk_size)]:
    ciphertext = public_key.encrypt(
    chunk,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
    print(ciphertext)
