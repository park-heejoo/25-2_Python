from tkinter import*
from tkinter.messagebox import showinfo

root=Tk()
root.geometry("400x400")
root.title="중간고사 4번"
choice=IntVar()

w=Canvas(root, width=300, height=200)
w.pack()

def rectangle():
    w.create_rectangle(10,10,50,50, fill="red")

def oval():
    w.create_oval(10,10,50,50,fill="blue")

def text():
    w.create_text(200, 100, text="Hello Duksung", fill="blue", font=(30,'bold'))

Radiobutton(root, text="사각형",padx=20, variable=choice,
            value=1, command=rectangle).pack(side="left")
Radiobutton(root, text="원", padx=20, variable=choice,
            value=2, command=oval).pack(side="left")
Radiobutton(root, text="텍스트", padx=20, variable=choice,
            value=3, command=text).pack(side="left")

button=Button(root, text="그리기")
button.bind("<Button-1>", w.delete("all"))
button.pack()


root.mainloop()