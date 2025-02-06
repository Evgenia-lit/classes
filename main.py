class Students:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.assessment_courses = []
        self.mark = []
        self.sr_values = 0


    def rate(self, lecturer, course, grape):
        if isinstance(lecturer, Lecturer) and course in self.assessment_courses and course in lecturer.for_grape:
            if course in lecturer.some_grapes:
                lecturer.some_grapes[course] += [grape]
            else:
                lecturer.some_grapes[course] = [grape]
        else:
            return 'Ошибка'


    def general_value(self):
        if len(self.mark) > 0:
            self.sr_values = sum(self.mark)/ len(self.mark)
        else:
            self.sr_values = 0


    def __lt__(self, other):
        return f'{self.name} имеет средний балл больше, чем {other.name}'

    def __gt__(self, other):
            return f'{self.name} имеет средний балл больше, чем {other.name}'


    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}'
                f'\nСредняя оценка за домашние задания: { self.sr_values }'
                f'\nКурсы в процессе изучения:{' '.join (self.courses_in_progress)}'
                f'\nЗавершенные курсы: {', '.join(self.finished_courses)}')

    def show(self):
        print(f'Имя: {self.name}, \nФамилия: {self.surname} '
              f' \nСредний балл за домашние задания: {self.sr_values}')


class Mentors:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentors):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.for_grape = []
        self.some_grapes = {}
        self.for_grape = []
        self.votes = []
        self.general_votes = 0


    def compare_grades (self,other):
        if isinstance(other, Lecturer):

            if self.general_votes == other.general_votes:
                return (f"{self.name} {self.surname} имеет такой же балл как и "
                    f"{other.name} {other.surname}")
            elif self.general_votes > other.general_votes:
                return (f"{self.name} {self.surname} имеет балл больше, чем "
                    f"{other.name} {other.surname}")
            elif self.general_votes < other.general_votes:
                return (f"{self.name} {self.surname} имеет балл меньше, чем "
                    f"{other.name} {other.surname}")
            else:
                return f'Невозможно сравнить'


    def for_votes(self):
        if len(self.votes) > 0:
            self.general_votes = sum(self.votes)/len(self.votes)
        else:
            self.general_votes = 0


    def __str__(self):
        return ( f'Имя: {self.name} '
                 f'\nФамилия:{self.surname}'
                 f' \nСредняя оценка за лекции :{self.general_votes}')


class Reviewer(Mentors):

    def __init__(self,name, surname):
        super().__init__(name, surname)
        self.courses_attached = []


    def check (self, student, course, grape):
        if (isinstance(student, Students) and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grape]
            else:
                student.grades[course] = [grape]
        else:
            return 'Ошибка'


    def __str__(self):
        return (f'Замечательный ревьюер по имени: {self.name} и '
                f'\nФамилии: {self.surname}')



best_student = Students("Анастасия", "Головина")
best_student.courses_in_progress += ['Python']
best_student.finished_courses = ["Git", "Основы программирования на Python"]
best_student.mark += [10,9,9,10,8,9]
best_student.assessment_courses = ["Python"]
best_student.general_value()

nerd_student = Students("Иван","Абрамович")
nerd_student.mark = [10,10,10,10,9,5]
nerd_student.general_value ()

lazy_student = Students("Саша","Попов")
lazy_student.mark = [9,8,7,9,10,8]
lazy_student.general_value ()


cool_mentor = Reviewer('Григорий', 'Прошин')
cool_mentor.courses_attached += ['Python']
cool_mentor.check(best_student, 'Python', 10)



cool_lecturer = Lecturer("Павел", "Башкатов")
best_student.assessment_courses = ["Python"]
cool_lecturer.for_grape = ["Python"]
best_student.rate(cool_lecturer, "Python", 10)
cool_lecturer.votes = [10,10,10,9,7]
cool_lecturer.for_votes ()

welldone_lecturer = Lecturer("Кирилл", "Смирнов")
welldone_lecturer.votes = [10,7,10,9,8,10]
welldone_lecturer.for_votes()

great_lecturer = Lecturer("Алёна","Батицкая")
great_lecturer.votes = [10,10,10,10,10,10]
great_lecturer.for_votes()


print(best_student)
nerd_student.show()
lazy_student.show()

print(cool_lecturer)
print(welldone_lecturer)
print(great_lecturer)
print(cool_mentor)


print(best_student < nerd_student)
print(nerd_student > lazy_student)

print(great_lecturer.compare_grades(welldone_lecturer))
print(welldone_lecturer.compare_grades(cool_lecturer))
print(cool_lecturer.compare_grades(great_lecturer))

