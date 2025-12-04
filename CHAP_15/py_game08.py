#8. 프레임 속도(FPS) 제어
import pygame

print('pygame 초기화 전')

pygame.init()
print('pygame 초기화 완료')

WIDTH, HEIGHT=600,400
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Step 8')

clock=pygame.time.Clock() #FPS 제어 준비

img=pygame.image.load('dukbird.png') #캐릭터 이미지
img=pygame.transform.scale(img, (150,150)) #크기 조절
rect=img.get_rect()
rect.center=(WIDTH//2, HEIGHT//2)

speed=3
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

    #실시간 키 입력
    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        rect.x-=speed
    if keys[pygame.K_RIGHT]:
        rect.x+=speed
    if keys[pygame.K_UP]:
        rect.y-=speed
    if keys[pygame.K_DOWN]:
        rect.y+=speed

    #화면 경계 제한
    rect.clamp_ip(screen.get_rect()) #추가: Rect의 내장기능 사용(더 깔끔!)

    #추가: 화면 그리기(Drawing) 영역
    screen.fill((170,200,255)) #추가: 파란 하늘 느낌 배경

    pygame.draw.rect(screen, (80,170,80),(0,HEIGHT-60,WIDTH,60)) #추가: 바닥(땅) 그리기
    pygame.draw.rect(screen, (250,80,80),(50,280,40,60)) #추가: 빨간 박스(아이템처럼 보이게)
    pygame.draw.circle(screen, (0,255,0),(450,150),20) #추가: 초록 원(코인 느낌)
    pygame.draw.line(screen, (0,0,0),(300,300),(500,300),5) #추가: 검은 선(장애물 느낌)

    screen.blit(img, rect)
    pygame.display.flip()
    
    clock.tick(60) #추가: 60 FPS

pygame.quit()
print('pygame 종료 완료')