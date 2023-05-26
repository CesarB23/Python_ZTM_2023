while True:
    try:
        age = int(input("What's your age: "))
        age = 10/age
    except TypeError:
        print("Please enter a number")
        continue #Returns to the top of the loop
    except ZeroDivisionError:
        print("Please enter age higher number than 0")
        break #Ends the program
    else:
        print("thank you")
        break
    finally: #Its the last action done in the loop, no matters if it ends lines up
        print("ok, im done")
print("Hello") #If the programm ends with a break, it will 
                # get out of the loop and execute