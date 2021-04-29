from essay import Essay
from user import User


class Student(User):
    result = 0

    def type(self):
        student_essay = input("Hello Student. \nPlease type your essay: ")

        self.calculate(student_essay)

    def calculate(self, student_essay):
        e1 = Essay()

        e1.sentence = len(student_essay.split(".")) - 1

        e1.word = len(student_essay.split(" "))

        self.result = e1.word / e1.sentence

        print(self.result)

    def display(self):
        print("Average number of words in your essay is: " + str(self.result))