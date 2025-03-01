from human.base_teacher import Teacher
from human.base_student import Student
import random
import time
import datetime

class School:
    def __init__(self, school_classification, classroom,capacity):
        self.school_classification = school_classification
        self.classroom = classroom
        self.school_classes = 8
        self.capacity = capacity
        self.current_members_in_school = []
        
class ClassRoom:
    def __init__(self, capacity = 32):
        self.capacity = capacity
        self.current_students_number = []
        
    def add_students(self):
        for _ in range(random.randint(20, 31)):
            random_number = random.randint(20,31)
            self.current_students_number.append(random_number)
    
class Teacher(Teacher):
    def __init__(self, name, width, height, depth, icon, age, voice, subject):
        self.subject = subject
    
class Student(Student):
    def __init__(self, name, width, height, depth, icon, age, voice, subject, knowledge):
        self.knowledge = knowledge
        

# current_time = time.time()
# readable_time = time.ctime(current_time)

school_class = []
students_in_school = 0

for i in range(1,9):
    school_class.append(i)  
    student_in_class = ClassRoom()
    student_in_class.add_students()
    print (f'Member of Class {i}: {len(student_in_class.current_students_number)}')
    students_in_school += len(student_in_class.current_students_number)
    
print(f'Now {students_in_school} students are in the school.')