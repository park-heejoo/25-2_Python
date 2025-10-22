from tkinter import*

root=Tk()
photo=PhotoImage(file="dog.png")
label=Label(root,image=photo)
label.pack()
root.mainloop()