# First we import the Student class from student_data

from student_data import Student


class Devops(Student):
    def __init__(self, name, age, course):
        super().__init__(name, age, course)


# Above we have used super to inherit functions from student_data.py
# We don't need to write any functions in this file because they are all inherited.

mehdi = Devops("Mehdi", "21", "DevOps")

print(mehdi.student_details())



