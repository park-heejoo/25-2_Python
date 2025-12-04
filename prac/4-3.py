from tkinter import *

class Person:
    def __init__(self, name):
        self.name=name

class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.classes=[]
        

    def enrollCourse(self, subject):
        self.classes.append(subject)

    def clearCourses(self):
        self.classes.clear()

class Teacher(Person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject=subject
        self.teachers=[]

    def enroll(self, teacher):
        self.teachers.append(teacher)

s=Student('홍길동')
t1=Teacher('박교수', 'Python')
t2=Teacher('김교수', 'AI')
t3=Teacher('이교수', 'DataScience')

root=Tk()
root.geometry('380x280')
root.title('문제4-3')

label1=Label(root, text=f'학생: {s.name}', font=('맑은 고딕',12, 'bold'))
label1.pack(pady=10)

label4=Label(root, text=f'담당교수: {t.name}', font=('맑은 고딕',12, 'bold'))
label4.pack(pady=10)

frame1=Frame(root)
frame1.pack()

class1=IntVar()
class2=IntVar()
class3=IntVar()

checkbutton1=Checkbutton(frame1, text='Python', variable=class1)
checkbutton1.pack(side='left')

checkbutton2=Checkbutton(frame1, text='AI', variable=class2)
checkbutton2.pack(side='left')

checkbutton3=Checkbutton(frame1, text='DataScience', variable=class3)
checkbutton3.pack(side='left')

label2=Label(root, text='과목을 선택하고 [등록하기]를 누르세요.')
label2.pack(pady=10)

label3=Label(root, text='')
label3.pack()

def show_selected():
    #아무 것도 선택 안 한 경우를 먼저 처리해야
    if class1.get()==0 and class2.get()==0 and class3.get()==0:
        label2.config(text='과목이 선택되지 않았습니다.')
        return #여기서 함수 끝

    if class1.get()==1:
        if 'Python' not in s.classes:
            s.enrollCourse('Python')
            s.enroll(t1)

    if class2.get()==1:
        if 'AI' not in s.classes:
            s.enrollCourse('AI')
    
    if class3.get()==1:
        if 'DataScience' not in s.classes:
            s.enrollCourse('DataScience')
    
    label2.config(text='등록된 과목: '+','.join(s.classes))
    label3.config(text='등록된 과목: '+','.join(s.teachers))

def clearbutton():
    class1.set(0)
    class2.set(0)
    class3.set(0)

    s.clearCourses()

    label2.config(text='모든 선택을 해제했습니다.')

frame2=Frame(root)
frame2.pack()

button1=Button(frame2, text='등록하기', command=show_selected)
button1.pack(side='left', padx=10)

button2=Button(frame2, text='초기화', command=clearbutton)
button2.pack(side='left', padx=10)

root.mainloop()