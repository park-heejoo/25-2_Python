from tkinter import*

def click(key):
    if key=='=':
        try:
            result=eval(entry.get())
            entry.delete(0, END)
            entry.insert(END, str(result))
        except:
            entry.insert(END, "오류!")
    elif key=='C':
        entry.delete(0, END)
    else:
        entry.insert(END, key)

root=Tk()
root.title("간단한 계산기")