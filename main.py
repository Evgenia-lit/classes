class Students:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.assessment_courses = []

    def rate(self, lecturer, course, grape):
        if isinstance(lecturer, Lecturer) and course in self.assessment_courses and course in lecturer.for_grape:
            if course in lecturer.some_grapes:
                lecturer.some_grapes[course] += [grape]
            else:
                lecturer.some_grapes[course] = [grape]
        else:
            return 'Ошибка'


    def show(self):
        print(f'Оценка успеваемости {self.name} {self.surname} по предмету - {self.grades}')

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
        self.some_grapes = {}

    def show(self):
            print(f'Оценка эффективности преподавателя {self.name} {self.surname} по {self.some_grapes}')


class Reviewer(Mentors):
    def __init__(self,name, surname):
        super().__init__(name, surname)
        self.courses_attached = []


    def check (self, student, course, grape):
        if isinstance(student, Students) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grape]
            else:
                student.grades[course] = [grape]
        else:
            return 'Ошибка'




best_student = Students("Анастасия", "Головина")
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Григорий', 'Прошин')
cool_mentor.courses_attached += ['Python']
cool_mentor.check(best_student, 'Python', 10)



cool_lecturer = Lecturer("Павел", "Башкатов")
best_student.assessment_courses = ["Python"]
cool_lecturer.for_grape = ["Python"]
best_student.rate(cool_lecturer, "Python", 10)


best_student.show()
cool_lecturer.show()