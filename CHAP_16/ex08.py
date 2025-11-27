#Bouncing Ball Game(패들 추가)
from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, color):
        self.canvas=canvas
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)

        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)

        self.x=starts[0]
        self.y=-3

        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos=self.canvas.coords(self.id)
        #print(self.canvas.coords(self.id))

        if pos[0]<=0:
            self.x=3

        if pos[1]<=0:
            self.y=1

        if pos[2]>self.canvas_width:
            self.x=-3

        if pos[3]>=self.canvas_height:
            self.y=-1

class Paddle: #패들 클래스 추가
    def __init__(self, canvas, color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)

        self.x=0 #처음에는 안 움직임
        self.canvas_width=self.canvas.winfo_width() #너비를 저장하고 있기(벽에 부딪히면 처리하기 위해서)
        
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left) #키보드 이벤트 연결
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self, evt):
        self.x=-2 #왼쪽으로 이동 속도

    def turn_right(self, evt):
        self.x=2 #오른쪽으로 이동 속도
    
    def draw(self): #패들을 x방향으로만 이동
        self.canvas.move(self.id, self.x,0)
        pos=self.canvas.coords(self.id)

        #화면 왼쪽/오른쪽 끝을 넘지 않게 막기
        if pos[0]<=0:
            self.x=0
        elif pos[2]>=self.canvas_width:
            self.x=0


tk=Tk()
tk.title('Game')
tk.resizable(0,0)
tk.wm_attributes('-topmost',1)

canvas=Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

ball=Ball(canvas,'red')
paddle=Paddle(canvas, 'blue') #추가

while True:
    ball.draw()
    paddle.draw() #추가
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)