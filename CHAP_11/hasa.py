#1. Dog is an Animal
class Animal:
    def move(self):
        print('동물이 움직입니다.')
    
class Dog(Animal):
    def __init__(self):
        self.animal=Animal()

    def move(self):
        self.animal.move()
        print('개가 달립니다.')

dog=Dog()
dog.move()


#2. Student is a Person
class Person:
    def speak(self):
        print('사람이 말을 합니다.')

class Student(Person):
    def __init__(self):
        self.person=Person()

    def study(self):
        self.person.speak()
        print('학생이 공부합니다.')

stu=Student()
stu.study()


#3. Car is a Vehicle
class Vehicle:
    def drive(self):
        print('차량이 이동 중입니다.')

class Car(Vehicle):
    def __init__(self):
        self.vehicle=Vehicle()

    def drive(self):
        super().drive()
        print('자동차가 도로를 달립니다.')

car=Car()
car.drive()