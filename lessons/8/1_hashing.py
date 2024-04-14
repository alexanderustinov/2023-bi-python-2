import hashlib

md5 = hashlib.md5('hello'.encode())
# print(md5.digest())
hash_ = md5.hexdigest()

while True:
    print("enter password:")
    hash_now = hashlib.md5(input().encode()).hexdigest()
    if hash_now == hash_:
        break
    print(f"wrong! (md5={hash_now})")
