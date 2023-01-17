#Print the year the user will turn 100 years old

#Ask for username, the default value of a input function is a str
user_name = input("Whats your name: ")
#We can change the value of the input for manipulating it latter
user_age = int(input(f"{user_name}, whats your age: "))
current_year = 2023
birthday = current_year - user_age

#F strings a very usefull to print info for the use
age = f"{user_name}, in the year {birthday + 100} you will be 100 years old"
print(age)

n_times = int(input(f"{user_name} give me a number: "))

#Here is usefull to use strings concatenation to 
print((age + "\n")*n_times)

