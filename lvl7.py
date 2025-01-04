from classiq import *


def lvl7():


    miroir = Miroir((27-250-20*27-1000+10, HEIGHT-10*27-150))
    all_sprites.add(miroir)


  



    P1 = Player()
    all_sprites.add(P1)

    spanw_txt = Texte("†",27, 360,(255, 255, 255))
    all_sprites.add(spanw_txt)



    plat_ = Platform((500, 20),(27, HEIGHT))
    all_sprites.add(plat_)
    platforms.add(plat_)




    
    for i in range(27):
        plat_ = Platform((20, 20),(27-250-20*i, HEIGHT-10*i))
        all_sprites.add(plat_)
        platforms.add(plat_)


    plat_ = Platform((2000, 20),(27-250-20*27-1000+10, HEIGHT-10*27))
    all_sprites.add(plat_)
    platforms.add(plat_)


    spanw_txt = Texte("OK, j'arrête de filmer",27-250-20*27-2100+10, HEIGHT-10*27-50,(255, 255, 255))
    all_sprites.add(spanw_txt)








    while not P1.greened:




        








        #quand P1 entre en collision avec platforms
        P1.update()
        miroir.update(P1.pos.x, P1.pos.y,P1.gauche,P1.droite)


        for event in pygame.event.get():
            P1.controls(event)

        P1.joystick()


        #fond noir
        screen.fill((0,0,0))
        

        #ajust camera
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