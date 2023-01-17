class PlayerCharacter:
    #Class object attribute, static for the whole class
    membership = True
    def __init__(self,name,age): 
        if(PlayerCharacter.membership): #Because membership is a COA we can use the class itself to call the this attibute
            self.name = name 
            self.age = age

    def shout(self): 
        print(f"My name is {self.name}") #But in a method we have to use self to call the attributes of the object
        # print(f"My name is {PlayerCharacter.name}") 

player1 = PlayerCharacter("Cesar",44) #Instanciating
player2 = PlayerCharacter("Itzel",48) #Instanciating
