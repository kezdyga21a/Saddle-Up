import pygame
from fighter import Fighter

pygame.init()

#ablak
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Saddle Up!")

#framerate beállítás
clock = pygame.time.Clock()
FPS = 60

#színek
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)


#háttér betöltés
bg_image = pygame.image.load("background.png").convert_alpha()


szilaj_image = pygame.image.load("Szilaj.png").convert_alpha()
nemszilaj_image = pygame.image.load("Nemszilaj.png").convert_alpha()
Arrow_img =pygame.image.load("Arrow.png").convert_alpha()




#háttér rajzolás funkció
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg,   (0,0))


    

#health bar rajzolás
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen,WHITE,(x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

# kettő fighter
fighter_1 = Fighter(1, 200, 386, szilaj_image,Arrow_img)
fighter_2 = Fighter(2, 700, 386, nemszilaj_image,Arrow_img)

#loop
run =True
while run:

    clock.tick(FPS)

    #draw background
    draw_bg()

    #show astats
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)


    #fighter mozgás
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2) 
    fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1) 

    #draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    #event kezelő
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


     #képernyő frissítés
    pygame.display.update()



#becsukás
pygame.quit()
