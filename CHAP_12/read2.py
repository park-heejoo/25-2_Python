infile=open('phones.txt','r',encoding='utf-8')
line=infile.readline()      # 첫 줄 읽기
while line !="":            # 빈 줄이 아닐 동안 반복
    print(line)             # 읽은 줄 출력
    line=infile.readline()  # 다음 줄 읽기
infile.close()