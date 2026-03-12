import pygame

class Projectile():
    def __init__(self, x, y, direction):
        self.rect = pygame.Rect(x, y, 20, 10)
        self.speed = 15 * direction

    def update(self, target):
        self.rect.x += self.speed

        if self.rect.colliderect(target.rect):
            target.health -= 5
            return True  # destroy projectile

        return False

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 0), self.rect)



class Fighter():
    def __init__(self,x, y):
        self.flip = False
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type =0
        self.health = 100
        self.projectiles = []

    def move(self, screen_width, screen_height, surface, target):
         SPEED = 10
         GRAVITY = 2
         dx = 0
         dy = 0   


         #get billenytűlenyomás
         key = pygame.key.get_pressed()
         
         #can only perform other actions if not currently attacking
         if self.attacking == False:
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
    

    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height )
        if attacking_rect.colliderect(target.rect):
            target.health -= 10

    
        
        
        
        
        
        pygame.draw.rect(surface, (0, 255, 0),attacking_rect)


    def shoot(self):
        self.attacking = True
        direction = -1 if self.flip else 1
        projectile = Projectile(self.rect.centerx, self.rect.centery, direction)
        self.projectiles.append(projectile)    
         



    def draw (self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

        for projectile in self.projectiles:
            projectile.draw(surface)


        