#Filter

#Filter info
my_list = [0,1,2,3,4,5]
def check_odd(item):
    return item % 2 != 0

#Returns only the items that satisfie the condition, True statements
print(list(filter(check_odd,my_list)))
print(my_list)

