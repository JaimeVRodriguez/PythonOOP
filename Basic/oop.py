class Dog:

    def __init__(self, name):
        self.name = name  # Attribute of dog

    def get_name(self):
        return self.name

    def bark(self):
        print(f'{self.name} goes woof')


# Instanciating
# Variable d
# Instance of dog class
d = Dog('Chloe')
print(d.get_name())

d2 = Dog('Smalls')
print(d2.get_name())


d.bark()
