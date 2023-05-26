import re

#At least 8 characters long, aA-zZ,0-9,$%@#,finish with digit
pattern = re.compile(r"[a-zA-Z0-9$%#@]{8,}\d$")
print("Create a password with at least 8 characers,letters aA-zZ,numbers 0-9, symbols $%@# and finish with a digit")
password = input("Enter your password: \n")

if re.search(pattern,password):
    print("Valid")
else:
    print("Invalid")