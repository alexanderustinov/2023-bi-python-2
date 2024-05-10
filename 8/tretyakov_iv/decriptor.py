import openssh_key.private_key_list as pkl
import cryptography.hazmat.primitives.asymmetric.rsa as rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import jwt

from pathlib import Path

from everybody import EVERYONE

home = Path.home()

pk_sk_pair = pkl.PrivateKeyList.from_string(open(home / '.ssh' / 'id_rsa').read())
own_private_key = pk_sk_pair[0].private.params.convert_to(rsa.RSAPrivateKey)
own_public_key = pk_sk_pair[0].public.params.convert_to(rsa.RSAPublicKey)
for smn in EVERYONE:
    public_key = smn.get('pubkey')
    data_encoded = ''
    messages = smn.get('data')
    for i in messages:
        plaintext = own_private_key.decrypt(
            i,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        data_encoded+=plaintext.decode()
    pers_res = jwt.decode(data_encoded, public_key, ['RS512'])
    for i in pers_res:
        print(pers_res[i])
