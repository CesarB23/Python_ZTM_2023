#Lambda expressions
#Functions used once, anonymous functions that dont need a definition or name
# lambda "parameter": func/manipulatiob/action (paramenter)
from functools import reduce
my_list = [1,2,3,4,5]
#Map
print(list(map(lambda item: item*2,my_list)))
print(list(map(lambda item: item**2,my_list)))
#Filter
print(list(filter(lambda item: item % 2 != 0,my_list)))
#Reduce
print(reduce(lambda acc, item: acc+item,my_list))
print(my_list)
