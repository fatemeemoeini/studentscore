class StudentScore:
    def __init__(self, name):
        self.name = name
        self.grade = []

    def addgrade(self, grade):
        self.grade.append(grade)

    def calculate(self):
        if len(self.grade) == 0:
            return 0
        else:
            return sum(self.grade) / len(self.grade)
            # return self.grade[0] + self.grade[1] + self.grade[2] + self.grade[3] + self.grade[4]


def get_students():
    students = []
    number_of_student = (int(input("Enter number of students: ")))

    for i in range(number_of_student):
        name = input("Enter name: ")
        student = students(name=name)
        students.append(student)

        return students


def displply_all_averages(students):
    for student in students:
        print(student.calculate())


def main():
    students = get_students()
    displply_all_averages(students)


if __name__ == '__main__':
    main()
