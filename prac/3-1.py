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
root.geometry('320x240')
root.title('문제3-1')

w=Canvas(root, width=300, height=200, bg='white')
w.pack()

label=Label(root, text='도형을 선택하고 그리기를 누르세요')
label.pack()

frame1=Frame(root)
frame1.pack()

def draw_rectangle():
    w.delete('all')
    shape=Rectangle(50,50,100,60)
    shape.draw(w)
    label.config(text=f'면적={shape.area():.2f}, 둘레={shape.perimeter():.2f}')

def draw_circle():
    w.delete('all')
    shape=Circle(150,110,40)
    shape.draw(w)
    label.config(text=f'면적={shape.area():.2f}, 둘레={shape.perimeter():.2f}')

def delete():
    w.delete('all')
    label.config(text='도형이 없습니다.')

b1=Button(root, text='사각형 그리기', command=draw_rectangle)
b1.pack(side='left', padx=10)

b2=Button(root, text='원 그리기', command=draw_circle)
b2.pack(side='left', padx=10)

b3=Button(root, text='지우기', command=delete)
b3.pack(side='left', padx=10)

root.mainloop()