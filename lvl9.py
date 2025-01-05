from classiq import *
from lvl1 import *

def genBlock(x,y):
    w = random.randint(20, 150)
    h = random.randint(20, 150)

    plat_ = Platform((w, h),(x, y))
    all_sprites.add(plat_)
    platforms.add(plat_)


def lvl9():

    infoObject = pygame.display.Info()
    width_ = infoObject.current_w
    height_ = infoObject.current_h
    pygame.mouse.set_visible(False) # Hide cursor here



    P1 = GreenPlayer()
    P1.pos.x= width_/2
    P1.pos.y= height_
    P1.rect.midbottom = P1.pos
    all_sprites.add(P1)

    plat_virtuelle_largeur_screen = MagicPlatform((5000, 20),(width_/2, height_+10))
    all_sprites.add(plat_virtuelle_largeur_screen)
    platforms.add(plat_virtuelle_largeur_screen)


    gen_structure_lvl(-2500,-2500)

    fin_escalier_droite_txt = Texte("I will always be there",7300-2500, -800-2500,(255, 255, 255))
    all_sprites.add(fin_escalier_droite_txt)

    red_door = PorteRouge((7300-2500+300+200, -800-2500))
    all_sprites.add(red_door)
    portesRouge.add(red_door)

    plaaaaa = Platform((1000, 20),(7300-2500+300, -800-2500+40))
    all_sprites.add(plaaaaa)
    platforms.add(plaaaaa)



    x_ = P1.pos.x
    y_ = P1.pos.y+300

    screen_y_offset = 0

    while not P1.reded:

        if y_ > -1500 :
            genBlock(x_,y_)
            x_-=random.randint(20, 150)
            y_-=random.randint(20, 150)



        P1.update()

        for event in pygame.event.get():
            P1.controls(event)

        P1.joystick()        

        screen.fill((0,0,0))

        camera.x = P1.pos.x - width_ / 2

        if P1.pos.y < 0.25*height_:
            screen_y_offset = P1.pos.y - (height_*0.25)

               
        for entity in all_sprites:
            entity.move()
            screen.blit(entity.surf, (entity.rect.x - camera.x, entity.rect.y - screen_y_offset))


        pygame.display.update()
        FramePerSec.tick(FPS)

    
    #change wallpaper
    url_fichier = os.path.realpath(__file__)
    url_dossier = os.path.dirname(url_fichier)

    print(url_dossier)

    ctypes.windll.user32.SystemParametersInfoW(20, 0, glob.escape(url_dossier) + "/assets/well_play.png" , 0)

