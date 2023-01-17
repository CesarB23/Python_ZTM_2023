#Truthy and falsy are no True/False statements but checks thatn object in python is not zero or an empty data type
#Are usefull to check non filled information 
#If we make a logic check for a non-zero or empy data type we obtain True or either False
print(bool(5))
print(bool('hello'))
print(bool(['2','2']))

password = 'password'
username = 'jhonny'

if password and username:
    print("User info complete")
    