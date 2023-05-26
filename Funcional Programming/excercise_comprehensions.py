some_list = ['a','b','c','b','d','m','n','n']
duplicates = [i for i in some_list if some_list.count(i) > 1]
# duplicates = list(set([i for i in some_list if some_list.count(i) > 1]))
print(duplicates)