# Below we are initialising a class for a student with variables name, age and course.

class Student():
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

# Below we are creating two functions, one to state the student is on lunch and one to state that they are at home.

    def lunch(self):
        print(self.name + " " + "is on lunch")

    def home(self):
        print(self.name + "is at home")

    def student_details(self):
        print("Student Name:" + " " + self.name)
        print("Age:" + " " + self.age)
        print("Course:" + " " + self.course)


mehdi = Devops("Mehdi", "21", "DevOps")
print(mehdi.student_details())

