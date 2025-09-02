class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(f"Привет меня зовут {self.name}, я родился в {self.birth_date}, я {self.occupation},",
              "у меня есть высшее образование" if self.higher_education else "у меня нет высшего образование" )

person1 = Person("Адилет", "11.09.1990", "Водитель", True)
person2 = Person("Нурсултан", "09.08.2007", "Юрист", True)
person3 = Person("Арсен", "21.05.2006", "Бариста", False)

person1.introduce()
person2.introduce()
person3.introduce()