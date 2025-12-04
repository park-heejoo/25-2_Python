import math
from tkinter import *

class Shape:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def area(self):
        pass

    def perimeter(self):
        pass

    def draw(self, canvas):
        pass

class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w=w
        self.h=h

    def area(self):
        return self.w*self.h
    
    def perimeter(self):
        return 2*(self.w+self.h)
    
    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + self.w, self.y + self.h, fill="tomato", outline="black")

class Circle(Shape):
    def __init__(self, x,y,r):
        super().__init__(x, y)
        self.r=r

    def area(self):
        return math.pi*self.r**2
    
    def perimeter(self):
        return 2*math.pi*self.r
    
    def draw(self, canvas):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill="skyblue", outline="black")

root=Tk()
root.geometry('320x300')
root.title('문제3-2')

canvas=Canvas(root, width=300, height=200, bg='white')
canvas.pack()

label=Label(root, text='도형을 선택하고 그리기를 누르세요')
label.pack()

frame1=Frame(root)
frame1.pack()

rect_check=IntVar()
cir_check=IntVar()

r1=Checkbutton(frame1, text='사각형', variable=rect_check)
r1.pack(side='left')
c1=Checkbutton(frame1, text='원', variable=cir_check)
c1.pack(side='left')

import random

def draw_shape():
    canvas.delete('all')
    total_area = 0
    total_perimeter = 0

    if rect_check.get() == 1:
        x = random.randint(10, 200)
        y = random.randint(10, 120)
        w = random.randint(40, 120)
        h = random.randint(30, 100)

        rect = Rectangle(x, y, w, h)
        rect.draw(canvas)
        total_area += rect.area()
        total_perimeter += rect.perimeter()

    if cir_check.get() == 1:
        x = random.randint(40, 260)
        y = random.randint(40, 160)
        r = random.randint(20, 60)

        cir = Circle(x, y, r)
        cir.draw(canvas)
        total_area += cir.area()
        total_perimeter += cir.perimeter()

    if total_area==0:
        label.config(text="도형을 선택하세요.")
    
    else:
        label.config(text=f'총 면적={total_area:.2f}, 총 둘레={total_perimeter:.2f}')

button=Button(root, text='그리기', command=draw_shape).pack(pady=10)

root.mainloop()