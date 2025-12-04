#1. pygame 초기화&종료
import pygame

print('pygame 초기화 전')

pygame.init()
print('pygame 초기화 완료')

pygame.quit()


#2. 화면(디스플레이) 만들기
WIDTH, HEIGHT=600,400
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Step 3')

screen.fill((255,255,255))
pygame.display.flip()

pygame.time.delay(2000)

#3. 게임 루프(Game Loop)의 구조
running=True
while running: #아직 이벤트는 자세히 다루지 않고, QUIT만 처리
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    #(나중에: 업데이트 로직 들어갈 자리)
    #(나중에: 그리기 로직 들어갈 자리)

    screen.fill((200,200,200))

    #게임 업데이트, 화면 그리기
    pygame.display.flip()
    
pygame.quit()
print('pygame 종료 완료')