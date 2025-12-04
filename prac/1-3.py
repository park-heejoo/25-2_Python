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
root.geometry('420x320')
choice=IntVar()

label1=Label(root, text="주행시킬 차량을 선택하고 '모두 주행'을 누르세요.", font=('맑은 고딕',12))
label1.pack(pady=10)

frame=Frame(root)
frame.pack()

def show_drive():
    messages = []

    if car_check.get()==1:
        messages.append(car.drive())

    if truck_check.get()==1:
        messages.append(truck.drive())

    if len(messages) == 0:
        result.set('선택된 차량이 없습니다.')

    else:
        # 줄바꿈으로 이어 붙이기
        result.set('\n'.join(messages))

car_check = IntVar()
truck_check = IntVar()

CarButton=Checkbutton(frame, text='자동차', variable=car_check)
CarButton.pack(side='left', padx=10)

TruckButton=Checkbutton(frame, text='트럭', variable=truck_check)
TruckButton.pack(side='left', padx=10)

b=Button(root, text='모두 주행', command=show_drive)
b.pack(pady=5)

result=StringVar(value='')
label2=Label(root, textvariable=result, font=('맑은 고딕',11))
label2.pack(pady=10)

root.mainloop()