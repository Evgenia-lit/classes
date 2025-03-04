class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_in_progress = []
        self.grades = {}

    def add_grade(self, course, grade):
        if course not in self.grades:
            self.grades[course] = []
        self.grades[course].append(grade)

    def get_average_grade(self, course):
        if course in self.grades and self.grades[course]:
            return sum(self.grades[course]) / len(self.grades[course])
        return 0


class Lecturer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def add_grade(self, course, grade):
        if course not in self.grades:
            self.grades[course] = []
        self.grades[course].append(grade)

    def get_average_grade(self, course):
        if course in self.grades and self.grades[course]:
            return sum(self.grades[course]) / len(self.grades[course])
        return 0


def get_average_student_grade(students, course):
    total_grades = 0
    count = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            count += len(student.grades[course])
    if count == 0:
        return 0
    return total_grades / count


def get_average_lecturer_grade(lecturers, course):
    total_grades = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    if count == 0:
        return 0
    return total_grades / count


# Создание студентов и добавление оценок
student1 = Student("Иван", "Иванов")
student2 = Student("Петр", "Петров")

student1.add_grade("Python", 9)
student1.add_grade("Python", 8)
student1.add_grade("Java", 7)

student2.add_grade("Python", 10)
student2.add_grade("Python", 9)
student2.add_grade("Java", 8)

students = [student1, student2]

# Создание лекторов и добавление оценок
lecturer1 = Lecturer("Анна", "Сидорова")
lecturer2 = Lecturer("Мария", "Кузнецова")

lecturer1.add_grade("Python", 9)
lecturer1.add_grade("Python", 8)
lecturer1.add_grade("Java", 7)

lecturer2.add_grade("Python", 10)
lecturer2.add_grade("Python", 9)
lecturer2.add_grade("Java", 8)

lecturers = [lecturer1, lecturer2]


average_student_grade = get_average_student_grade(students, "Python")
print(f"Средняя оценка студентов за курс 'Python': {average_student_grade}")

average_lecturer_grade = get_average_lecturer_grade(lecturers, "Python")
print(f"Средняя оценка лекторов за курс 'Python': {average_lecturer_grade}")