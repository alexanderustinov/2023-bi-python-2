from itertools import product 
from string import ascii_lowercase
from hashlib import md5

hash_was = '5f4dcc3b5aa765d61d8327deb882cf99'

for i in range(8):
    print('word length:', i)
    gen = product(ascii_lowercase, repeat=i+1)
    found = False
    while True:
        try:
            word_now = ''.join(next(gen))
            hash_now = md5(word_now.encode()).hexdigest()
            if hash_now==hash_was:
                found = True
                print(f"password seems to be '{word_now}'")
                break
        except StopIteration:
            break
    if found:
        break
        # else:
        #     print(f"{word_now} {hash_now}")

if not found:
    print('password not found')
