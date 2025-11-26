with open('file1.txt', 'r', encoding='utf-8') as f1:
    text1=f1.read()

with open('file2.txt', 'r', encoding='utf-8') as f2:
    text2=f2.read()

with open('outfile.txt','w',encoding='utf-8') as out:
    out.write(text1)
    out.write('\n')
    out.write(text2)