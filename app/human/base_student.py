from base_human import Human

class Student(Human):
    def __init__(self, name, age, sex, myclass):
        super().__init__(name, age, sex)
        self.myclass = myclass