#Reduce
from functools import reduce

my_list = [2,3,4]
def accumulator(acc,item):
    return acc + item

print(reduce(accumulator,my_list,0))
