import hashlib

passwords = ["password", "123456", "qwerty"]

with open("hashes.txt", "w") as f:
    for pwd in passwords:
        hash_md5 = hashlib.md5(pwd.encode()).hexdigest()
        f.write(hash_md5 + "\n")
