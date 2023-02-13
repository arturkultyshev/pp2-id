class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.age = 0

    def say(self, message):
        self.message = message
        print(f'я сказал/сказала {self.message}')

    def age_of_person(self, year):
        self.age = 2023 - year

    def __str__(self):
        return f'я {self.name}'
