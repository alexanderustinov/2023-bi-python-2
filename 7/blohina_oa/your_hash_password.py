import random
import string
import hashlib
print('Введите длину пароля от 1 до 5 символов = ', end = '')
a = int(input())
pasw = ''.join(random.choice(string.ascii_letters) for _ in range(a))
#print(pasw)
hashed_pasw = hashlib.md5(pasw.encode()).hexdigest()
with open('my_pass.py', 'w') as file:
    file.write(f"pasw_hash = '{hashed_pasw}'\n")
