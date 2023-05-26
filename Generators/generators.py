#A generator is a iterable, but not everything that is a iterable is a generator
# The built in range function is a generator and a iterable
# A list is a iterable but not a generator

# Standar form to create a generator
def generator(num):
    for i in range(num):
        yield i #Yield pause the iteration, creates each object one by one instead of all at once

g = generator(100)
print(g) # This creates a generator objects
print(next(g))  #Next key-word is what returns the next iteration from the generator
print(next(g)) #Next can be called as many times as the range expires