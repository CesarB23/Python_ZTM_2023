#As we import many modules and the proyect becomes bigger and bigger
#We are going to have a "main.py or whatever" file where we are running
#The main program, this sintaxis helps us to check if its the main file
#In order to do an specific action in that file and only in that file

print(__name__)
if __name__ == '__main__':
    print("Hello")