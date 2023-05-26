#Zip
#Like a zipper, matches the i'th element of an arrays of iterables 
# with the i'th element of another element of an array, 
my_list = [1,2,3,4,5]
your_list = [10,20,30,40]

merged = list(zip(my_list,your_list))
print(merged)
