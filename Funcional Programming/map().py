#Map
#Bad practice
def multiply_2(li):
    new_list = []
    for i in li:
        new_list.append(i*2)
    return new_list

print(multiply_2([1,2,3,4]))

#Map def
# map(action, iterable[],(),{})
my_list = [1,2,3,4,5]
def multiply_by2(item):
    return item*2

# print(list(map(multiply_by2,[1,2,3,4])))

# As a pure function, map doesnt modify the data from the outside
print(list(map(multiply_by2,my_list)))
print(tuple(map(multiply_by2,my_list)))
print(set(map(multiply_by2,my_list)))
print(my_list)