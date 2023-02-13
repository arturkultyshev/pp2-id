from class_person import Person


class Boy(Person):
    def say(self, message):
        self.message = message
        print(f'я сказал {self.message}')


class Girl(Person):
    def say(self, message):
        self.message = message
        print(f'я сказала {self.message}')


boy = Boy('artur', 'kultyshev')
girl = Girl('Masha', "Kim")
print(boy.name)
girl.say('Hello')
girl.age_of_person(2005)
print(girl.age)


"""
Создайте класс Soda (для определения типа газированной воды), 
принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду). 
В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки, 
а иначе отобразится следующая фраза: «Обычная газировка».



класс в него дается 3 отрезка 
если это треугольник то найти периметр
    

"""