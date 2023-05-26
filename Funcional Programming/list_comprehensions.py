#Comprehensions, list, sets, dictionarys

my_list = [i for i in "hello"]
print(my_list)
my_list_2 = [i*2 for i in range(0,100)]
print(my_list_2)
my_list_3 = [i**2 for i in range(0,100)]
print(my_list_3)
my_list_4 = [i**2 for i in range(0,100) if i % 2 ==0 ]
print(my_list_4)