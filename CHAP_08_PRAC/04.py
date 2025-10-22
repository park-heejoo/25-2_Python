import tkinter as tk
import random
import time

def animate_text(canvas, text_id):
    for i in range(10):
        update_text_size(canvas, text_id)
        update_text_color(canvas, text_id)
        canvas.update()
        time.sleep(0.5)

def update_text_size(canvas, text_id):
    current_size=100
    new_size=current_size+random.randint(-100, 100)
    canvas.itemconfig(text_id, font=("Helvetica", new_size))

def update_text_color(canvas, text_id):
    colors=["red", "orange", "yellow", "green", "blue", "purple", "magenta", "cyan"]
    new_color = random.choice(colors)
    canvas.itemconfig(text_id, fill=new_color)

# 초기 설정
root = tk.Tk()
root.title("Text Animation")

canvas = tk.Canvas(root, width=600, height=300)
canvas.pack()

text_id = canvas.create_text(200, 100, text="Hello", font=("Helvetica", 12), fill="black")

# 애니메이션 실행
animate_text(canvas, text_id)   # 10번 반복 기본값

root.mainloop()