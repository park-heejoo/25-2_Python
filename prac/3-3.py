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

shapes=[Rectangle(50,50,100,60), Circle(150,110,40)]

root=Tk()
root.geometry('300x300')
root.title('문제3-3')

canvas=Canvas(root, width=300, height=200, bg='white')
canvas.pack()

label=Label(root, text='모두 그리기를 누르세요')
label.pack()

frame1=Frame(root)
frame1.pack()

def draw_shape():
    canvas.delete('all')

    total_area=0
    total_perimeter=0

    for s in shapes:
        s.draw(canvas)
        total_area += s.area()
        total_perimeter += s.perimeter()

    label.config(text=f'면적={total_area:.2f}, 둘레={total_perimeter:.2f}')

def delete_all():
    canvas.delete('all')
    label.config(text='도형이 없습니다.')

frame2=Frame(root)
frame2.pack()
b1=Button(frame2, text='모두 그리기', command=draw_shape)
b1.pack(side='left',pady=10, padx=10)
b2=Button(frame2, text='지우기', command=delete_all)
b2.pack(side='left',padx=10)

root.mainloop()