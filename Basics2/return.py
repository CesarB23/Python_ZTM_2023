#Functions need to return something as the built in python functions
#If the function doesnt return anything it will return None type

def quick_sum(a,b):
    return a + b
print(quick_sum(5,5))
#We can assing  the returned value to a variable 
total = quick_sum(15,20)
print(total)
#We can go further by assining the returned value of a function as the input of another function
print(quick_sum(10,quick_sum(50,100)))
