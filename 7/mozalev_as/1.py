from passlib.hash import argon2

password = input('Настоятельно не рекомендую устанавливать пароль более 3х знаков, если у вас нет лишних пары часов жизни. \n Введите пароль: ')
h = argon2.using(rounds=1).hash(password)

with open('./.hash','w+') as f:
    f.write(h)



# print(md5.digest())
# hash_ =md5.hexdigest()
# while True:
#     print("enter password: ")
#     hash_now=hashlib.md5(input().encode()).hexdigest()
#     if hash_now == hash_:
#         break
#     print(f'wrong!  (md5={hash_now})' )
    