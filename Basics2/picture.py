#Exercise!
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for row in picture:
    for pixel in row:
        if pixel == 0:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print("")
#Assing the pixels to variables
empty = " "
fill = "$"

for row in picture:
    for pixel in row:
        if pixel:
            print(fill,end=" ")
        else:
            print(empty,end=" ")
    print("")
