#Data structures, usefull to store data, like a frige stores food, a backpack items, but the difference if how to access to those stored items, 
#Each data structure is usefull for a differente purpose

#Lists are the most common data structures, as well as strings, we can do indexing, slicing and aplying metods
items = ['start','stop','stepover']
#Lists are mutable, we can replace the elements
items[0] = "something"
print(items)
#Using list slicing creates a new list in memory
#To create a copy of a list using list slicing we have to be carefull, we have to use semicolon
new_items = items[:]
new_items[0] = "hello"
print(new_items)
print(items)