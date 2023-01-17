#Scope - what variables do i have access to..?
#The variable scope is divided in two worlds
#Global and local variables

#Order of the variables scope
#1 - Start with local
#2 - Parent local
#3 - Global
#4 - Built in python functions

a = 1 # Global
def parent():
    a = 10 # Local
    def confusion():
        return a   #Parent local
    return confusion()

print(parent())
print(a)

