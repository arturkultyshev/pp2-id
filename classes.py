class Person():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.age = 0

    def say(self, message):
        self.message = message
        print(f"i said {self.message}")

    def age_of_person(self, year):
        self.age += 2023 - year


    def __str__(self):
        return f'это человек {self.name}'


class Sister(Person):
    def prezent(self):
        print('kypi')

person = Person('Artur', 'Kultyshev')
sister = Sister('Nika', "Kultyshev")
person.age_of_person(2004)
print(person.age)
print(sister.name)
print(person.name)
print(person)
