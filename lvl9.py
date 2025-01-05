from classiq import *


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

    P1 = Player()
    P1.pos.x= width_/2
    P1.pos.y= height_
    P1.spawn= P1.pos
    P1.rect.midbottom = P1.pos
    all_sprites.add(P1)

    plat_virtuelle_largeur_screen = MagicPlatform((5000, 20),(width_/2, height_+10))
    all_sprites.add(plat_virtuelle_largeur_screen)
    platforms.add(plat_virtuelle_largeur_screen)

    x_ = P1.pos.x
    y_ = P1.pos.y

    screen_y_offset = 0

    while not P1.greened:

        genBlock(x_,y_)
        x_-=100
        y_-=100

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

        if P1.pos.y > (height_+20):
            P1.into_the_void()

        pygame.display.update()
        FramePerSec.tick(FPS)

        

        