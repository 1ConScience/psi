import pygame
from pygame.locals import *
import sys
import random
 
pygame.init()

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

camera = pygame.math.Vector2((0, 0))
vec = pygame.math.Vector2 #2 for two dimensional
 
WIDTH = 800
HEIGHT = 600
ACC = 0.5
#FRIC = -0.12
FRIC = -0.09
FPS = 60
 
FramePerSec = pygame.time.Clock()
 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("psi")


my_font = pygame.font.SysFont('Times New Roman', 30)

image_droite = pygame.image.load("e.png").convert_alpha()
image_gauche = pygame.image.load("e_inv.png").convert_alpha()
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = image_droite
        self.rect = self.surf.get_rect()
   
        self.pos = vec((27, 360))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False
 
    def move(self,gauche,droite):
        self.acc = vec(0,0.5)
                
        if gauche:
            self.acc.x = -ACC
            self.surf = image_gauche
        if droite:
            self.acc.x = ACC
            self.surf = image_droite
                 
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
        self.pos = vec((27, 360))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False
 
    def test_portes(self):
        hits = pygame.sprite.spritecollide(self ,portes, False)
        if hits:
            pygame.quit()
            sys.exit()
 
 
class Platform(pygame.sprite.Sprite):
    def __init__(self,size,color,pos):
        super().__init__()
        self.surf = pygame.Surface(size)
        self.surf.fill(color)
        self.rect = self.surf.get_rect(center = pos)

    def move(self,gauche,droite):
        pass


class Porte(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.surf = pygame.Surface((16, 60))
        self.surf.fill((0,255,26))
        self.rect = self.surf.get_rect(center = pos)

    def move(self,gauche,droite):
        pass    


class Texte(pygame.sprite.Sprite):
    def __init__(self,txt,x,y,color):
        super().__init__()
        self.surf = my_font.render(txt, False, color)
        self.rect = self.surf.get_rect(center = (x, y))
    def move(self,gauche,droite):
        pass



all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
portes = pygame.sprite.Group()



P1 = Player()
all_sprites.add(P1)

spanw_txt = Texte("†",27, 360,(255, 255, 255))
all_sprites.add(spanw_txt)


PT0 = Platform((100, 20),(43,255,255),(-100, HEIGHT+200))
all_sprites.add(PT0)
platforms.add(PT0)

drug_txt = Texte("C'est une drogue",-150, HEIGHT+300,(255, 255, 255))
all_sprites.add(drug_txt)

for i in range(272):
    PT = Platform(((WIDTH/30), 15),(255,255,255),((WIDTH/30)*i, HEIGHT - 5*i))
    all_sprites.add(PT)
    platforms.add(PT)


def tree(x,y,profondeur):
    profondeur+=1
    if profondeur < 7 :
        plat = Platform(((WIDTH/30), 15),(255,255,255),(x, y))
        all_sprites.add(plat)
        platforms.add(plat)
        tree(x-50, y+200,profondeur)
        tree(x+50, y+200,profondeur)

tree(-200, HEIGHT+400,0)

PT01 = Platform((100, 20),(43,255,255),(-200, 2200))
all_sprites.add(PT01)
platforms.add(PT01)

tout_en_bas_txt = Texte("?",-200, 2100,(255, 255, 255))
all_sprites.add(tout_en_bas_txt)

mid_txt = Texte("J'ai compté, il y en a 272",3650, -250,(255, 255, 255))
all_sprites.add(mid_txt)

fin_escalier_droite_txt = Texte("Je te sens perplexe Epsilon",7300, -800,(255, 255, 255))
all_sprites.add(fin_escalier_droite_txt)



check_haut_escalier = False
check_bas_derniere_platform = False
new_bas_last_plat_added = False
new_haut_escalier_added = False

gauche = False
droite = False

deadzone = 0.3

while True:

    #quand P1 entre en collision avec platforms
    P1.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                gauche = True
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                droite = True  
            if event.key == pygame.K_SPACE or event.key == pygame.K_z or event.key == pygame.K_UP:
                P1.jump()
        if event.type == pygame.KEYUP:   
            if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                gauche = False
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                droite = False 
            if event.key == pygame.K_SPACE or event.key == pygame.K_z or event.key == pygame.K_UP:
                P1.cancel_jump()

        if event.type == pygame.JOYBUTTONDOWN:      
            if  event.button == 4:
                gauche = True
            if  event.button == 5:
                droite = True  
            if  event.button == 0:
                P1.jump()
        if event.type == pygame.JOYBUTTONUP:      
            if  event.button == 4:
                gauche = False
            if  event.button == 5:
                droite = False 
            if  event.button == 0:
                P1.cancel_jump()

        if pygame.joystick.get_count()>0:
            axis_pos = joysticks[0].get_axis(0)

            if axis_pos < -1 * deadzone:
                gauche = True
            elif axis_pos > deadzone:
                droite = True  
            else:
                gauche = False
                droite = False 

    #fond noir
    screen.fill((0,0,0))

    #ajust camera
    camera.x = P1.pos.x - WIDTH / 2
    camera.y = P1.pos.y - HEIGHT / 2
     
    #deplacer les sprites 
    for entity in all_sprites:
        entity.move(gauche,droite)
        screen.blit(entity.surf, (entity.rect.x - camera.x, entity.rect.y - camera.y))

    if (P1.rect.y - camera.y) > HEIGHT:
        P1.into_the_void()

    

    if P1.pos.x>7100 and not new_bas_last_plat_added:
        check_haut_escalier = True
        if check_bas_derniere_platform:
            tout_en_bas_txt.kill()
            tout_en_bas_txt = Texte("Tiens ton susucre :)",-200, 2100,(255, 255, 255))
            all_sprites.add(tout_en_bas_txt)

            PTNEXT = Platform((1000, 20),(255,255,255),(-800, 2350))
            all_sprites.add(PTNEXT)
            platforms.add(PTNEXT)

            porte1 = Porte((-1292, 2310))
            all_sprites.add(porte1)
            portes.add(porte1)

            new_bas_last_plat_added = True

    if P1.pos.y>2190 and P1.pos.x<1100 and not new_haut_escalier_added:
        check_bas_derniere_platform = True
        if check_haut_escalier:
            fin_escalier_droite_txt.kill()
            fin_escalier_droite_txt = Texte("Quoi ? Non, je ne me joue pas de toi :)",7300, -800,(255, 255, 255))
            all_sprites.add(fin_escalier_droite_txt)

            PTNEXT2 = Platform((1000, 20),(43,255,255),(7800, -900))
            all_sprites.add(PTNEXT2)
            platforms.add(PTNEXT2)

            porte2 = Porte((8293, -940))
            all_sprites.add(porte2)
            portes.add(porte2)

            new_haut_escalier_added = True

    P1.test_portes()

    pygame.display.update()
    FramePerSec.tick(FPS)