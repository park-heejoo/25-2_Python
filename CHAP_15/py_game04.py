#1. pygame 초기화&종료
import pygame

print('pygame 초기화 전')

pygame.init()
print('pygame 초기화 완료')

#2. 화면(디스플레이) 만들기
WIDTH, HEIGHT=600,400
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Step 4')

screen.fill((255,255,255))
pygame.display.flip()

pygame.time.delay(2000)

#3. 게임 루프(Game Loop)의 구조
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: #창 닫기 버튼
            running=False

        if event.type==pygame.KEYDOWN: #키 눌림
            print('KEYDOWN:', event.key)

        if event.type==pygame.KEYUP: #키에서 손 뗌
            print('KEYUP:', event.key)

        if event.type==pygame.MOUSEBUTTONDOWN: #마우스 클릭
            print('Mouse Click:', event.pos)

        #(업데이트 로직이 들어갈 자리)
        #(그리기 로직 들어갈 자리)

        screen.fill((200,200,200))
        pygame.display.flip()
    
pygame.quit()
print('pygame 종료 완료')