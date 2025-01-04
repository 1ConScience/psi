from classiq import *


def lvl6():


    P1 = Player()
    all_sprites.add(P1)

    spanw_txt = Texte("†",27, 360,(255, 255, 255))
    all_sprites.add(spanw_txt)




    def create_block(x, y):
        plat_ = Platform((10, 20),(x, y))
        all_sprites.add(plat_)
        platforms.add(plat_)

        plat_ = Plafond((10, 20),(x, y-200))
        all_sprites.add(plat_)
        plafonds.add(plat_)


    

    porte = Porte((-11802,1421))
    all_sprites.add(porte)
    portes.add(porte)


 


    index_x=0
    index_y=HEIGHT

    while not P1.greened:

        index_x+=4
        create_block(index_x, index_y)

        status= random.randint(1, 4)
        match status:
            case 1:
                index_y-=1
            case 2:
                pass
            case 3:
                index_y-=1
            case 4:
                index_y+=1

   





        #quand P1 entre en collision avec platforms
        P1.update()


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