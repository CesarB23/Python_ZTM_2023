#Set and dict comprehension

#Set comprehension stills the same as lists buy returns a set with no duplicates

simple_dict = {
    'a':1,
    'b':2
}

my_dict = {k:v**2 for k,v in simple_dict.items()}
print(my_dict)


my_dict_2 = {num:num*2 for num in [1,2,3,4,5]}
print(my_dict_2)