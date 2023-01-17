#Inheritance "heredar" is a way that we can assing other functionalities from other classes
#To another one by just passing it as a parameter

#Parent class
class User():
    def sig_in(self):
        print("Logged in")

#Children,sub or derived classes
class Wizard(User):
    def __init__(self,name,power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")

class Archer(User):
    def __init__(self,name,power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")

wizard1 = Wizard("Cesar",3.14)
archer1 = Archer("Vic",333)

print(wizard1.sig_in())
wizard1.attack()
print(isinstance(wizard1,Wizard)) #Check True/False for an instance
print(isinstance(wizard1,User))