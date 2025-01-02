import pygame
from pygame.locals import *
import sys
import random
 
pygame.init()

camera = pygame.math.Vector2((0, 0))
vec = pygame.math.Vector2 #2 for two dimensional
 
WIDTH = 800
HEIGHT = 600
ACC = 0.5
FRIC = -0.12
FPS = 60
 
FramePerSec = pygame.time.Clock()
 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("psi")
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        #self.image = pygame.image.load("character.png")
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()
   
        self.pos = vec((27, 360))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False
 
    def move(self):
        self.acc = vec(0,0.5)
    
        pressed_keys = pygame.key.get_pressed()
                
        if pressed_keys[K_LEFT] or pressed_keys[K_q]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            self.acc.x = ACC
                 
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
             
        #le carré blanc sera positionné par rapport à son mid en x et son bottom en y     
        self.rect.midbottom = self.pos
 
    def jump(self): 
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and not self.jumping:
           self.jumping = True
           self.vel.y = -15
 
    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3
 
    def update(self):
        hits = pygame.sprite.spritecollide(self ,platforms, False)
        if self.vel.y > 0:        
            if hits:
                if self.pos.y < hits[0].rect.bottom:               
                    self.pos.y = hits[0].rect.top +1
                    self.vel.y = 0
                    self.jumping = False

    def into_the_void(self):
        self.pos.y = 0
 
 
class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
    def move(self):
        pass






all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()

P1 = Player()
all_sprites.add(P1)

PT0 = platform()
PT0.surf = pygame.Surface((100, 20))
PT0.surf.fill((43,255,255))
PT0.rect = PT0.surf.get_rect(center = (-100, HEIGHT+200))
all_sprites.add(PT0)
platforms.add(PT0)

PT01 = platform()
PT01.surf = pygame.Surface((100, 20))
PT01.surf.fill((255,255,255))
PT01.rect = PT01.surf.get_rect(center = (-200, HEIGHT+400))
all_sprites.add(PT01)
platforms.add(PT01)


for i in range(272):
    PT = platform()
    PT.surf = pygame.Surface(((WIDTH/30), 15))
    PT.surf.fill((255,255,255))
    PT.rect = PT.surf.get_rect(center = ((WIDTH/30)*i, HEIGHT - 5*i))

    all_sprites.add(PT)
    platforms.add(PT)


pygame.font.init()
my_font = pygame.font.SysFont(None, 30)
text_surface = my_font.render("C'est une drogue", False, (255, 255, 255))


while True:

    #quand P1 entre en collision avec platforms
    P1.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE or event.key == pygame.K_z or event.key == pygame.K_UP:
                P1.jump()
        if event.type == pygame.KEYUP:    
            if event.key == pygame.K_SPACE or event.key == pygame.K_z or event.key == pygame.K_UP:
                P1.cancel_jump()

    #fond noir
    screen.fill((0,0,0))
    screen.blit(text_surface, (0,0))

    #ajust cam
    camera.x = P1.pos.x - WIDTH / 2
    camera.y = P1.pos.y - HEIGHT / 2
     
    #deplacer les sprites 
    for entity in all_sprites:
        entity.move()
        screen.blit(entity.surf, (entity.rect.x - camera.x, entity.rect.y - camera.y))

    if (P1.rect.y - camera.y) > HEIGHT:
        P1.into_the_void()

    pygame.display.update()
    FramePerSec.tick(FPS)
