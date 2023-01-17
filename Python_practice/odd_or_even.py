#Check if a number is even or odd
num = int(input("Give me a number: "))

if num % 4 == 0 and num % 2 == 0:
    print(f"{num} is even and is multiple of 4")
elif num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

check = int(input("Give another number: "))

if num % check == 0:
    print(f"{num} is divisible by {check}")
else:
    print(f"{num} is not divisible by {check}")