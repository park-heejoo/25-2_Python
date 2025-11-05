from tkinter import*

class Book():
    def __init__(self, title, author):
        self.title=title
        self.author=author
        self.borrowed=False

    def borrow(self):
        if self.borrowed==False:
            self.borrowed=True
            return f'{self.title}이(가) 대출되었습니다.', 'blue'
        else:
            return f'{self.title}은(는) 이미 대출 중입니다.', 'red'
        
    def return_book(self):
        if self.borrowed==True:
            self.borrowed=False
            return f'{self.title}이(가) 반납되었습니다.', 'green'
        
        else:
           return f'{self.title}은(는) 대출되지 않은 상태입니다.', 'red'

def borrow_book():
    t=titleEntry.get()
    a=authorEntry.get()
    b=Book(t,a)
    msg,color=b.borrow()
    bottom_Label.config(text=msg, fg=color)

def return_book():
    t=titleEntry.get()
    a=authorEntry.get()
    b=Book(t,a)
    msg,color=b.return_book()
    bottom_Label.config(text=msg, fg=color)

root=Tk()
root.title('도서 대출 관리 프로그램')
root.geometry('300x200')

top_frame=Frame(root)
top_frame.pack()

titleLabel=Label(top_frame, text='도서 대출 관리 시스템', font=('맑은 고딕',14), width=200, height=2)
titleLabel.pack()

middle_frame=Frame(root)
middle_frame.pack()

title=Label(middle_frame, text='제목:', height=2)
title.grid(row=0, column=0)

author=Label(middle_frame, text='저자:', height=2)
author.grid(row=1, column=0)

titleEntry=Entry(middle_frame)
titleEntry.grid(row=0, column=1)

authorEntry=Entry(middle_frame)
authorEntry.grid(row=1, column=1)

bottom_frame=Frame(root)
bottom_frame.pack()

b1=Button(bottom_frame, text='대출', width=7, command=borrow_book)
b1.pack(side='left', padx=10)

b2=Button(bottom_frame, text='반납', width=7, command=return_book)
b2.pack(side='left', padx=10)

bottom_Label=Label(root, text='', height=3)
bottom_Label.pack()

root.mainloop()