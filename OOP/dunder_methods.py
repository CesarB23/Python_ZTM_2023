#Dunder methods
#__method__ speciall notation

class Toy():
    def __init__(self,color,age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name':"Coco",
            'has_pets': False
        }
        
    #We can modify the dunder methods with our own instructions
    #Its no recomendated but can be implemented

    def __str__(self):
        return f"{self.color}"

    def __call__(self):
        return('yesss')

    def __getitem__(self,i):
        return self.my_dict[i]


toy1 = Toy("Woody",23)

print(toy1())
print(toy1['name'])