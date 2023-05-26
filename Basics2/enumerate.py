#Enumarate gives us an index of what we are looping
for i,char in enumerate(list(range(100))):
    if char == 50:
        print(f'The index of 50 is: {i}')


for i,char in enumerate(list(range(100))):
    print(i,char)