import pygame, random

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption('Cuckold Adventures')

WINDOW_SIZE = (800, 700)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
SPEED = 0 
GAME_SPEED = 8 
DOGGO_GAP = 100
audio_jump = pygame.mixer.Sound('audio/Jump.wav')

play = 0

class Corno(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.img_run = [pygame.transform.scale(pygame.image.load('img/run1.png').convert_alpha(), (76, 125)),
                       pygame.transform.scale(pygame.image.load('img/run1.png').convert_alpha(), (76, 125)),
                       pygame.transform.scale(pygame.image.load('img/run1.png').convert_alpha(), (76, 125)),
                       pygame.transform.scale(pygame.image.load('img/run2.png').convert_alpha(), (76, 125)),
                       pygame.transform.scale(pygame.image.load('img/run2.png').convert_alpha(), (76, 125)),
                       pygame.transform.scale(pygame.image.load('img/run2.png').convert_alpha(), (76, 125)),
                       pygame.transform.scale(pygame.image.load('img/run3.png').convert_alpha(), (76, 125)),
                       pygame.transform.scale(pygame.image.load('img/run3.png').convert_alpha(), (76, 125)),
                       pygame.transform.scale(pygame.image.load('img/run3.png').convert_alpha(), (76, 125)),
                       pygame.transform.scale(pygame.image.load('img/run4.png').convert_alpha(), (76, 125)),
                       pygame.transform.scale(pygame.image.load('img/run4.png').convert_alpha(), (76, 125)),
                       pygame.transform.scale(pygame.image.load('img/run4.png').convert_alpha(), (76, 125)),
                       pygame.transform.scale(pygame.image.load('img/run5.png').convert_alpha(), (76, 125)),
                       pygame.transform.scale(pygame.image.load('img/run5.png').convert_alpha(), (76, 125)),
                       pygame.transform.scale(pygame.image.load('img/run5.png').convert_alpha(), (76, 125)),
                       pygame.transform.scale(pygame.image.load('img/run6.png').convert_alpha(), (76, 125)),
                       pygame.transform.scale(pygame.image.load('img/run6.png').convert_alpha(), (76, 125)),
                       pygame.transform.scale(pygame.image.load('img/run6.png').convert_alpha(), (76, 125))]

        self.img_jmp = [pygame.transform.scale(pygame.image.load('img/jmp4.png').convert_alpha(), (70, 90)),
                       pygame.transform.scale(pygame.image.load('img/jmp4.png').convert_alpha(), (70, 90)),
                       pygame.transform.scale(pygame.image.load('img/jmp4.png').convert_alpha(), (70, 90)),
                       pygame.transform.scale(pygame.image.load('img/jmp5.png').convert_alpha(), (70, 90)),
                       pygame.transform.scale(pygame.image.load('img/jmp5.png').convert_alpha(), (70, 90)),
                       pygame.transform.scale(pygame.image.load('img/jmp5.png').convert_alpha(), (70, 90)),
                       pygame.transform.scale(pygame.image.load('img/jmp6.png').convert_alpha(), (70, 90)),
                       pygame.transform.scale(pygame.image.load('img/jmp6.png').convert_alpha(), (70, 90)),
                       pygame.transform.scale(pygame.image.load('img/jmp6.png').convert_alpha(), (70, 90)),
                       pygame.transform.scale(pygame.image.load('img/jmp7.png').convert_alpha(), (70, 90)),
                       pygame.transform.scale(pygame.image.load('img/jmp7.png').convert_alpha(), (70, 90)),
                       pygame.transform.scale(pygame.image.load('img/jmp7.png').convert_alpha(), (70, 90)),
                       pygame.transform.scale(pygame.image.load('img/jmp8.png').convert_alpha(), (70, 90)),
                       pygame.transform.scale(pygame.image.load('img/jmp8.png').convert_alpha(), (70, 90)),
                       pygame.transform.scale(pygame.image.load('img/jmp8.png').convert_alpha(), (70, 90)),
                       pygame.transform.scale(pygame.image.load('img/jmp9.png').convert_alpha(), (70, 90)),
                       pygame.transform.scale(pygame.image.load('img/jmp9.png').convert_alpha(), (70, 90)),
                       pygame.transform.scale(pygame.image.load('img/jmp9.png').convert_alpha(), (70, 90))]

        self.speed = SPEED

        self.current_image = 0

        self.image = pygame.image.load('img/run1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 500*3/10
        self.rect[1] = 550

    def update(self):
        if self.rect[1] == 550:
            self.current_image = (self.current_image + 1) % 18
            self.image = self.img_run[ self.current_image ]
        else:
            self.current_image = (self.current_image + 1) % 18
            self.image = self.img_jmp[ self.current_image ]


        self.rect[1] += self.speed
        if self.rect[1] < 550:
            self.speed += 2
        if self.rect[1] >= 550:
            self.rect[1] = 550
            self.speed = 0


    def jump(self):
        
        if self.rect[1] == 550:
            self.speed = -30
            
        
class Ground(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/bkg3.png')
        self.image = pygame.transform.scale(self.image, (2*800, 500))

        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = 200
    def update(self):
        self.rect[0] -= GAME_SPEED

class Ground2(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/bkg2.png')
        self.image = pygame.transform.scale(self.image, (2*800, 500))

        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = 80
    def update(self):
        self.rect[0] -= 4

class Ground3(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/bkg1.png')
        self.image = pygame.transform.scale(self.image, (2*800, 500))

        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = 0
    def update(self):
        self.rect[0] -= 2


def is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])



class Doggo(pygame.sprite.Sprite):
    def __init__(self, xpos):
        pygame.sprite.Sprite.__init__(self)
        
        self.doggo = [pygame.transform.scale(pygame.image.load('img/doggo1.png').convert_alpha(), (200, 125)),
                    pygame.transform.scale(pygame.image.load('img/doggo1.png').convert_alpha(), (200, 125)),
                    pygame.transform.scale(pygame.image.load('img/doggo1.png').convert_alpha(), (200, 125)),
                    pygame.transform.scale(pygame.image.load('img/doggo2.png').convert_alpha(), (200, 125)),
                    pygame.transform.scale(pygame.image.load('img/doggo2.png').convert_alpha(), (200, 125)),
                    pygame.transform.scale(pygame.image.load('img/doggo2.png').convert_alpha(), (200, 125)),
                    pygame.transform.scale(pygame.image.load('img/doggo3.png').convert_alpha(), (200, 125)),
                    pygame.transform.scale(pygame.image.load('img/doggo3.png').convert_alpha(), (200, 125)),
                    pygame.transform.scale(pygame.image.load('img/doggo3.png').convert_alpha(), (200, 125)),
                    pygame.transform.scale(pygame.image.load('img/doggo4.png').convert_alpha(), (200, 125)),
                    pygame.transform.scale(pygame.image.load('img/doggo4.png').convert_alpha(), (200, 125)),
                    pygame.transform.scale(pygame.image.load('img/doggo4.png').convert_alpha(), (200, 125)),
                    pygame.transform.scale(pygame.image.load('img/doggo5.png').convert_alpha(), (200, 125)),
                    pygame.transform.scale(pygame.image.load('img/doggo5.png').convert_alpha(), (200, 125)),
                    pygame.transform.scale(pygame.image.load('img/doggo5.png').convert_alpha(), (200, 125))]

        self.current_image = 0

        self.image = pygame.image.load('img/doggo1.png').convert_alpha()

        self.rect = self.image.get_rect()
        self.rect[0] = random.randint(700, 900)
        self.rect[1] = 550

    def update(self):
        self.current_image = (self.current_image + 1) % 15
        self.image = self.doggo[ self.current_image ]        
        self.rect[0] -= 20
        if self.rect[0] <= -200:
            self.rect[0] = random.randint(700, 1100)

class GamoOver(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.go = [pygame.transform.scale(pygame.image.load('img/go.png').convert_alpha(), (200, 125))]
        self.image = pygame.image.load('img/go.png').convert_alpha()
        self.rect = self.image.get_rect()
    def update(self):
        self.rect[0] = 300
        self.rect[1] = 300

SPACE = pygame.image.load('img/space.png')
SPACE = pygame.transform.scale(SPACE, (200, 75))
CRED = pygame.image.load('img/cred.png')
CRED = pygame.transform.scale(CRED, (200, 75))
LOGO = pygame.image.load('img/go.png')
LOGO = pygame.transform.scale(LOGO, (600, 200))
BACKGROUND1 = pygame.image.load('img/bkg1.png')
BACKGROUND1 = pygame.transform.scale(BACKGROUND1, (800, 700))
BACKGROUND2 = pygame.image.load('img/bkg2.png')
BACKGROUND2 = pygame.transform.scale(BACKGROUND2, (800, 700))
BACKGROUND3 = pygame.image.load('img/bkg3.png')
BACKGROUND3 = pygame.transform.scale(BACKGROUND3, (800, 500))
GOVER = pygame.image.load('img/gover.png')
GOVER = pygame.transform.scale(GOVER, (800, 250))
CREDITOS = pygame.image.load('img/creditos.png')
CREDITOS = pygame.transform.scale(CREDITOS, (800, 700))




corno_group = pygame.sprite.Group()
corno = Corno()
corno_group.add(corno)

go_group = pygame.sprite.Group()
game_over = GamoOver()
go_group.add(game_over)

ground_group = pygame.sprite.Group()
for i in range(2):
    ground = Ground((2*800*i)+20)
    ground_group.add(ground)

ground_group2 = pygame.sprite.Group()
for i in range(2):
    ground2 = Ground2((2*800*i)+20)
    ground_group2.add(ground2)

ground_group3 = pygame.sprite.Group()
for i in range(2):
    ground3 = Ground3((2*800*i)+20)
    ground_group3.add(ground3)

doggo_group = pygame.sprite.Group()
doggo = Doggo(random.randint(700, 800))
doggo_group.add(doggo)


while play == 0:
    screen.blit(BACKGROUND1, (0, 0))
    screen.blit(BACKGROUND2, (0, 0))
    screen.blit(BACKGROUND3, (0, 200))
    screen.blit(LOGO, (80, 100))
    screen.blit(SPACE, (300, 350))
    screen.blit(CRED, (300, 450))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                play = 1
    pygame.display.update()
    clock.tick(50)
while play == 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                corno.jump()



    if is_off_screen(ground_group.sprites()[0]):
        ground_group.remove(ground_group.sprites()[0])
        new_ground = Ground(2*800*i - 20)
        ground_group.add(new_ground)
    
    if is_off_screen(ground_group2.sprites()[0]):
        ground_group2.remove(ground_group2.sprites()[0])
        new_ground2 = Ground2(2*800*i - 20)
        ground_group2.add(new_ground2)

    if is_off_screen(ground_group3.sprites()[0]):
        ground_group3.remove(ground_group3.sprites()[0])
        new_ground3 = Ground3(2*800*i - 20)
        ground_group3.add(new_ground3)


    corno_group.update()
    ground_group.update()
    doggo_group.update()
    go_group.update()
    ground_group2.update()
    ground_group3.update()

    ground_group3.draw(screen)
    ground_group2.draw(screen)
    ground_group.draw(screen)
    corno_group.draw(screen)
    doggo_group.draw(screen)

    pygame.display.update()
    clock.tick(50)

    if pygame.sprite.groupcollide(corno_group, doggo_group, False, False, pygame.sprite.collide_mask): 
        play = 2 
        while play == 2:
            screen.blit(GOVER, (0, 185))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        pygame.quit()
            pygame.display.update()
            clock.tick(50) 

        