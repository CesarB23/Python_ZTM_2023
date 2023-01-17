#Functions are usefull to recycle lines of code to run every time we call it
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

def say_hello():
    print("Hello")

say_hello()

def show_img():
    for row in picture:
        for pixel in row:
            if pixel == 0:
                print(" ",end=" ")
            else:
                print("*",end=" ")
        print("")
#Call the function
show_img()