from classiq import *

def lvl2():

    home = Path.home()

    # get the path/directory
    folder_dir = glob.escape(home) + "/Pictures"


    liste_images = []

    nb_photos = 0


    #liste un a un de facon recursive les dossiers se trouvant dans le dossier image de l'utilisateur
    def get_dirlist(rootdir):

        dirlist = []

        with os.scandir(rootdir) as rit:
            for entry in rit:
                if not entry.name.startswith('.') and entry.is_dir():
                    dirlist.append(entry.path)
                    dirlist += get_dirlist(entry.path)

        return dirlist





    for prout in get_dirlist(folder_dir):

        # iterate over files in
        # that directory
        for img in glob.iglob(f'{prout}/*'):
        
            # check if the image ends with png
            if (img.endswith(".jpg")):
                image = pygame.image.load(img).convert()
                image = pygame.transform.scale(image, (WIDTH/10, HEIGHT/10)) 
                liste_images.append(image)

                nb_photos +=1

            if nb_photos>10:
                break

        if nb_photos>10:
            break




    for index, image in enumerate(liste_images):
        tableau = Tableau(image,WIDTH+index*300, -1950)
        all_sprites.add(tableau)






    P1 = Player()
    all_sprites.add(P1)

    PT1 = Platform((20000, 20),(0, -1880))
    all_sprites.add(PT1)
    platforms.add(PT1)

    porte = Porte(((WIDTH/30)*26, HEIGHT - 200*27))
    all_sprites.add(porte)
    portes.add(porte)


    for i in range(27):
        PT = Platform((200, 15),((WIDTH/30)*i, HEIGHT - 200*i))
        all_sprites.add(PT)
        platforms.add(PT)



    never_txt = Texte("Quel endroit magnifique...",0, -1950,(43,255,255))
    all_sprites.add(never_txt)



    while not P1.greened:

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