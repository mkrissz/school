from base_human import Human

class Student(Human):
    def __init__(self,name, width, height, depth, icon, age, voice, myclass):
        super().__init__(name, width, height, depth, icon, age, voice)
        self.myclass = myclass