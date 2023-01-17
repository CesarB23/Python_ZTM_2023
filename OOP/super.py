class User():
    def __init__(self,email):
        self.email = email

    def sing_in(self):
        print("Logged in")

class Wizard(User):
    def __init__(self, name, power, email):
        #Is a way to inherit attributes to other classes that already have a init dunder method
        #In order to dont repeat code
        # User.__init__(self,email)
        super().__init__(email) #Default method to do the same
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with {self.power} point of power")

wizard1 = Wizard("Pangoringo",50,"pango@gmail.com")
print(wizard1.email)

