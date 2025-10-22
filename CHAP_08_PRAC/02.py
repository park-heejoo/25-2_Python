import tkinter as tk
from PIL import ImageTk, Image
import os

BASE_DIR=os.path.dirname(os.path.abspath(__file__))

def update_image():
    global current_index
    
    image_path=os.path.join(BASE_DIR, image_files[current_index])
    
    #이미지 열기
    image=Image.open(image_path)

    #크기 조정
    image = image.resize((400, 300))
    
    #Tkinter용 PhotoImage 객체로 변환
    photo=ImageTk.PhotoImage(image)

    #Label 위젯에 이미지 표시
    image_label.config(image=photo)
    image_label.image=photo

    #다음 이미지 인덱스로 이동(마지막이면 0으로 돌아감)
    current_index = (current_index + 1) % len(photos)
    root.after(interval, update_image)

# 초기 설정
root = tk.Tk()
root.title("Image Slider")

image_files = ["image1.png", "image2.png", "image3.png", "image4.png"]

interval = 2000  # 2초
current_index = 0

photos = []      # PhotoImage를 보관해 GC(가비지 컬렉션)로 사라지지 않게 함





# 이미지 미리 로드 (PNG/GIF 지원. JPG는 PIL 필요)
for f in image_files:
    photos.append(tk.PhotoImage(file=f))

image_label = tk.Label(root)
image_label.pack()

update_image()

root.mainloop()