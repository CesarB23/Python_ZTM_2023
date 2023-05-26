#We have to be carefull with the mode
#If the file doesnt exist, it will create it and write on it
with open('test2.txt',mode='w') as my_file:
    text = my_file.write("hey its me assholes")
    print(text)