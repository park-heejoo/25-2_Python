from tkinter import *

root = Tk()
root.geometry("300x200")

# 🔹 상단 프레임
top_frame = Frame(root, bg="lightblue")
top_frame.pack(fill="x")   # 가로로 꽉 채움

# 🔹 하단 프레임
bottom_frame = Frame(root, bg="lightgreen")
bottom_frame.pack(fill="both", expand=True)

# 🔸 상단 프레임 안에 버튼들
Button(top_frame, text="버튼 1").pack(side="left", padx=10, pady=5)
Button(top_frame, text="버튼 2").pack(side="left", padx=10, pady=5)

# 🔸 하단 프레임 안에 라벨
Label(bottom_frame, text="이건 하단 프레임에 들어있어요").pack()

root.mainloop()