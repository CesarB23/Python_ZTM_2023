#Dict Methods
user = {
    'age' : 22,
    'gender' : 'Male'
}
#Get
print(user.get('hobbies','lol'))
print(user)
#Another way to create dicts with the built in function
user2= dict(name = 'Cesar Borgia')
print(user2)
#Search for objects in a dict
print('name' in user2)
#Keys, check for
print('age' in user2.keys())
#Values, check for
print('Male' in user.values())
#Items
print(user.items())
#Clear
user2.clear()
print(user2)
#Copy
user3 = user.copy()
print(user3)
#Pop
user3.pop('gender')
print(user3)
#Update
user3.update({'age':44})
print(user3)