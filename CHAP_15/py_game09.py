#9. Sprite 클래스 & 그룹(중급 기본기)
import pygame

print('pygame 초기화 전')

pygame.init()
print('pygame 초기화 완료')

WIDTH, HEIGHT=600,400
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Step 9')

clock=pygame.time.Clock() #FPS 제어 준비

#추가: Sprite 클래스 정의
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #원래 사용하던 이미지 로드 부분을 여기로 이동
        #img=pygame.image.load('dukbird.png')
        #img=pygame.transform.scale(img, (150,150))
        self.image=pygame.image.load('dukbird.png') #캐릭터 이미지
        self.image=pygame.transform.scale(self.image, (100,100)) #크기 조정
        self.rect=self.image.get_rect()
        self.rect.center=(WIDTH//2, HEIGHT//2)
        self.speed=3

    def update(self): #Sprite의 동작 정의: 키 입력에 따라 위치 변경
        keys=pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x-=self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x+=self.speed
        if keys[pygame.K_UP]:
            self.rect.y-=self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y+=self.speed

        #화면 경계 제한
        self.rect.clamp_ip(screen.get_rect())

#추가: Sprite 그룹 생성 및 Player 추가
all_sprites=pygame.sprite.Group()
player=Player()
all_sprites.add(player)

running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    all_sprites.update() #추가: Sprite 그룹 업데이트 (Player.update() 자동 호출)


    #그림 그리기 영역
    screen.fill((170,200,255))
    pygame.draw.rect(screen, (80,170,80),(0,HEIGHT-60,WIDTH,60))
    pygame.draw.rect(screen, (250,80,80),(50,280,40,60))
    pygame.draw.circle(screen, (0,255,0),(450,150),20)
    pygame.draw.line(screen, (0,0,0),(300,300),(500,300),5)

    #(기존 코드) 이미지 직접 blit
    #screen.blit(img, rect)

    all_sprites.draw(screen) #추가: Sprite 그룹 그리기(Player 포함)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print('pygame 종료 완료')