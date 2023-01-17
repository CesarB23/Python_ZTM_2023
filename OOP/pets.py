class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#1 Add nother Cat
class Cow(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [Simon("Simon",26),Sally("Itzel",23),Cow("Cow",25)]

# simon = Simon("Simon",26)
# sally = Sally("Itzel",23)
# cow = Cow("Cow",25)
# my_cats = [simon,sally,cow]

#3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

#4 Output all of the cats walking using the my_pets instance
#print(my_pets.walk()) is not necessary to print
# my_pets.walk()
print(my_cats[0].walk())
my_cats[0].walk()
print(my_pets.walk())
my_pets.walk()

