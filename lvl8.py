from classiq import *




        



def lvl8():

    screen_cam = pygame.math.Vector2((0, 0))

    infoObject = pygame.display.Info()
    offset_x_manquant = (infoObject.current_w-800)/2
    offset_y_manquant = (infoObject.current_h-600)/2


    P1 = Player()
    P1.pos.x= (infoObject.current_w)/2
    P1.pos.y= (infoObject.current_h)/2
    P1.spawn.x= (infoObject.current_w)/2
    P1.spawn.y= (infoObject.current_h)/2
    P1.rect.midbottom = P1.pos
    P1.surf=image_gauche
    all_spritesHorsCadre.add(P1)


    platane = Platform((400, 20),(P1.pos.x+200, P1.pos.y+8))
    all_spritesHorsCadre.add(platane)
    platforms.add(platane)

    
    plat_virtuelle = MagicPlatform((400, 20),(P1.pos.x, P1.pos.y+8))
    all_spritesHorsCadre.add(plat_virtuelle)
    platforms.add(plat_virtuelle)

    plat_virtuelle_largeur_screen = MagicPlatform((10000, 20),(P1.pos.x, infoObject.current_h+10))
    all_spritesHorsCadre.add(plat_virtuelle_largeur_screen)
    platforms.add(plat_virtuelle_largeur_screen)

    '''
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
    '''

    #/fenetre
    fenetre = pygame.Surface((800, 600))

    spanw_txt = Texte("OK, I stop recording",27-250-20*27-2100+10, 600-10*27-50,(255, 255, 255))
    all_sprites.add(spanw_txt)
    #fenetre/


    bg_img = pygame.image.load("monitor-1.png").convert_alpha()

 
    camera.x = -2602.93827160495 - 800 / 2
    camera.y = 321.75 - 600 / 2

    phi_not_spawned = True

    while not P1.greened:

        
       
        P1.update()

        for event in pygame.event.get():
            P1.controls(event)

        P1.joystick()        

  
        screen.fill((0,0,0))
        fenetre.fill((0,0,0))
        
        screen.blit(bg_img, (0 - screen_cam.x, 0 - screen_cam.y))

      
        for entity in all_sprites:
            entity.move()
            fenetre.blit(entity.surf, (entity.rect.x - camera.x, entity.rect.y - camera.y))


        screen.blit(fenetre, (offset_x_manquant - screen_cam.x, offset_y_manquant- screen_cam.y))

               
        for entity in all_spritesHorsCadre:
            entity.move()
            screen.blit(entity.surf, (entity.rect.x - screen_cam.x, entity.rect.y - screen_cam.y))


        if P1.pos.y > (infoObject.current_h+100):
            P1.into_the_void()



        if P1.pos.x > (infoObject.current_w*0.75):
            screen_cam.x = P1.pos.x - (infoObject.current_w*0.75)
            if phi_not_spawned:
                phi_not_spawned = False
                phi = PhiBot(infoObject.current_w+500,infoObject.current_h)
                all_spritesHorsCadre.add(phi)
                #genererStructure(infoObject.current_w+1000,infoObject.current_h)

                porte2 = Porte((infoObject.current_w+1500,infoObject.current_h-30))
                all_spritesHorsCadre.add(porte2)
                portes.add(porte2)

        if not phi_not_spawned:
            phi.update()
            phi.deplacements()

        pygame.display.update()
        FramePerSec.tick(FPS)
