#Error handling, allow us the python script still running if there is an error
while True:
    try:
        age = input("What's your age: ")
    except TypeError:
        print("Please enter a number")
    except ZeroDivisionError:
        print("Please enter age higher number than 0")
    else:
        print("thank you")
        break