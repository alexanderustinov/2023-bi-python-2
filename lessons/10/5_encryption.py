from pickle import load

import openssh_key.private_key_list as pkl
import cryptography.hazmat.primitives.asymmetric.rsa as rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# # рабочий код для получения своих ssh-ключей
# from pathlib import Path
# home = Path.home()

# pk_sk_pair = pkl.PrivateKeyList.from_string(open(home / '.ssh' / 'id_rsa').read())
# own_private_key = pk_sk_pair[0].private.params.convert_to(rsa.RSAPrivateKey)
# own_public_key = pk_sk_pair[0].public.params.convert_to(rsa.RSAPublicKey)


with open('pair.pkl', 'rb') as f:
    pk_sk_pair = load(f)
private_key = pk_sk_pair.private.params.convert_to(rsa.RSAPrivateKey)

correspondent_pubkey = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDDrFeHXcEnawVpx1/oKJ5pWUHTR9kGuLoOkBwgj9QdBcO4ECMFx3gdO6SMVO2r55RJvBAbhKPypdN2POyhLEhuVOw/2aUoTL+yitpzproQ8Qcfo21KarlolBv43T1cUA3R/oNer3N2YfaNRNNZ/J5YL2oGqM9kUtxVrolwDX8YPoEKOkG5rHheDlcZSmziF4Q6i/fdU7QWDtQU31e0tbxQpPd6ImlYlfnihqZbTxYXrVhkydTqOtPW3H8fDmqN4Nvk33l7qfKzTykDzJLfhZ7tT7gMB+cX8hyZN7F8f5VK9I31t8lczZV9C3nwxGE/mlDEyJxVGYr3ouHGWKpsLs2uBSOsoyZDrR3E9DMknoJDdxAJ2BXpCAxlxkmZgv1/NeV8i6PVzEE+1/UuhNxzZ7iVfF8fEUaW7xViEmom368IhKErL3TFrxPBmgGWoKO6euXGa3Cgt7C/XVs4KDzYa+tXAWHzFTyp3ooV1ok/TWS/hlUwTotcl+4FXcu0LgLu9TURRNV2BzgfSYYDQI24BP1A30uXe8bHuSGn0p/OvYf9rEFhn588fem4TY5RU/PWwcicK3QCgz5jtZIhdQTQZQ7ztAvOaTCuAZpwH7mRdFN1xod5+hngEadZQ5E/pUcdCR1xF2jtQj4ZnNarQZXLEv9wctCcOID8uEwGbfrO3DVOMQ=="
public_key = pkl.PublicKey.from_string(correspondent_pubkey).params.convert_to(rsa.RSAPublicKey)

message = b"Hello, Ivan, my name is Ustinov"
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

message_encrypted = b';$\x17\xd2\xde\xd2\xf2f\x06\xd3\xce\x12JMSL+C[\x80\xc8\x9f \x10n4y\xc5\xb6\xae-\x07\xb3W[\xe4\xe9nq\xefaEaW\x85;\xcbp-\xa8H\xcd\x169\xb1\x14\xf7\xf3F\xdc\x9f,\xf8\xb2\xe4\xear\x86\x0e\xf6\r\x83\xaf\xccg\xa9f\x91m\xe6J\x10\xeb\xe8l\xd6<\x1e2\x90\xb79\x82\x83\x16G\xf2\xb0\xe9\x8b\x0e\xb1\xd2\xec\xe5\xe2\xeb\x90\xaf\xdd\xa7#K\x0c\x9a/\xf0\xd7\xc8\x87q\'\x19\xb65\xcaR\x86d>\x9eV3k\xe2%$c\x1f\x0f\xe4V9\xae\x03\x18\x1a\xee\x03\xff\xa9v\x8eQD\xa5\x12<\x01BKZ, \x83\xa9\xd6L\x94\xb82\x9f\x00\xfbS\x12cur\x9f\xfe&TV\x02\xb3\xce\x0c[\xae\xd9\x0b\xa0R\xf1\xd43\x87\xacE\xcf\x17\xcc0F\xd9c\xab\xa7\x16\'\xa6\xefL\xf47\xce6>\xa0J\x19\xeb\xdd\x90\xa0\xff\xfb\x0ep\xa00\x89\xc5\x89\x8c\xc8\x07\xdes\x08h\xfaJ^\n\xdb\\\xfei\x9c\x9c\xf0V\xb5$hwE\x18\x12\xdd\xd1m\xb0<\xf7K\xbaV\x93\x1e\xe3\x9a\xebo6S\xed\xf0\xb2\xb6\xa9}2\xb0\x9eJ\xe9t\x02\xf2>\xaa\x9e\xd2|h\x90\x1f\xcc\xfb\x80\x8d\xcb\xc4z\xc3?9?\xaa\xba\xc4\xd7Z\x7fc"\xf6*\xc3\xe4\xd9\x86\xb0\xe2\nm\xda\x94\xee\x1a\x06\xdaY5\xd9\xdc3\x18\x93\xf8\xf0\x99\xb8mX\xe6b\xd4\xf6\xb8\xd67\xc9\x1e\xe6F\xa2v\x91\xb2h"\x172\xdb\xf3d\x98Y\x96\xcc(\xb6\x14\xe0\xcee$\xf4\x83C\x7f\x12a\xd6\xbc5\xa0\r\xd5\xbc\x10=\xf8\xd2}deC\xc5\xdbb\xaa \xfe\x8d\xd0\xaeo>n\xe9s:\xff\xf6\x96\x8e%\xd0\xa2uzk&O8\xfaX\xab\x97:\xf9D\x908\xac(-Kae\xc8\xb2\xba\x97\x9c\xdd\x0c47\x9e\xe4\xc4D\xb4\xbb\x06\xe2\'j.\x0b\x12\xcd\xd0\xdf\xaa\xcba\xcb9\x13t\x88\xd2z\x17\xe1\x82A/%\x1d\x8c\xa4c\x19.\x9d\xc7F\x9d=\x1caa\xc1F{2 \xd9\xa6M\xc8&d\xb0'

print(private_key.decrypt(
    message_encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
))