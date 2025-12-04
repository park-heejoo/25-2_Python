from tkinter import *

class Pet:
    def speak(self):
        return '...'
    
class Dog(Pet):
    def __init__(self, name):
        self.name=name

    def speak(self):
        return '멍멍!'
    
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

def select_dog():
    person.pet=Dog('dog1')
    label2.config(text='강아지를 선택했습니다.')

def select_cat():
    person.pet=Cat('cat1')
    label2.config(text='고양이를 선택했습니다.')

def delete_pet():
    person.pet=None
    label2.config(text='반려동물을 등록해 주세요.')

def show_speak():
    if person.pet is None:
        label2.config(text='반려동물이 없습니다.')

    sound=person.pet.speak()
    label2.config(text=f'{person.name}의 반려동물 → {sound}')

root=Tk()
root.title('문제2-3')
root.geometry('400x230')

label1=Label(root, text="동물을 선택하고 '말하기'를 누르세요", font=('맑은 고딕',12))
label1.pack(pady=10)

frame1=Frame(root)
frame1.pack()

DogButton=Button(frame1, text='강아지 선택', command=select_dog)
DogButton.pack(side='left', padx=10, pady=10)

CatButton=Button(frame1, text='고양이 선택', command=select_cat)
CatButton.pack(side='left', padx=10, pady=10)

frame2=Frame(root)
frame2.pack(pady=10)

SpeakButton=Button(frame2, text='말하기', command=show_speak)
SpeakButton.pack()

DeleteButton=Button(frame2, text='반려동물 삭제', command=delete_pet)
DeleteButton.pack()

label2=Label(root, text='', font=('맑은 고딕', 12), fg='blue')
label2.pack()

root.mainloop()