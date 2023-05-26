#Debbuing is a common practice of developing code,
#Python comes with a built in debugger library that allows
#to debbug line by line nteractivly

import pdb

def add(n1,n2):
    pdb.set_trace()
    return n1 + n2

print(add("hola",2))

#help command helps to list commands in the library
#The best way to debbug is throw a IDE 