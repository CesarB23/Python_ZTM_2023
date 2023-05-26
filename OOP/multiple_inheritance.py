class User():
    def sig_in(self):
        print("Logged in")

class Wizard(User):
    def __init__(self,name,power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")

class Archer(User):
    def __init__(self,name,arrows):
        self.name = name
        self.arrows = arrows

    def arrows_left(self):
        print(f"{self.arrows} left")

    def run(self):
        print("Running")

#Multiple inheritance from multiple *classes,
#No the most convinient option, could be confussing 
class Cyborg(Wizard,Archer):
    def __init__(self, name,power,arrows):
        Archer.__init__(self,name,arrows)
        Wizard.__init__(self,name,power)

cyborg1 = Cyborg("Cesar",50,100)
print(cyborg1.attack())
print(cyborg1.run())
print(cyborg1.arrows_left())
print(cyborg1.sig_in())
