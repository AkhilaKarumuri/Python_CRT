class Grandfather():
    def __init__(self):
        pass
    #method overriding
    @staticmethod
    def Properties():
        print("100 Acres of land")
class Father(Grandfather):
    def __init__(self):
        super().__init__()
    @staticmethod
    def Properties():
        print("50 acres of land")
class son(Father):
    def __init__(self):
        super().__init__()
    @staticmethod
    def Properties():
        print("Job")
Grandfather.Properties()
Father.Properties()
son.Properties()