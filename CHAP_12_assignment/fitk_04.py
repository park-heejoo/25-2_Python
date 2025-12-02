from tkinter import *

class Vehicle:
    def __init__(self, name):
        self.name=name

    def drive(self):
        print('NotImplementedError')

class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)

    def drive(self):
        return f'승용차 {self.name}가 주행합니다.'
    
class Truck(Vehicle):
    def __init__(self, name):
        super().__init__(name)

    def drive(self):
        return f'트럭 {self.name}가 화물을 싣고 주행합니다.'
    
def append_log(message):
    with open('drive_log.txt','a',encoding='utf-8') as f:
        f.write(message+'\n')

def clear_log_file():
    with open('drive_log.txt','w',encoding='utf-8') as f:
        f.write('') #파일 비우기


root=Tk()
root.title('문제4')
root.geometry('400x320')

label1=Label(root, text="차량 이름을 입력하세요:")
label1.pack(pady=10)

entry=Entry(root)
entry.pack()

result=StringVar(value='결과가 여기에 표시됩니다.')
label2=Label(root, textvariable=result)
label2.pack(pady=10)

car=entry.get().strip()
truck=entry.get().strip()

def drive_car():
    name=entry.get().strip()
    if name=='':
        name='이름없음'

    c=Car(name)
    message=c.drive()
    append_log(message)
    result.set(message)

def drive_truck():
    name=entry.get().strip()
    if name=='':
        name='이름없음'

    t=Truck(name)
    message=t.drive()
    append_log(message)
    result.set(message)

def clear_log():
    clear_log_file()
    result.set('로그 파일을 비웠습니다.')

b1=Button(root, text='자동차 주행', width=15, command=drive_car)
b1.pack(pady=5)

b2=Button(root, text='트럭 주행', width=15, command=drive_truck)
b2.pack()

b3=Button(text='로그 비우기', width=15, command=clear_log)
b3.pack(pady=5)

root.mainloop()