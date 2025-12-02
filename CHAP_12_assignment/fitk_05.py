from tkinter import *
from tkinter import filedialog, messagebox

def count_stats(filename):
    spaces_cnt=0
    upper_cnt=0
    lower_cnt=0

    with open(filename,'r',encoding='utf-8') as f:
        for line in f:   
            for ch in line:
                if ch==' ': #스페이스 개수 세기
                    spaces_cnt+=1

                elif ch.isupper():
                    upper_cnt+=1
            
                elif ch.islower():
                    lower_cnt+=1

    return spaces_cnt, upper_cnt, lower_cnt

def select_file():
    filepath=filedialog.askopenfilename(#경로 추출+창 띄우기
        title='파일을 선택하세요',
        filetypes=[('텍스트 파일','*.txt'), ('모든 파일','*.*')] #파일 확장자 필터 설정 옵션
    )

    if not filepath: #사용자가 취소하면 종료
        return
    
    try:
        space_cnt, upper_cnt, lower_cnt=count_stats(filepath)

        label2.config(text=f'선택된 파일: {filepath}')
        label3.config(text=f'스페이스: {space_cnt}, 대문자: {upper_cnt}, 소문자: {lower_cnt}')

    except Exception as e:
        messagebox.showerror('에러', f'파일을 처리하는 중 오류가 발생했습니다.\n{e}') #{e}는 오류 내용 들어가는 자리


root=Tk()
root.title('문제5')
root.geometry('520x220')

label1=Label(root, text="텍스트 파일을 선택하여 스페이스, 대문자, 소문자 개수를 세어보세요.")
label1.pack(pady=10)

b=Button(root, text='파일 선택', command=select_file)
b.pack()

label2=Label(root, text='선택된 파일: (없음)')
label2.pack(pady=5)

label3=Label(root, text='스페이스: 0, 대문자: 0, 소문자: 0')
label3.pack(pady=10)

root.mainloop()