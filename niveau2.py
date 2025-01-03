import pygame
from pygame.locals import *
import sys

import glob
from pathlib import Path
import os



pygame.init()

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

camera = pygame.math.Vector2((0, 0))
vec = pygame.math.Vector2 #2 for two dimensional
 
WIDTH = 1280
HEIGHT = 720
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


class Tableau(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        self.surf = image
        self.rect = self.surf.get_rect(center = (x, y))
    def move(self,gauche,droite):
        pass



all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
portes = pygame.sprite.Group()






home = Path.home()

# get the path/directory
folder_dir = glob.escape(home) + "/Pictures"


liste_images = []

nb_photos = 0


#liste un a un de facon recursive les dossiers se trouvant dans le dossier image de l'utilisateur
def get_dirlist(rootdir):

    dirlist = []

    with os.scandir(rootdir) as rit:
        for entry in rit:
            if not entry.name.startswith('.') and entry.is_dir():
                dirlist.append(entry.path)
                dirlist += get_dirlist(entry.path)

    return dirlist





for prout in get_dirlist(folder_dir):

    # iterate over files in
    # that directory
    for img in glob.iglob(f'{prout}/*'):
    
        # check if the image ends with png
        if (img.endswith(".jpg")):
            image = pygame.image.load(img).convert()
            image = pygame.transform.scale(image, (WIDTH/10, HEIGHT/10)) 
            liste_images.append(image)

            nb_photos +=1

        if nb_photos>10:
            break

    if nb_photos>10:
        break




for index, image in enumerate(liste_images):
    tableau = Tableau(image,WIDTH+index*300, -1950)
    all_sprites.add(tableau)






P1 = Player()
all_sprites.add(P1)

PT1 = Platform((20000, 20),(255,255,255),(0, -1880))
all_sprites.add(PT1)
platforms.add(PT1)

porte = Porte(((WIDTH/30)*26, HEIGHT - 200*27))
all_sprites.add(porte)
portes.add(porte)


for i in range(27):
    PT = Platform((200, 15),(255,255,255),((WIDTH/30)*i, HEIGHT - 200*i))
    all_sprites.add(PT)
    platforms.add(PT)



never_txt = Texte("Quel endroit magnifique...",0, -1950,(43,255,255))
all_sprites.add(never_txt)




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

    P1.test_portes()

    pygame.display.update()
    FramePerSec.tick(FPS)