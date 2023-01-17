class PlayerCharacter:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def shout(self):
        pass
    
    @classmethod #This way we can create methods for the class we just created
    def adding_things(cls,num1,num2):
        #We can istanciate in the classmethod
        return cls("Ted",num1 + num2)
        
        
    @staticmethod #This way we can create methods for the class we just created without access to the cls
    #We cant modify them
    def adding_things2(num1,num2):
        return num1 + num2

# player1 = PlayerCharacter("Tom",22)
#We can call the method without making the instanciation
player3 = PlayerCharacter.adding_things(5,5)
print(player3.age)


