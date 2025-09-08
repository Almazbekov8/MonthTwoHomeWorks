class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

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
              f"я родился в {self.birth_date}, я {self.occupation},"
              "у меня есть высшее образование" if self.higher_education else "у меня нет высшего образование")



class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education,)
        self.hobby = hobby

    def introduce(self):
        print(f"Привет меня зовут {self.name}, я близкий друг Игоря,"
              f"я родился в {self.birth_date}, я {self.occupation},"
              f"после работы у меня есть любимое хобби - {self.hobby},"
              "у меня есть высшее образование" if self.higher_education else "у меня нет высшего образование")

