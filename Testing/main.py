def sum_1(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            return "Please enter a number"
    except ValueError as err:
        return err