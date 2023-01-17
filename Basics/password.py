username = input("Username: ")
password = input("Password: ")
password_len = len(password)
secret_password = '*' * password_len
print(f"{username}, your password {secret_password} is {password_len} letters long")