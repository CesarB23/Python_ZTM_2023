#While loops are usefull when we dont know the lenght of what we are looping
#We need more conditions to make it work without creatin an infinite loop
i = 0
while i < 50:
    print(i)
    i += 1
    break
else:
    print("Done")
#infinite Loops
while True:
    respone = input('Say something')
    if respone == 'bye': #Break infinite loops
        break