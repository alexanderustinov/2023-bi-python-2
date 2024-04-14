from pickle import dump

from cryptography.hazmat.primitives.asymmetric import rsa

private_key = rsa.generate_private_key(
    key_size=2048,
    public_exponent=65537
)

public_key = private_key.public_key()


# pickle does not help - strange rusty object

# with open('privkey', 'wb') as f:
#     dump(private_key., f)

# with open('pubkey', 'wb') as f:
#     dump(public_key, f)

# use https://gist.github.com/gabrielfalcao/de82a468e62e73805c59af620904c124
