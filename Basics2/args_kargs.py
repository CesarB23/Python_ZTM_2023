#*args, **kwargs
#Rule: parameters, *args, default paramters, **kwargs
def super_func(*args,**kwargs):
    #Print all the arguments given
    print(*args)
    #Print a tuple of the arguments
    print(args)
    #Return a dict of the kwargs
    print(kwargs)

    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total
#This way we can give the function all the arguments we want without specyfing them as parameters
#As well as keyword arguments
print(super_func(1,2,3,4,5,6,7,8,9,10,name=5,cow=6))