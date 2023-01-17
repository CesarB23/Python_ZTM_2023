#Cleaning a simple code
def is_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False

print(is_even(20))

def is_even_2(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_even_2(20))

def is_even_3(num):
    if num % 2 == 0:
        return True
    return False
    
print(is_even_3(20))

def is_even_4(num):
    return num % 2 == 0

print(is_even_4(20))

        