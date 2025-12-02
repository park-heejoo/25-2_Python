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
root.geometry('300x300')
root.title('문제3')
choice=IntVar()

w=Canvas(root, width=300, height=200, bg='white')
w.pack()

label=Label(root, text='도형을 선택하고 그리기를 누르세요')
label.pack()

frame1=Frame(root)
frame1.pack()

RectangleRadio=Radiobutton(frame1, text='사각형', variable=choice, value=1)
RectangleRadio.pack(side='left')
CircleaRadio=Radiobutton(frame1, text='원', variable=choice, value=2)
CircleaRadio.pack(side='left')

def draw_shape():
    w.delete('all')

    sel=choice.get()
    if sel == 0:
        label.config(text="도형을 먼저 선택하세요!")
        return

    if sel==1:
        shape=Rectangle(50,50,100,60)
    elif sel==2:
        shape=Circle(150,110,40)
    
    shape.draw(w)
    label.config(text=f'면적={shape.area():.2f}, 둘레={shape.perimeter():.2f}')

button=Button(root, text='그리기', command=draw_shape).pack(pady=10)

root.mainloop()