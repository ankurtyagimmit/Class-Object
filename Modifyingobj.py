class Student:
    def __init__(self, name, course,E_Roll_No, mail):
        self.name=name
        self.course=course
        self.E_Roll_No=E_Roll_No
        self.mail=mail

    def show(self):
        print("Student Details:")
        print("Name:",self.name)
        print("course:",self.course)
        print("Enrollment No.:",self.E_Roll_No)
        print("mail:", self.mail)
    

s=Student("Ankur","BCA",2105420298,"abc@gmail.com")
s.show()

print("\n*****Modification Details*****")
s=Student("Ankur","BBA",2105420288,"xyz@gmail.com")
s.show()
