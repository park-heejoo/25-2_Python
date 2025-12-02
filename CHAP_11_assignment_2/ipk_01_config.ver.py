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
root.title('문제1')
root.geometry('400x300')

label1=Label(root, text='버튼을 눌러보세요.', font=('맑은 고딕',12))
label1.pack(pady=10)

frame=Frame(root)
frame.pack()

def show_car():
    label2.config(text=car.drive())

def show_truck():
    label2.config(text=truck.drive())

CarButton=Button(frame, text='자동차 주행', command=show_car)
CarButton.pack(side='left', padx=10)

TruckButton=Button(frame, text='트럭 주행', command=show_truck)
TruckButton.pack(side='left', padx=10)

label2=Label(root, text='', font=('맑은 고딕',11))
label2.pack(pady=10)

root.mainloop()