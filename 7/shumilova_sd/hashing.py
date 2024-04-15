from cracking import hash

password = input('Please, enter your password: ')

with open('password.txt', 'w') as file:
    file.write(hash(password))