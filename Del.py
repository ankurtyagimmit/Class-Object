class Student:
    def __init__(self,name,course,sex,E_roll_no,mail):
        self.name=name
        self.course=course
        self.sex=sex
        self.E_roll_no=E_roll_no
        self.mail=mail
S=Student("Ankur","BCA","Male",2105420298,"abc@gmail.com")


del S.sex
print("Student Details:")
print("Name:",S.name)
print("Course:",S.course)

print("Enrollment No.:",S.E_roll_no)
print("Email:",S.mail)
print("Sex:",S.sex)
        
