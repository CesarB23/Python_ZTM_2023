#Standard way to open a file
#While writing and reading the program set a cursor a the beggining of the file
#We have to be carefull where we are writing new text or whatever

with open('test.txt',mode='r+') as my_file:
    text = my_file.write("hey its me")
    print(text)