import pygame

class Projectile():
    def __init__(self, x, y, direction,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.speed = 15 * direction
        self.direction = direction

    def update(self, target):
        self.rect.x += self.speed

        if self.rect.colliderect(target.rect):
            target.health -= 5
            return True  # destroy projectile

        return False

    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.direction < 0, False)
        surface.blit(img, self.rect)



class Fighter():
    def __init__(self,player, x, y, image, Arrow_img,  ):
        self.player = player
        self.Arrow_img = Arrow_img
        self.image = image
        self.flip = False
        self.action = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type =0
        self.health = 100
        self.projectiles = []
        self.attack_cooldown = 0
        self.alive = True

        

    def move(self, screen_width, screen_height, surface, target):
         if not self.alive:
            return
         SPEED = 10
         GRAVITY = 2
         dx = 0
         dy = 0   


         #get billenytűlenyomás
         key = pygame.key.get_pressed()
         
         #can only perform other actions if not currently attacking
         if self.attacking == False and self.alive == True:

        #check player 1 c
            if self.player == 1:
            #mozgás
                if key[pygame.K_a]:
                    dx = -SPEED
                if key[pygame.K_d]:
                    dx = SPEED

                #ugrás
                if key[pygame.K_w] and self.jump == False:
                        self.vel_y =-30
                        self.jump = True

                #támadás
                if key[pygame.K_r] or key[pygame.K_t]:
                    self.attack(surface, target)
                            
                    #támadás fajta
                    if key[pygame.K_r]:
                        self.attack_type = 1
                    if key[pygame.K_t]:
                        self.attack_type = 2

                if key [pygame.K_f]:
                    self.shoot()


             #check player 2 c
            if self.player == 2:
            #mozgás
                if key[pygame.K_LEFT]:
                    dx = -SPEED
                if key[pygame.K_RIGHT]:
                    dx = SPEED

                #ugrás
                if key[pygame.K_UP] and self.jump == False:
                        self.vel_y =-30
                        self.jump = True

                #támadás
                if key[pygame.K_KP1] or key[pygame.K_KP2]:
                    self.attack(surface, target)
                            
                    #támadás fajta
                    if key[pygame.K_KP1]:
                        self.attack_type = 1
                    if key[pygame.K_KP2]:
                        self.attack_type = 2

                if key [pygame.K_KP4]:
                    self.shoot()
            
    
         #Apply gravitáció
         self.vel_y += GRAVITY
         dy += self.vel_y

         #képernyőn maradás
         if self.rect.left +dx < 0:
             dx = 0 -self.rect.left
         if self.rect.right +dx > screen_width:
             dx = screen_width - self.rect.right
         if self.rect.bottom + dy > screen_height - 34:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 34 - self.rect.bottom 

         #ensure player face eachother
         if target.rect.centerx > self.rect.centerx:
             self.flip = False
         else:
             self.flip = True

         #player hely frissítés
         self.rect.x += dx
         self.rect.y +=dy

         for projectile in self.projectiles[:]:
            if projectile.update(target):
                self.projectiles.remove(projectile)
                
                # reduce attack cooldown
         if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

            
            # reset attacking
         if self.attack_cooldown == 0:
            self.attacking = False
                
         if self.health <= 0:
            self.health = 0
            self.alive = False       
    def attack(self, surface, target):
        if self.attack_cooldown == 0:
            self.attacking = True
            self.attack_cooldown = 20



            attacking_rect = pygame.Rect(self.rect.centerx - ( self.rect.width * self.flip), self.rect.y,  self.rect.width, self.rect.height )
            if attacking_rect.colliderect(target.rect):
                target.health -= 10
        
        


        
        
        
        
        
        pygame.draw.rect(surface, (0, 255, 0),attacking_rect)


    def shoot(self):
        if self.attack_cooldown == 0:
            self.attacking = True
            self.attack_cooldown = 20
            direction = -1 if self.flip else 1
            projectile = Projectile(self.rect.centerx, self.rect.centery, direction, self.Arrow_img)
            self.projectiles.append(projectile)    
         



    def draw (self, surface):
        for projectile in self.projectiles:
            projectile.draw(surface)
        img = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(img, (self.rect.x, self.rect.y))

        for projectile in self.projectiles:
            projectile.draw(surface)


 
