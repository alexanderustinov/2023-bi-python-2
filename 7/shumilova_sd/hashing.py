from cracking import hash

print('Пароль должен содержать не более 4-х символов. Может состоять из латинских букв, цифр и/или специальных символов.')
password = input('Please, enter your password: ')

with open('password.txt', 'w') as file:
    file.write(hash(password))
