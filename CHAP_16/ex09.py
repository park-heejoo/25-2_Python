#Bouncing Ball Game(공과 패들이 만남)
from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas=canvas
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.paddle=paddle
        self.canvas.move(self.id,245,100)

        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)

        self.x=starts[0]
        self.y=-3

        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width() #수정

    #추가: 공이 패들에 부딪혔는지 검사하는 함수
    def hit_paddle(self, pos):
        paddle_pos=self.canvas.coords(self.paddle.id) #패들의 위치 [px1,py1,px2,py2]

        #가로 방향으로 공과 패들이 겹치는지 확인
        if pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2]: #공의 아래쪽(y2)이 패들의 위아래 사이에 있는지 확인
            if pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos=self.canvas.coords(self.id) #현재 공의 위치 가져오기 [x1,y1,x2,y2]
        #print(self.canvas.coords(self.id))

        if pos[0]<=0:
            self.x=3

        if pos[1]<=0:
            self.y=1

        if pos[2]>self.canvas_width:
            self.x=-3

        if pos[3]>=self.canvas_height:
            self.y=-1
        #추가: 패들과 부딪혔는지 검사
        if self.hit_paddle(pos)==True:
            self.y=-3
        
        if pos[0]<=0:
            self.x=3
        
        if pos[2]>=self.canvas_width:
            self.x=-3

class Paddle:
    def __init__(self, canvas, color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)

        self.x=0
        self.canvas_width=self.canvas.winfo_width()
        
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self, evt):
        self.x=-2

    def turn_right(self, evt):
        self.x=2
    
    def draw(self):
        self.canvas.move(self.id, self.x,0)
        pos=self.canvas.coords(self.id)

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

paddle=Paddle(canvas, 'blue') #수정-패들 먼저 생성해야함
ball=Ball(canvas, paddle, 'red') #수정

while True:
    ball.draw()
    paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)