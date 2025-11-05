from tkinter import *

class Book:
    def __init__(self, title, author):
        self.title=title
        self.author=author
        self.borrowed=True

    def info(self):
        return f"{self.title} ({self.author})"

borrowed_books = []

def update_borrowed_list():
    if len(borrowed_books) == 0:
        borrowed_Label.config(text="현재 대출 중인 책 없음")
    else:
        text = " / ".join([book.info() for book in borrowed_books])
        borrowed_Label.config(text=text)

def borrow_book():
    t = titleEntry.get().strip()
    a = authorEntry.get().strip()

    if t == "" or a == "":
        bottom_Label.config(text="제목과 저자를 입력하세요.", fg="red")
        return

    for book in borrowed_books:
        if book.title == t and book.author == a:
            bottom_Label.config(text=f"『{t}』은(는) 이미 대출 중입니다.", fg="red")
            return

    new_book = Book(t, a)
    borrowed_books.append(new_book)

    bottom_Label.config(text=f"『{t}』이(가) 대출되었습니다.", fg="blue")
    update_borrowed_list()


def return_book():
    t = titleEntry.get().strip()
    a = authorEntry.get().strip()

    if t == "" or a == "":
        bottom_Label.config(text="제목과 저자를 입력하세요.", fg="red")
        return

    for book in borrowed_books:
        if book.title == t and book.author == a:
            borrowed_books.remove(book)
            bottom_Label.config(text=f"『{t}』이(가) 반납되었습니다.", fg="green")
            update_borrowed_list()
            return

    bottom_Label.config(text=f"『{t}』은(는) 대출 목록에 없습니다.", fg="red")

root = Tk()
root.title("도서 대출 관리 프로그램 v2")
root.geometry("430x280")

titleLabel = Label(root, text="도서 대출 관리 시스템", font=("맑은 고딕", 16))
titleLabel.pack(pady=5)

middle_frame = Frame(root)
middle_frame.pack()

Label(middle_frame, text="제목:", width=8, anchor="e").grid(row=0, column=0, pady=5)
Label(middle_frame, text="저자:", width=8, anchor="e").grid(row=1, column=0, pady=5)

titleEntry = Entry(middle_frame, width=30)
authorEntry = Entry(middle_frame, width=30)
titleEntry.grid(row=0, column=1, pady=5)
authorEntry.grid(row=1, column=1, pady=5)

btn_frame = Frame(root)
btn_frame.pack(pady=7)

Button(btn_frame, text="대출", width=10, command=borrow_book).pack(side="left", padx=10)
Button(btn_frame, text="반납", width=10, command=return_book).pack(side="left", padx=10)

bottom_Label = Label(root, text="", font=("맑은 고딕", 12), height=2)
bottom_Label.pack()

borrowed_Label = Label(root, text="현재 대출 중인 책 없음", font=("맑은 고딕", 11), fg="navy")
borrowed_Label.pack()

root.mainloop()