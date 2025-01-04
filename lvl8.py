from classiq import *


def lvl8():

    infoObject = pygame.display.Info()
    offset_x_manquant = (infoObject.current_w-WIDTH)/2
    offset_y_manquant = (infoObject.current_h-HEIGHT)/2


    P1 = Player()
    P1.pos.x= (infoObject.current_w)/2
    P1.pos.y= (infoObject.current_h)/2
    P1.rect.midbottom = P1.pos
    P1.surf=image_gauche
    all_spritesHorsCadre.add(P1)

    plat_virtuelle = MagicPlatform((200, 20),(P1.pos.x, P1.pos.y+8))
    all_spritesHorsCadre.add(plat_virtuelle)
    platforms.add(plat_virtuelle)

    for i in range(10):
        plat_ = Platform((20, 20),(P1.pos.x+10*i, P1.pos.y+8-10*i))
        all_spritesHorsCadre.add(plat_)
        platforms.add(plat_)

    for i in range(10):
        plat_ = Platform((20, 20),(P1.pos.x-10*i-20*7, P1.pos.y+8-10*i-10*7))
        all_spritesHorsCadre.add(plat_)
        platforms.add(plat_)

    for i in range(10):
        plat_ = Platform((20, 20),(P1.pos.x+10*i, P1.pos.y+8-10*i-10*14))
        all_spritesHorsCadre.add(plat_)
        platforms.add(plat_)
    for i in range(10):
        plat_ = Platform((20, 20),(P1.pos.x+10*i+20*7, P1.pos.y+8-10*i-10*21))
        all_spritesHorsCadre.add(plat_)
        platforms.add(plat_)


    #/fenetre
    fenetre = pygame.Surface((WIDTH, HEIGHT))

    spanw_txt = Texte("OK, j'arrête de filmer",27-250-20*27-2100+10, HEIGHT-10*27-50,(255, 255, 255))
    all_sprites.add(spanw_txt)
    #fenetre/


    bg_img = pygame.image.load("monitor-1.png").convert_alpha()

 
    camera.x = -2602.93827160495 - WIDTH / 2
    camera.y = 321.75 - HEIGHT / 2

    while True:

        
       
        P1.update()

        for event in pygame.event.get():
            P1.controls(event)

        P1.joystick()        

  
        screen.fill((0,0,0))
        fenetre.fill((0,0,0))
        
        screen.blit(bg_img, (0, 0))

      
        for entity in all_sprites:
            entity.move()
            fenetre.blit(entity.surf, (entity.rect.x - camera.x, entity.rect.y - camera.y))


        screen.blit(fenetre, (offset_x_manquant, offset_y_manquant))

               
        for entity in all_spritesHorsCadre:
            entity.move()
            screen.blit(entity.surf, (entity.rect.x, entity.rect.y))



        pygame.display.update()
        FramePerSec.tick(FPS)
