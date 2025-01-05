from classiq import *


def lvl3():


    P1 = Player()
    all_sprites.add(P1)

    spanw_txt = Texte("†",27, 360,(255, 255, 255))
    all_sprites.add(spanw_txt)

    plat = Platform((2000, 20),(0, 600))
    all_sprites.add(plat)
    platforms.add(plat)



    mur_droit = Mur((20, 1500),(500, 600-760))
    all_sprites.add(mur_droit)
    murs.add(mur_droit)


    id_txt = Texte("Good ideas always come back",0, 600-50,(255,255,255))
    all_sprites.add(id_txt)




    love_txt = Texte("<",375, -228,(255, 16, 240))
    all_sprites.add(love_txt)
    loves.add(love_txt)




    porte = Porte((800, 600-40))
    all_sprites.add(porte)
    portes.add(porte)




    for i in range(5):
        pl = Platform((30*i, 20),(490-(15*i), 600 - i*200))
        all_sprites.add(pl)
        platforms.add(pl)



    while not P1.greened:


        #quand P1 entre en collision avec platforms
        P1.update()

        for event in pygame.event.get():
            P1.controls(event)

        P1.joystick()

        #fond noir
        screen.fill((0,0,0))

        #ajust camera
        camera.x = P1.pos.x - 800 / 2
        camera.y = P1.pos.y - 600 / 2
        
        #deplacer les sprites 
        for entity in all_sprites:
            entity.move()
            screen.blit(entity.surf, (entity.rect.x - camera.x, entity.rect.y - camera.y))

        if (P1.rect.y - camera.y) > 600:
            P1.into_the_void()


        pygame.display.update()
        FramePerSec.tick(FPS)