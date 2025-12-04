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

root=Tk()
root.title('문제2')
root.geometry('400x220')

label1=Label(root, text="반려동물을 선택하고 '말하기'를 누르세요.", font=('맑은 고딕',12))
label1.pack(pady=10)

frame1=Frame(root)
frame1.pack()

choice=IntVar()

DogRadio=Radiobutton(frame1, text='강아지 선택', variable=choice, value=1)
DogRadio.pack(side='left', padx=10, pady=10)

CatRadio=Radiobutton(frame1, text='고양이 선택', variable=choice, value=2)
CatRadio.pack(side='left', padx=10, pady=10)

def show_speak():
    if choice.get()==1:
        person.pet=Dog('dog1')

    elif choice.get()==2:
        person.pet=Cat('cat1')

    else:
        label2.config(text='동물을 선택하세요.')
        return

    sound=person.pet.speak()
    label2.config(text=f'{person.name}의 반려동물 → {sound}')

frame2=Frame(root)
frame2.pack(pady=10)

SpeakButton=Button(frame2, text='말하기', command=show_speak)
SpeakButton.pack()

label2=Label(root, text='', font=('맑은 고딕', 12), fg='blue')
label2.pack()

root.mainloop()