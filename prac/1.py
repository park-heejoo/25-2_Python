class Pet:
    def speak(self):
        return '...'

class Dog(Pet):
    def __init__(self, name):
        self.name=name

    def speak(self):
        return '멍멍'
    
class Cat(Pet):
    def __init__(self, name):
        self.name=name


    def speak(self):
        return '야옹!'
    
class Person:
    def __init__(self, name, pet=None):
        self.name=name
        self.pet=pet

person=Person('홍길동')

from tkinter import *

root=Tk()
root.title('문제2')
root.geometry('400x200')

label1=Label(root, text='동물을 선택해 주세요.').pack()

frame1=Frame(root)
frame1.pack()

def select_dog():
    person.pet=Dog('dog1')
    result.set('강아지를 선택했습니다.')

def select_cat():
    person.pet=Cat('cat1')
    result.set('고양이를 선택했습니다.')

def pet_speak():
    result.set(f'{person.name}의 반려동물->{person.pet.speak()}')

b1=Button(frame1, text='강아지 선택', command=select_dog)
b1.pack(side='left', padx=10)

b2=Button(frame1, text='고양이 선택', command=select_cat)
b2.pack(side='left', padx=10)

b3=Button(root, text='말하기', command=pet_speak)
b3.pack(pady=10)

result=StringVar()
label2=Label(root, textvariable=result)
label2.pack()

root.mainloop()