import re
#The expression is valid with [a-zA-Z0-9_.+-]
#Letters aA-zZ numbers 0-9 and the symbols _.+- 
#No lenght specified
#Match a unique character @ and then all characters in list
#Match a unique character . and then all characters in list
pattern = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$")
email = input("Please enter you Email: \n")
a = pattern.search(email)

print(f"Logged in {email}") if a else print("Invalid Email")