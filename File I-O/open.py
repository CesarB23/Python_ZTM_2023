#Opening file
my_file = open ('test.txt')
print(my_file.read())
print(my_file.readlines())
#It's a good practice to always close the file when ended the action
my_file.close()