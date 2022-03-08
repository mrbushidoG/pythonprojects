class Animal():

    def __init__(self,name):
        self.legs = 4
        self.mouth = True
        self.teeth = True
        self.name = name

    def eat(self):
        print("I'm an animal and i eat")

    def my_name(self):
        print(f"my Name is {self.name}")

class Dog(Animal):

    def __init__(self,name):
        self.name = name



myanimal = Animal('Animal')
mydog = Dog('Shepherad')

print(myanimal.my_name())
print(mydog.my_name())