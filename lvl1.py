from classiq import *


def gen_structure_lvl(offset_x,offset_y):
    spanw_txt = Texte("†",27+offset_x, 360+offset_y,(255, 255, 255))
    all_sprites.add(spanw_txt)


    PT0 = MagicPlatform((100, 20),(-100+offset_x, 600+200+offset_y))
    all_sprites.add(PT0)
    platforms.add(PT0)



    for i in range(272):
        PT = Platform(((800/30), 15),((800/30)*i+offset_x, 600 - 5*i+offset_y))
        all_sprites.add(PT)
        platforms.add(PT)


    def tree(x,y,profondeur):
        profondeur+=1
        if profondeur < 7 :
            plat = Platform(((800/30), 15),(x, y))
            all_sprites.add(plat)
            platforms.add(plat)
            tree(x-50, y+200,profondeur)
            tree(x+50, y+200,profondeur)

    tree(-200+offset_x, 600+400+offset_y,0)

    PT01 = Platform((100, 20),(-200+offset_x, 2200+offset_y))
    all_sprites.add(PT01)
    platforms.add(PT01)


    PTNEXT = MagicPlatform((1000, 20),(-800+offset_x, 2350+offset_y))
    all_sprites.add(PTNEXT)
    platforms.add(PTNEXT)







def lvl1():

    P1 = Player()
    all_sprites.add(P1)

    gen_structure_lvl(0,0)

    drug_txt = Texte("The cake is NOT a lie",-150, 600+300,(255, 255, 255))
    all_sprites.add(drug_txt)

    tout_en_bas_txt = Texte("<- ʚʃɞ",-200, 2100,(255, 255, 255))
    all_sprites.add(tout_en_bas_txt)

    mid_txt = Texte("I counted, there are 272 steps",3650, -250,(255, 255, 255))
    all_sprites.add(mid_txt)

    fin_escalier_droite_txt = Texte("Please, don't kill yourself Epsilon",7300, -800,(255, 255, 255))
    all_sprites.add(fin_escalier_droite_txt)

    '''
    check_haut_escalier = False
    check_bas_derniere_platform = False
    new_bas_last_plat_added = False
    new_haut_escalier_added = False
    '''



    porte1 = Porte((-1292, 2310))
    all_sprites.add(porte1)
    portes.add(porte1)    

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

        
        '''
        if P1.pos.x>7100 and not new_bas_last_plat_added:
            check_haut_escalier = True
            if check_bas_derniere_platform:
                tout_en_bas_txt.kill()
                tout_en_bas_txt = Texte("Here is your cake :)",-200, 2100,(255, 255, 255))
                all_sprites.add(tout_en_bas_txt)



                new_bas_last_plat_added = True

        if P1.pos.y>2190 and P1.pos.x<1100 and not new_haut_escalier_added:
            check_bas_derniere_platform = True
            if check_haut_escalier:
                fin_escalier_droite_txt.kill()
                fin_escalier_droite_txt = Texte("What ? No, I am not kidding you :)",7300, -800,(255, 255, 255))
                all_sprites.add(fin_escalier_droite_txt)

                PTNEXT2 = MagicPlatform((1000, 20),(7800, -900))
                all_sprites.add(PTNEXT2)
                platforms.add(PTNEXT2)

                porte2 = Porte((8293, -940))
                all_sprites.add(porte2)
                portes.add(porte2)

                new_haut_escalier_added = True
        '''   


        pygame.display.update()
        FramePerSec.tick(FPS)