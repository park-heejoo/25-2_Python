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
    
class Bus(Vehicle):
    def __init__(self, name):
        super().__init__(name)

    def drive(self):
        return f'버슥 {self.name}가 승객을 태우고 주행합니다.'

car=Car('car1')
truck=Truck('truck1')
bus=Bus('bus1')

root=Tk()
root.title('문제1-2')
root.geometry('400x300')

label1=Label(root, text='버튼을 눌러 차량을 주행시키세요.', font=('맑은 고딕',12))
label1.pack(pady=10)

frame=Frame(root)
frame.pack()

count={'car':0, 'truck':0, 'bus':0}

def update_count():
    count_text.set(f'자동차: {count["car"]}회, 트럭: {count["truck"]}회, 버스: {count["bus"]}회')

def show_car():
    count['car'] += 1
    result.set(car.drive())
    update_count()

def show_truck():
    count['truck'] += 1
    result.set(truck.drive())
    update_count()

def show_bus():
    count['bus'] += 1
    result.set(bus.drive())
    update_count()

CarButton=Button(frame, text='자동차 주행', command=show_car)
CarButton.pack(side='left', padx=10)

TruckButton=Button(frame, text='트럭 주행', command=show_truck)
TruckButton.pack(side='left', padx=10)

BusButton=Button(frame, text='버스 주행', command=show_bus)
BusButton.pack(side='left',padx=10)

result=StringVar(value='')
label2=Label(root, textvariable=result, font=('맑은 고딕',11))
label2.pack(pady=10)

count_text=StringVar(value='자동차: 0회, 트럭: 0회, 버스: 0회')
label3=Label(root, textvariable=count_text, font=('맑은 고딕',11))
label3.pack(pady=10)


root.mainloop()