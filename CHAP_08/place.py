from tkinter import*

root=Tk()
root.geometry("300x100")

button1=Button(root, text="버튼 1", bg="red", fg="white")
button1.grid(row=0, column=0)

button2=Button(root, text="버튼 2", bg="green", fg="black")
button2.grid(row=30, column=30)

button3=Button(root, text="버튼 3", bg="blue", fg="white")
button3.grid(row=60, column=60)

root.mainloop()