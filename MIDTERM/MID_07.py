from tkinter import *

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("변형문제 3번")
        self.root.geometry("400x400")

        self.canvas = Canvas(root, width=400, height=250, bg="white")
        self.canvas.pack()

        self.choice = IntVar(value=1)
        frame = Frame(root)
        frame.pack(pady=10)
        Radiobutton(frame, text="사각형", variable=self.choice, value=1).pack(side=LEFT, padx=8)
        Radiobutton(frame, text="원", variable=self.choice, value=2).pack(side=LEFT, padx=8)
        Radiobutton(frame, text="이미지", variable=self.choice, value=4).pack(side=LEFT, padx=8)

        Button(root, text="그리기", command=self.draw, bg="lightgray").pack(pady=5)
        self.img = None

    def draw(self):
        self.canvas.delete("all")
        c = self.choice.get()

        if c == 1:
            self.canvas.create_rectangle(80, 80, 180, 180, fill="red")
        elif c == 2:
            self.canvas.create_oval(200, 80, 300, 180, fill="blue")

        elif c == 4:
            # 힌트 코드 적용: PhotoImage + 참조 유지
            self.img = PhotoImage(file="logo.png")
            self.canvas.create_image(200, 130, anchor=CENTER, image=self.img)

root = Tk()
DrawingApp(root)
root.mainloop()