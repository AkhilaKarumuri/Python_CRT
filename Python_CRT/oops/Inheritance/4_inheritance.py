class Graduation:
    def __init__(self):
        pass
    @staticmethod
    def Graduate():
        print("Congratulations you are a graduate now")
#first sub class
class CSE(Graduation):
    # def __init__(self):
    #     super().__init__()
    @staticmethod
    def Graduate():
        print("Congratulations you are a CSE graduate")
class ECE(Graduation):
    @staticmethod
    def Graduate():
        print("Congratulations you are an ECE graduate now")
Graduation.Graduate()
CSE.Graduate()
ECE.Graduate()