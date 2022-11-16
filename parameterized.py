class MyAge:
    def __init__(self, Age):
        self.Age=Age
    def Velid(self, user_age):
        if user_age>=self.Age:
            print("You are Eligible for voting.")
        else:
            print("You are not Eligible for voting.")
V=MyAge(17)
V.Velid(17)


V=MyAge(18)
V.Velid(17)

        
    
