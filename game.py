from lvl1 import *
from lvl2 import *
from lvl3 import *

def nettoyage():
    pygame.sprite.Group.empty(all_sprites)
    pygame.sprite.Group.empty(platforms)
    pygame.sprite.Group.empty(portes)
    pygame.sprite.Group.empty(loves)
    pygame.sprite.Group.empty(murs)

lvl1()
nettoyage()
lvl2()
nettoyage()
lvl3()
nettoyage()




