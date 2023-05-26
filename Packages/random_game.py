import sys
import random

rand = random.randint(int(sys.argv[1]),int(sys.argv[2]))
your_numb = 0

while your_numb != rand:
    try:
        your_numb = int(input(f"Give me a number from {int(sys.argv[1])} to {int(sys.argv[2])}: "))
        if your_numb > rand:
            print("Your number is higher than the random number")
        elif your_numb < rand:
            print("Your number is lower than the random number")
        elif your_numb == rand:
            print(f"You guess it")
            break
    except ValueError:
        print("Please enter a int")
        continue
    

        



