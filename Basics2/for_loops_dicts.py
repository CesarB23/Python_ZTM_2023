#We could use a method for printing more info
user = {
    'name':'Golem',
    'age':5000,
    'powers':False
}
#.items return a tuple of each key-value pair
for i in user.items():
    print(i)
#To unpack values from a tuple theres two ways
#Assing variable outside the for loop
for item in user.items():
    key,value = item
    print(key,value)

#Assing the variable to unpack in the loop itself
for key,value in user.items():
    print(key,value)

#.values return only values
for i in user.values():
    print(i)
   
#.keys return only keys
for i in user.keys():
    print(i)
