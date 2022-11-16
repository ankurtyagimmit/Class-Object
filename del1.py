class Student:
    def __init__(self, name, course,sex):
        self.name=name
        self.course=course
        self.sex=sex
    def show(self):
        print("Details of Student:")
        print("Name:",self.name)
        print("course:",self.course)
        print("sex:",self.sex)
S=Student("Ankur","BCA",'Mail\n')
S1=Student("Pappu","B.Sc",'Mail')
S.show()

#print("\nAfter ching details of student:")

S1.show()
del S1
print()
S.show()
S1.show()



