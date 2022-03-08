# class Dog():
#
#     def __init__(self,name,breed):
#         self.name = name
#         self.breed = breed
#
# my_dog = Dog(name='Shephard', breed='dogcow')
#
# print(my_dog.name + ' ' + my_dog.breed)

class Calculate():

    def __init__(self):
        pass

    def add_this(self,number1,number2):
        return number1 + number2


add_this = Calculate()

number1 = 123
number2 = 344

result = add_this.add_this(number1,number2)

print(result)

