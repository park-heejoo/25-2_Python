from tkinter import *

class Person:
    def __init__(self, name):
        self.name=name

class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.classes=[]

    def enrollCourse(self, subject):
        self.classes = [subject] 

    def clearCourses(self):
        self.classes.clear()

s=Student('홍길동')

root=Tk()
root.geometry('380x280')
root.title('문제4-1')

label1=Label(root, text=f'학생: {s.name}', font=('맑은 고딕',12, 'bold'))
label1.pack(pady=10)

frame1=Frame(root)
frame1.pack()

choice=IntVar()

b1=Radiobutton(frame1, text='Python', variable=choice, value=1)
b1.pack(side='left')

b2=Radiobutton(frame1, text='AI', variable=choice, value=2)
b2.pack(side='left')

b3=Radiobutton(frame1, text='DataScience', variable=choice, value=3)
b3.pack(side='left')

label2=Label(root, text='과목을 선택하고 [등록하기]를 누르세요.')
label2.pack(pady=10)

def show_selected():
    if choice.get()==1:
        s.enrollCourse('Python')
    elif choice.get()==2:
        s.enrollCourse('AI')
    elif choice.get()==3:
        s.enrollCourse('DataScience')
    
    label2.config(text='등록된 과목: '+','.join(s.classes))

def clearbutton():
    choice.set(0)

    s.clearCourses()

    label2.config(text='대표 과목이 없습니다.')

frame2=Frame(root)
frame2.pack()

button1=Button(frame2, text='대표 과목 등록', command=show_selected)
button1.pack(side='left', padx=10)

button2=Button(frame2, text='초기화', command=clearbutton)
button2.pack(side='left', padx=10)



root.mainloop()