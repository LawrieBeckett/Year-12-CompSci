import pygame
# -- Global Constants
# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
# -- Initialise PyGame
pygame.init()
# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("Lawrie's Game")
# -- Exit game flag set to false
done = False
computer_score = 0
player_score = 0
block_p_x = 10
block_p_y = 5
block_c_x = 620
block_c_y = 5
direction_y = 0
speed = 5
ball_x = 5
ball_y = 5
ball_x_direction = 1
ball_y_direction = -1
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

while not done:
# -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction_y = -1
            elif event.key == pygame.K_DOWN:
                direction_y = 1
        elif event.type == pygame.KEYUP:
            direction_y = 0
        #End If
    #Next event
    # -- Game logic goes after this comment
    block_p_y = block_p_y + direction_y * speed

    if block_p_y + 100 > 480:
        direction_y = direction_y * 0
    elif block_p_y < 0:
        direction_y = direction_y * 0
    
    

    
    if ball_x >= 640 or ball_x <= 0 or (ball_x < block_p_x + 10 and ball_y < block_p_y + 100 and ball_y > block_p_y ) or (ball_x > block_c_x - 10 and ball_y < block_c_y + 100 and ball_y > block_c_y) :
        ball_x_direction = ball_x_direction * -1
    ball_x = ball_x + ball_x_direction * speed

    if ball_y >= 480:
        ball_y_direction = -1
    elif ball_y <= 0:
        ball_y_direction = 1
    ball_y = ball_y + ball_y_direction * speed

    if ball_x >= 320:
        if ball_y > block_c_y:
            block_c_y = block_c_y + 1 * speed
        elif ball_y < block_c_y + 100:
            block_c_y = block_c_y - 1 * speed

    if block_c_y + 100 < 0:
        block_c_y = block_c_y + 1

    if ball_x == 0:
        computer_score = computer_score + 1
    elif ball_x == 640:
        player_score = player_score + 1

    ### SRC - The scoring doesn't seem to be working...

    if player_score == 5:
        done = True
        fo.open(Leaderboard [a][1])
        input(fileObject.write())
        fo.close
    elif computer_score == 5:
        done = True
        fo.open(Leaderboard [a][1])
        input(fileObject.write())
        fo.close

    
    
   

     ### SRC - Why so much space?     

            
    
    
 


    # -- Screen background is BLACK
    screen.fill (BLACK)
    # -- Draw here
    pygame.draw.rect(screen, BLUE, (block_p_x, block_p_y,10,100))
    pygame.draw.circle(screen, WHITE, (ball_x,ball_y),5,0)
    pygame.draw.rect(screen, YELLOW, (block_c_x, block_c_y,10,100))
    
                     
  
    # -- flip display to reveal new position of objects
    pygame.display.flip()
     # - The clock ticks over
    clock.tick(60)
    #End While - End of game loop
pygame.quit()
