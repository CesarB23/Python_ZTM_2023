#We can let the interpreter know when we want to use a global variable in a function
total = 0

def count():
    global total
    total += 1
    return total
count()
count()
print(count())