
class PlayerCharacter:
    def __init__(self,name,age): #Self is a way to refer to the class we just created
        self.name = name #With this notation we assing the atribute to the object
        self.age = age #Attributes, proterties

    def run(self): #Method
        print("Run")

player1 = PlayerCharacter("Cesar",44) #Instanciating
player2 = PlayerCharacter("Itzel",48) #Instanciating
# player2.attack = 50
#When we call the object, whatever is to the left of the period takes place of self to refer to that object
print(player1.name) #Using the method notation to access the attribute of name
print(player1.age)
print(player1.run())
# print(player2.attack)
#print(player1.attack)