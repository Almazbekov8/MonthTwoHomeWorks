class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(f"Привет меня зовут {self.name}, я родился в {self.birth_date}, я {self.occupation}" +
              ", у меня есть высшее образование" if self.higher_education else "у меня нет высшего образование" )

