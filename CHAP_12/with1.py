with open('proverbs.txt','r') as file:
    for line in file:
        print(line.strip())

#with 블록을 빠져나오면 파일이 자동으로 닫힘