filename=input('파일명을 입력하세요: ').strip()
word=input('검색 문자열을 입력하세요: ').strip()

with open(filename, 'r', encoding='utf-8') as f:
    content=f.read()
    count=content.count(word)

print(f"'{word}'(은)는 파일 내에서 {count}번 나타납니다.")