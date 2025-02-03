class Students:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender


class Mentors:
    def __init__(self, name, surname, cours):
        self.name = name
        self.surname = surname
        self.cours = cours

    def show(self):
        print (f"Его/Ее зовут {self.name} {self.surname} преподает {self.cours}")


class Lecturer(Mentors):
    def __init__(self, name, surname, cours):
        super().__init__(name, surname, cours)


class Reviewer(Mentors):
    def __init__(self,name, surname, cours):
        super().__init__(name, surname,cours)



boris = Students ("Борис","Иванов", "Men")
german = Mentors("Герамн", "Петров", "Python")
ruslan = Reviewer ("Руслан", "Богданов", "Java")
anastasia = Lecturer ("Анастасия", "Булочкина", "С++")

german.show()
ruslan.show()
anastasia.show()