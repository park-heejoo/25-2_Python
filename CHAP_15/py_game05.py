#1. pygame 초기화&종료
import pygame

print('pygame 초기화 전')

pygame.init()
print('pygame 초기화 완료')

#2. 화면(디스플레이) 만들기
WIDTH, HEIGHT=600,400
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Step 5')

screen.fill((255,255,255))
pygame.display.flip()

pygame.time.delay(2000)

#이동 테스트용 좌표
x,y=WIDTH//2, HEIGHT//2
speed=1
size=40 #네모 크기

#3. 게임 루프(Game Loop)의 구조
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            print('KEYDOWN:', event.key)

        if event.type==pygame.KEYUP:
            print('KEYUP:', event.key)

        if event.type==pygame.MOUSEBUTTONDOWN:
            print('Mouse Click:', event.pos)

    #5. 실시간 키 입력(get_pressed)
    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x-=speed
    if keys[pygame.K_RIGHT]:
        x+=speed
    if keys[pygame.K_UP]:
        y-=speed
    if keys[pygame.K_DOWN]:
        y+=speed

    #(중요) 화면 경계 안으로만 이동하도록 제한
    if x<0:
        x=0
    if x> WIDTH -size:
        x=WIDTH-size
    if y<0:
        y=0
    if y>HEIGHT-size:
        y=HEIGHT-size

    screen.fill((200,200,200))
    pygame.draw.rect(screen, (0,0,225),(x,y,size, size))

    pygame.display.flip()
    
pygame.quit()
print('pygame 종료 완료')