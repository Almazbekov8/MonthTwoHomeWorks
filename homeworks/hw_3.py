class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

    @occupation.setter
    def occupation(self, occupation):
        self.__occupation = occupation

    @higher_education.setter
    def higher_education(self, higher_education):
        self.__higher_education = higher_education

    def introduce(self):
        print(f"Привет меня зовут {self.name}, я родился в {self.birth_date}, я {self.occupation},",
              "у меня есть высшее образование" if self.higher_education else "у меня нет высшего образование" )



class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        print(f"Привет меня зовут {self.name}, я одноклассник Игоря,"
              f"мы учились вместе в группе {self.group_name},"
              f"я родился в {self.birth_date}, я {self.occupation},",
              "у меня есть высшее образование" if self.higher_education else "у меня нет высшего образование")




class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education,)
        self.hobby = hobby

    def introduce(self):
        print(f"Привет меня зовут {self.name}, я близкий друг Игоря,"
              f"я родился в {self.birth_date}, я {self.occupation},"
              f"после работы у меня есть любимое хобби - {self.hobby},",
              "у меня есть высшее образование" if self.higher_education else "у меня нет высшего образование")



classmate_1 = Classmate("Бектур", "5.12.2000", "Программист", True, "11 Д")
classmate_2 = Classmate("Артур", "30.05.1999", "Менеджер", False, "11 Д")
friend_1 = Friend("Курманбек", "12.08.2005", "Разработчик", False, "Компьютерные игры")
friend_2 = Friend("Арсен", "13.10.1999", "Финансовый директор", True, "Нечего не делать ")

person_list = [classmate_1, classmate_2, friend_1, friend_2]

for i in person_list:
    i.introduce()
