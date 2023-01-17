my_list = [1,2,3,4,5,6,7,8,9,10]
my_sum = 0
for i in range(len(my_list)):
    my_sum = my_sum + my_list[i]
print(my_sum)

for i in my_list:
    my_sum = my_sum + i
print(my_sum)