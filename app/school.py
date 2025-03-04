from human.base_teacher import Teacher  # Tanár osztály importálása
from human.base_student import Student  # Diák osztály importálása
import random  # Véletlenszerű értékek generálásához
import time  # Időkezeléshez 
import datetime  # Dátumkezeléshez 

class School:
    """
    Az iskola osztálya, amely tartalmazza az iskola besorolását, osztálytermeket
    és az iskola maximális kapacitását.
    """
    def __init__(self, school_classification, classroom, capacity):
        self.school_classification = school_classification  # Pl.: általános iskola, középiskola
        self.classroom = classroom  # Osztálytermek listája vagy objektuma
        self.school_classes = 8  # Rögzített érték: az iskola 8 osztályos
        self.capacity = capacity  # Az iskola maximális befogadóképessége

class ClassRoom:
    """
    Az osztályterem objektum, amely az osztályok kapacitását és a diákokat tárolja.
    """
    def __init__(self, capacity=32):
        self.capacity = capacity  # Egy osztály maximális létszáma
        self.classroom = []  # Az osztályok listája

    def make_classroom(self):
        """
        Létrehozza a 8 osztályt, mindegyiket egy üres listával reprezentálva.
        """
        for i in range(1, 9):
            self.classroom.append([])

class Teacher(Teacher):  # Hiba! A Teacher osztály már öröklődik önmagából, de nincs konstruktor.
    """
    A tanár osztály, amely egy adott tantárgyat tanít.
    """
    def __init__(self, name, age, sex, subject):  # Hiányzott a subject paraméter!
        super().__init__(name, age, sex)  # Az ősosztály inicializálása
        self.subject = subject  # A tanár tantárgya

class SchoolStudent(Student):
    """
    Az iskolai diák osztály, amely örököl a Student osztályból.
    """
    def __init__(self, name, age, sex, myclass):
        super().__init__(name, age, sex, myclass)  # Az ősosztály inicializálása

    def make_student(self, name, age, sex):
        """
        Véletlenszerűen kiválaszt egy nevet a diák nemének megfelelő listából.
        """
        if self.sex == 'male':
            self.name = random.choice(self.male_names)  # Fiú nevek közül választ
        else:
            self.name = random.choice(self.female_names)  # Lány nevek közül választ
        return self.name

    def witch_class(self):
        """
        A diák életkora alapján meghatározza, melyik osztályba tartozik.
        (6 éves kortól 13 éves korig, így 1-8. osztály)
        """
        for age in range(6, 14):
            if self.age == age:
                self.myclass = age - 5  # Pl. egy 6 éves az 1. osztályba kerül
        return self.myclass

# === Diákok generálása ===
scool_students = []  # Helyes név: school_students lenne!

for _ in range(random.randint(20, 30)):  # Véletlenszerű számú diák generálása
    age = random.randint(6, 13)  # 6 és 13 év közötti életkor
    sex = random.choice(['male', 'female'])  # Nem kiválasztása
    student = SchoolStudent("", age, sex, None)  # Új diák létrehozása üres névvel
    student_class = student.witch_class()  # Osztály meghatározása
    student_name = student.make_student('name', 'age', 'sex')  # Véletlen név generálása
    scool_students.append({"name": student_name, "age": age, "sex": sex, "class": student_class})  # Diák hozzáadása a listához

# === Osztálytermek létrehozása ===
classrooms = ClassRoom()
classrooms.make_classroom()  # Létrehozza a 8 osztályt (üres listákat)

# === Diákok hozzárendelése az osztályokhoz ===
for student in scool_students:
    student_class = student["class"]  # Az osztály sorszáma
    classrooms.classroom[student_class - 1].append(student)  # A megfelelő osztályhoz adja a diákot

# === Osztályok és diákjaik kiírása ===
for index, class_list in enumerate(classrooms.classroom, start=1):
    print(f"Class {index}:")  # Osztály száma
    for student in class_list:
        print(f"  Name: {student['name']}, Age: {student['age']}, Sex: {student['sex']}")  # Diák adatai
    print()  # Üres sor az osztályok között.
