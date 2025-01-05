from classiq import *


def lvl4():


    P1 = Player()
    all_sprites.add(P1)

    spanw_txt = Texte("†",27, 360,(255, 255, 255))
    all_sprites.add(spanw_txt)


    clone = Bot()
    all_sprites.add(clone)


    sim_txt = Texte("You live in a simulation Epsilon",0, 600-50,(255,255,255))
    all_sprites.add(sim_txt)



    def create_block(x, y):
        plat = PlatformRandomColor((15, 15),(x, y))
        all_sprites.add(plat)
        platforms.add(plat)

    def fractal(x,y,profondeur):
        create_block(x, y)
        x_droit=x
        x_gauche=x

        index=0
        while index < 3:
            index+=1
            
            for i in range(profondeur):
                x_gauche-=15
                x_droit+=15
                y+=i
                create_block(x_gauche, y)
                create_block(x_droit, y)

                for i in range(profondeur):
                    x_gauche-=15
                    x_droit+=15
                    y+=i
                    create_block(x_gauche, y)
                    create_block(x_droit, y)
            
            for i in range(profondeur):
                x_gauche-=15
                x_droit+=15
                y-=i
                create_block(x_gauche, y)
                create_block(x_droit, y)
                
                for i in range(profondeur):
                    x_gauche-=15
                    x_droit+=15
                    y-=i
                    create_block(x_gauche, y)
                    create_block(x_droit, y)

            

 


    fractal(0, 600,10)

    porte = Porte((15*3*10*10*2, 600))
    all_sprites.add(porte)
    portes.add(porte)

    porte = Porte((-15*3*10*10*2, 600))
    all_sprites.add(porte)
    portes.add(porte)



    while not P1.greened:


        #quand P1 entre en collision avec platforms
        P1.update()

        clone.update()

        for event in pygame.event.get():
            P1.controls(event)

        P1.joystick()

        clone.deplacements()

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

        if (clone.rect.y - camera.y) > 600:
            clone.into_the_void()


        pygame.display.update()
        FramePerSec.tick(FPS)