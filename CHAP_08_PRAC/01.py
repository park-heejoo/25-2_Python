import tkinter as tk
import random

class MovingShapeApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Moving Shape App")

        # 캔버스 생성
        self.canvas = tk.Canvas(self.root, width=600, height=600, bg="white")
        self.canvas.pack()

        # 원
        self.shape = self.canvas.create_oval(100, 100, 200, 200, fill="blue")

        # 키보드 이벤트
        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

        # 마우스 이벤트
        self.canvas.bind("<B1-Motion>", self.change_color)

        # 루프 시작
        self.root.mainloop()

    # 이동 매서드
    def move_shape(self, dx, dy):
        self.canvas.move(self.shape, dx, dy)

    def move_up(self, event):
        self.canvas.move(self.shape, 0, -10)  # y좌표 -10 (위로 이동)

    def move_down(self, event):
        self.canvas.move(self.shape, 0, 10)   # y좌표 +10 (아래로 이동)

    def move_left(self, event):
        self.canvas.move(self.shape, -10, 0)  # x좌표 -10 (왼쪽으로 이동)

    def move_right(self, event):
        self.canvas.move(self.shape, 10, 0)   # x좌표 +10 (오른쪽으로 이동)

    #색 변경
    def change_color(self, event):
        colors = ["red", "green", "blue", "yellow", "purple", "orange"]
        color = random.choice(colors)
        self.canvas.itemconfig(self.shape, fill=color)  # 색상 변경

app = MovingShapeApp()
root.mainloop()
