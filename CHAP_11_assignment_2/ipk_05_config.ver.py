class Pet:
    def __init__(self, name):
        self.name=name

    def speak(self):
        return '...'
    
class Dog(Pet):
    def speak(self):
        return '멍멍!'
    
class Cat(Pet):
    def speak(self):
        return '야옹!'
    
class Person:
    def __init__(self, name, pet=None):
        self.name=name
        self.pet=pet

from tkinter import *

root=Tk()
root.geometry('700x300')
root.title('반려동물 등록하기')

person=Person('홍길동')

petName=StringVar()
kind=IntVar(value=0)
vaccine=IntVar(value=0)
neuter=IntVar(value=0)

frame1=Frame(root)
frame1.pack()

label2=Label(frame1, text='반려동물 이름:')
label2.grid(row=0, column=0, sticky='e', pady=5)

entry=Entry(frame1, textvariable=petName)
entry.grid(row=0, column=1, padx=10)

label3=Label(frame1, text='종류:')
label3.grid(row=1, column=0, sticky='e', pady=5)

dog=Radiobutton(frame1, text='강아지', variable=kind, value=1)
dog.grid(row=1, column=1, sticky='w', padx=10)

cat=Radiobutton(frame1, text='고양이', variable=kind, value=2)
cat.grid(row=1, column=2, sticky='w')

label4=Label(frame1, text='옵션:')
label4.grid(row=2, column=0, sticky='e', pady=5)

check1=Checkbutton(frame1, text='예방접종 완료', variable=vaccine)
check1.grid(row=2, column=1, sticky='w', padx=10)

check2=Checkbutton(frame1, text='중성화 완료', variable=neuter)
check2.grid(row=2, column=2, sticky='w')

frame2=Frame(root)
frame2.pack()

label3=Label(root, text='', font=('맑은 고딕', 10),fg='blue', justify='left')
label3.pack(pady=10)

def register():
    name=petName.get()
    if not name:
        name='이름없음'

    kind_val=kind.get()
    if kind_val==1:
        pet=Dog(name)
        kind_str='강아지'

    elif kind_val==2:
        pet=Cat(name)
        kind_str='고양이'

    else:
        label3.config(text='동물 종류를 선택하세요!')
        return

    person.pet=pet
    sound=pet.speak()

    vacc_result='O' if vaccine.get()==1 else 'X'
    neuter_result='O' if neuter.get()==1 else 'X'

    msg=(
        f'{person.name}의 반려동물 등록 완료!\n'
        f'이름: {pet.name} ({kind_str})\n'
        f'소리: {sound}\n'
        f'예방접종: {vacc_result}, 중성화: {neuter_result}'
    )
    label3.config(text=msg)

frame3=Frame(root)
frame3.pack(pady=10)

b1=Button(frame3, text='등록하기', padx=15, command=register)
b1.pack(side='left', padx=15)

def clearbutton():
    petName.set('')
    kind.set(0)
    vaccine.set(0)
    neuter.set(0)
    label3.config(text='')

b2=Button(frame3, text='초기화', padx=15, command=clearbutton)
b2.pack(side='left', padx=15)

root.mainloop()