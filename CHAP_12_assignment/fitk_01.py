filename=input('파일명을 입력하세요: ')

try:
    with open(filename, 'r', encoding='utf-8') as file:
        content=file.read()
    print(content)
except FileNotFoundError:
    print('파일을 찾을 수 없습니다.')