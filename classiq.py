import pygame
from pygame.locals import *
import sys
import random
import glob
from pathlib import Path
import os
 
pygame.init()

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

camera = pygame.math.Vector2((0, 0))
vec = pygame.math.Vector2 #2 for two dimensional
 
WIDTH = 800
HEIGHT = 600
ACC = 0.5
FRIC = -0.09#-0.12
FPS = 60

deadzone = 0.3
 
FramePerSec = pygame.time.Clock()
 
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("psi")

image_droite = pygame.image.load("e.png").convert_alpha()
image_gauche = pygame.image.load("e_inv.png").convert_alpha()
image_droite_pink = pygame.image.load("e_pink.png").convert_alpha()
image_gauche_pink = pygame.image.load("e_inv_pink.png").convert_alpha()

image_phi_droite = pygame.image.load("phi.png").convert_alpha()
image_phi_gauche = pygame.image.load("phi_inv.png").convert_alpha()

all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
portes = pygame.sprite.Group()
loves = pygame.sprite.Group()
murs = pygame.sprite.Group()




 
class Personnage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = image_droite
        self.rect = self.surf.get_rect()
   
        self.pos = vec((27, 360))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False

        self.gauche = False
        self.droite = False

        self.greened = False
        self.pinked = False
 
    def move(self):
        self.acc = vec(0,0.5)
                
        if self.gauche:
            self.acc.x = -ACC
        if self.droite:
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
        
        hits = pygame.sprite.spritecollide(self ,portes, False)
        if hits:
            self.greened = True  
        
        hits = pygame.sprite.spritecollide(self ,loves, False)
        if hits:
            self.pinked = True      
        
        hits = pygame.sprite.spritecollide(self ,murs, False)
        if self.vel.x > 0 and not self.pinked:        
            if hits:
                if self.pos.x > hits[0].rect.left:               
                    self.pos.x = hits[0].rect.left -1  
                    self.vel.x = 0  

    def into_the_void(self):
        self.pos = vec((27, 360))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False




class Bot(Personnage):
    def __init__(self):
        super().__init__()  

    def deplacements(self):
        status= random.randint(1, 3)
        match status:
            case 1:
                self.droite = True 
                self.gauche = False 
            case 2:
                self.gauche = True
                self.droite = False
            case 3:
                self.droite = False
                self.gauche = False

        if self.gauche:
            self.surf = image_gauche
        if self.droite:
            self.surf = image_droite  


class PhiBot(Personnage):
    def __init__(self,pos_x,pos_y):
        super().__init__()  
        self.surf = image_phi_droite
        self.pos = vec((pos_x, pos_y))

    def deplacements(self):
        status= random.randint(1, 5)
        match status:
            case 1:
                self.droite = True 
                self.gauche = False 
            case 2:
                self.gauche = True
                self.droite = False
            case 3:
                self.droite = False
                self.gauche = False
            case 4:
                self.jump()
            case 5:
                self.cancel_jump()

        if self.gauche:
            self.surf = image_phi_gauche
        if self.droite:
            self.surf = image_phi_droite 


class Player(Personnage):
    def __init__(self):
        super().__init__()  

    def controls(self,event):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                self.gauche = True
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.droite = True  
            if event.key == pygame.K_SPACE or event.key == pygame.K_z or event.key == pygame.K_UP:
                self.jump()
        if event.type == pygame.KEYUP:   
            if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                self.gauche = False
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.droite = False 
            if event.key == pygame.K_SPACE or event.key == pygame.K_z or event.key == pygame.K_UP:
                self.cancel_jump()

        if event.type == pygame.JOYBUTTONDOWN:      
            if  event.button == 4:
                self.gauche = True
            if  event.button == 5:
                self.droite = True  
            if  event.button == 0:
                self.jump()
        if event.type == pygame.JOYBUTTONUP:      
            if  event.button == 4:
                self.gauche = False
            if  event.button == 5:
                self.droite = False 
            if  event.button == 0:
                self.cancel_jump()

        if self.gauche:
            if self.pinked :
                self.surf = image_gauche_pink
            else :
                self.surf = image_gauche
        if self.droite:
            if self.pinked :
                self.surf = image_droite_pink
            else :
                self.surf = image_droite    

    def joystick(self):
        if pygame.joystick.get_count()>0:
            axis_pos = joysticks[0].get_axis(0)

            if axis_pos < -1 * deadzone:
                self.gauche = True
            elif axis_pos > deadzone:
                self.droite = True  
            else:
                self.gauche = False
                self.droite = False          
 
 



class Platform(pygame.sprite.Sprite):
    def __init__(self,size,pos):
        super().__init__()
        self.surf = pygame.Surface(size)
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(center = pos)

    def move(self):
        pass


class PlatformRandomColor(Platform):
    def __init__(self,size,pos):
        super().__init__(size,pos)

        self.surf.fill((random.randint(0, 255),random.randint(0, 255),255))

    def move(self):
        pass    


class PlatformBlacknWhite(Platform):
    def __init__(self,size,pos):
        super().__init__(size,pos)

        blackorwhite = random.randint(0, 1)
        if blackorwhite==0 :
            self.surf.fill((255,255,255))
        else :
            self.surf.fill((0,0,0))

    def move(self):
        pass    
 
 
class MagicPlatform(Platform):
    def __init__(self,size,pos):
        super().__init__(size,pos)

        self.surf.fill((43,255,255))

    def move(self):
        pass
 
 




 
class Mur(pygame.sprite.Sprite):
    def __init__(self,size,pos):
        super().__init__()
        self.surf = pygame.Surface(size)
        self.surf.fill((255, 16, 240))
        self.rect = self.surf.get_rect(center = pos)

    def move(self):
        pass


class Porte(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.surf = pygame.Surface((16, 60))
        self.surf.fill((0,255,26))
        self.rect = self.surf.get_rect(center = pos)

    def move(self):
        pass    


class Texte(pygame.sprite.Sprite):
    def __init__(self,txt,x,y,color):
        super().__init__()
        my_font = pygame.font.SysFont('Times New Roman', 30)
        self.surf = my_font.render(txt, False, color)
        self.rect = self.surf.get_rect(center = (x, y))
    def move(self):
        pass


class Tableau(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        self.surf = image
        self.rect = self.surf.get_rect(center = (x, y))
    def move(self):
        pass


