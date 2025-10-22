from tkinter import *

def show_selection():
    selected = listbox.get(ACTIVE)  # 현재 선택된 항목 가져오기
    label.config(text=f"선택한 과일: {selected}")

root = Tk()
root.title("Listbox 예시")

# ① 리스트박스 생성
listbox = Listbox(root, height=5)
listbox.pack(pady=10)

# ② 항목 추가
fruits = ["사과", "바나나", "포도", "복숭아", "딸기"]
for fruit in fruits:
    listbox.insert(END, fruit)

# ③ 버튼 클릭 시 선택 확인
Button(root, text="선택 확인", command=show_selection).pack()

# ④ 선택 결과를 표시할 레이블
label = Label(root, text="선택한 과일 없음")
label.pack(pady=5)

root.mainloop()