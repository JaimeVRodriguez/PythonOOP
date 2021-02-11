class Dog:

    def __init__(self, name, human_age):
        self.name = name  # Attribute of dog
        self.human_age = human_age

    def get_name(self):
        return self.name

    def dog_age(self):
        if self.human_age <= 1:
            return 15
        elif self.human_age <= 2:
            return 24
        else:
            return 24 + ((self.human_age - 2) * 4)

    def details(self):
        name_message = f'Name: {self.name}'
        h_age_message = f'Age (human years): {self.human_age}'
        d_age_message = f'Age (dog years): {self.dog_age()}'

        return f'''
        {name_message}
        {h_age_message}
        {d_age_message}
        '''

    def bark(self):
        print(f'{self.name} goes woof')


# Instanciating
# Variable d
# Instance of dog class
d = Dog('Chloe', 6)
print(d.details())

d2 = Dog('Smalls', 4)
print(d2.details())
