from pickle import dump

import openssh_key.private_key_list as pkl

pk_sk_pair = pkl.PublicPrivateKeyPair.generate('ssh-rsa')
with open('pair.pkl', 'wb') as f:
    dump(pk_sk_pair, f)
    