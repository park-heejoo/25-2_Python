class Vehicle:
    def __init__(self, name):
        self.name=name
    
    def drive(self):
        pass

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
    
car=Car('car1')
truck=Truck('truck1')

def car_select():
    result.set(car.drive())

def truck_select():
    result.set(truck.drive())

from tkinter import *

root=Tk()
root.geometry('400x300')
root.title('문제1')

label1=Label(root, text='버튼을 눌러보세요.', font=('맑은 고딕', 12))
label1.pack(pady=10)

frame1=Frame(root)
frame1.pack()

b1=Button(frame1, text='자동차 주행', command=car_select)
b1.pack(side='left', padx=10)
b2=Button(frame1, text='트럭 주행', command=truck_select)
b2.pack(side='left', padx=10)

result=StringVar(value=' ')
label2=Label(root, textvariable=result, font=('맑은 고딕', 12))
label2.pack(pady=10)

root.mainloop()
