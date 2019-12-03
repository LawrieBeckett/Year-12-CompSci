import pygame
import random
# -- Global Constants
# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (224,0,0)
screen_width = 640
screen_height = 640
speed = 2
direction = 0
shoot = 0
# -- Classes


class Invader(pygame.sprite.Sprite):
    def __init__(self,colour,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(RED)

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 1

        if self.rect.y == screen_height:
            self.rect.x =random.randrange(screen_width)
            self.rect.y = random.randrange(320)
            
        

class Player(pygame.sprite.Sprite):
    def __init__(self,colour,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()

class Bullet(pygame.sprite.Sprite):
    def __init__(self,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= speed
        

# -- Initialise PyGame
pygame.init()
# -- Blank Screen

size = (screen_width,screen_height)
screen = pygame.display.set_mode(size)

myinvader_grp = pygame.sprite.Group()

bullet_grp = pygame.sprite.Group()

all_sprites_grp = pygame.sprite.Group()

myplayer = Player(WHITE,25,25)
myplayer.rect.x = 320
myplayer.rect.y = (640 - 25)
all_sprites_grp.add(myplayer)

mybullet = Bullet(2,5)
mybullet.rect.y = 0

for i in range(50):
    myinvader = Invader(RED,25,25)
    myinvader.rect.x = random.randrange(screen_width)
    myinvader.rect.y = random.randrange(320)
    myinvader_grp.add(myinvader)
    all_sprites_grp.add(myinvader)

# -- Title of new window/screen
pygame.display.set_caption("Lawrie's Game")
# -- Exit game flag set to false
done = False

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

while not done:
# -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = 1
            elif event.key == pygame.K_LEFT:
                direction = -1
        elif event.type == pygame.KEYUP:
            direction = 0



    myplayer.rect.x += direction * 2
        #End If
    #Next event
    # -- Game logic goes after this comment
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            shoot = 1
    elif event.type == pygame.KEYUP:
            shoot = 0
        

    if shoot == 1:
        mybullet = Bullet(2,5)
        bullet_grp.add(mybullet)
        mybullet.rect.x = myplayer.rect.x
        mybullet.rect.y = myplayer.rect.y

    for bullet in bullet_grp:
 
        invaderhitlist = pygame.sprite.spritecollide(bullet_grp, myinvader_grp, True)
 
        for invader in invaderhitlist:
            bullet_grp.remove(bullet)
            score += 1
            print(score)
 
        if bullet.rect.y < -10:
            bullet_grp.remove(bullet)
            all_sprites_list.remove(bullet)

    
    
        
    
    
   

          

            
    all_sprites_grp.update()
    bullet_grp.update()
    
 


    # -- Screen background is BLACK
    screen.fill (BLACK)
    # -- Draw here
    all_sprites_grp.draw(screen)
    bullet_grp.draw(screen)
  
    # -- flip display to reveal new position of objects
    pygame.display.flip()
     # - The clock ticks over
    clock.tick(60)
    #End While - End of game loop
pygame.quit()
