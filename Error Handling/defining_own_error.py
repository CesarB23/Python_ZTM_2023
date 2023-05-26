def sum(num1,num2):
    try:
        return num1 + num2
    except TypeError as err:
        #Showing in line the error part
        print(f"Please enter numbers, {err}")
    except (TypeError,ZeroDivisionError) as err:
        #Multiple error handling
        print(f"Please enter numbers, {err}")

sum(1,"2")