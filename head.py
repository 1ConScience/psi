import pygame
from pygame.locals import *
import sys
import random
import glob
from pathlib import Path
import os
#screenshot
from mss import mss
#change wallpaper
import ctypes


def nettoyage():
    pygame.sprite.Group.empty(all_sprites)
    pygame.sprite.Group.empty(platforms)
    pygame.sprite.Group.empty(plafonds)
    pygame.sprite.Group.empty(portes)
    pygame.sprite.Group.empty(loves)
    pygame.sprite.Group.empty(murs)

    pygame.sprite.Group.empty(all_spritesHorsCadre)
    pygame.sprite.Group.empty(portesRouge)


pygame.init()

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

camera = pygame.math.Vector2((0, 0))
vec = pygame.math.Vector2 #2 for two dimensional
 
HEIGHT = 800
WIDTH = 600
ACC = 0.5
FRIC = -0.10#-0.12
FPS = 60

deadzone = 0.3
 
FramePerSec = pygame.time.Clock()
 
screen = pygame.display.set_mode((HEIGHT, WIDTH))

pygame.display.set_caption("psi")


image_droite = pygame.image.load("assets/e.png").convert_alpha()
image_gauche = pygame.image.load("assets/e_inv.png").convert_alpha()
image_droite_black = pygame.image.load("assets/e_black.png").convert_alpha()
image_gauche_black = pygame.image.load("assets/e_inv_black.png").convert_alpha()
image_droite_pink = pygame.image.load("assets/e_pink.png").convert_alpha()
image_gauche_pink = pygame.image.load("assets/e_inv_pink.png").convert_alpha()
image_droite_green = pygame.image.load("assets/e_green.png").convert_alpha()
image_gauche_green = pygame.image.load("assets/e_inv_green.png").convert_alpha()

image_phi_droite = pygame.image.load("assets/phi.png").convert_alpha()
image_phi_gauche = pygame.image.load("assets/phi_inv.png").convert_alpha()


ana = pygame.image.load("assets/red_flash.gif").convert_alpha()

all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
plafonds = pygame.sprite.Group()
portes = pygame.sprite.Group()
loves = pygame.sprite.Group()
murs = pygame.sprite.Group()



all_spritesHorsCadre = pygame.sprite.Group()
portesRouge = pygame.sprite.Group()

