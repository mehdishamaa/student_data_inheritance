from student_data import Student


class Devops(Student):
    def __init__(self, name, age, course, grade):
        self.name = name
        self.age = age
        self.course = course
        self.grade = grade

# Below we are creating two functions, one to state the student is on lunch and one to state that they are at home.

    def lunch(self):
        print(self.name + " " + "is on lunch")

    def __home(self):
        print(self.name + "is at home")

    def student_details(self):
        print("Student Name:" + " " + self.name)
        print("Age:" + " " + self.age)
        print("Course:" + " " + self.course)
        print("Grade is:" + " " + self.grade)


mehdi = Devops("Mehdi", "21", "DevOps", "9")

print(mehdi.student_details())



