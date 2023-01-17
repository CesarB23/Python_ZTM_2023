class PlayerCharacter:
    #Class object attribute, static for the whole class
    membership = True
    def __init__(self,name="Anonymous",age=0): 
        if (age > 18): #We can use safeguards to instanciate the correct way
            self.name = name
            self.age = age

    def shout(self): 
        print(f"My name is {self.name}") 

player1 = PlayerCharacter("Xokas",19) #Instanciating
print(player1.shout())