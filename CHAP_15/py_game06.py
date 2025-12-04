#6. Surface와 Rect(이미지 적용 버전)
import pygame

print('pygame 초기화 전')

pygame.init()
print('pygame 초기화 완료')

WIDTH, HEIGHT=600,400
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Step 6 - 이미지로 변경')

screen.fill((255,255,255))
pygame.display.flip()

pygame.time.delay(2000)

#사용자 이미지 로드
img=pygame.image.load('dukbird.png') #여기에 파일 이름 입력! (png, jpg 등)
img=pygame.transform.scale(img, (150,150)) #크기 조절 (원하면)
rect=img.get_rect()
rect.center=(WIDTH//2, HEIGHT//2)

speed=1

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
    if rect.left<0:
        rect.left=0
    if rect.right> WIDTH:
        rect.right=WIDTH
    if rect.top<0:
        rect.top=0
    if rect.bottom>HEIGHT:
        rect.bottom=HEIGHT

    screen.fill((200,200,200))
    screen.blit(img, rect) #네모 대신 이미지 그리기
    pygame.display.flip()
    
pygame.quit()
print('pygame 종료 완료')