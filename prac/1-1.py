from tkinter import *

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

root=Tk()
root.title('문제1-1')
root.geometry('400x300')
choice=IntVar()

label1=Label(root, text="차량을 선택하고 '주행'을 누르세요.", font=('맑은 고딕',12))
label1.pack(pady=10)

frame=Frame(root)
frame.pack()

def show_drive():
    if choice.get()==1:
        result.set(car.drive())
    
    else:
        result.set(truck.drive())


CarRB=Radiobutton(frame, text='자동차', variable=choice, value=1)
CarRB.pack(side='left', padx=10)

TruckRB=Radiobutton(frame, text='트럭', variable=choice, value=2)
TruckRB.pack(side='left', padx=10)

button=Button(root, text='주행', command=show_drive)
button.pack()

result=StringVar(value='')
label2=Label(root, textvariable=result, font=('맑은 고딕',11))
label2.pack(pady=10)

root.mainloop()