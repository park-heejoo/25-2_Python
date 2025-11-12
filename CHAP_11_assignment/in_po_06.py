from tkinter import *

class Animal:
    def speak(self):
        return '알 수 없음'

class Dog(Animal):
    def speak(self):
        return '멍멍!'

class Cat(Animal):
    def speak(self):
        return '야옹!'

class Duck(Animal):
    def speak(self):
        return '꽥꽥!'
    
def make_sound(animal):
    sound=animal.speak()
    result_label.config(text=sound)
    
root=Tk()
root.title('동물 소리 듣기')
root.geometry('350x200')

top_frame=Frame(root)
top_frame.pack()

label=Label(top_frame, text='동물 버튼을 눌러 소리를 들어보세요.', height=2)
label.pack()

middle_frame=Frame(root)
middle_frame.pack()

b1=Button(middle_frame, text='강아지', width=10, command=lambda:make_sound(Dog()))
b1.pack(side='left', padx=10)
b2=Button(middle_frame, text='고양이', width=10, command=lambda:make_sound(Cat()))
b2.pack(side='left', padx=10)
b3=Button(middle_frame, text='오리', width=10, command=lambda:make_sound(Duck()))
b3.pack(side='left', padx=10)

bottom_frame=Frame(root)
bottom_frame.pack()

result_label=Label(bottom_frame, text='(여기에 울음소리가 나옵니다)', font=('맑은 고딕',14,'bold'), width=200, height=2)
result_label.pack()

root.mainloop()