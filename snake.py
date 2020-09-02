import pygame, sys, time, random

# Check error pygame
check_errors = pygame.init()
if check_errors[1] > 0:
    print('[!]{check_errors} errors run the game')
    sys.exit(-1)
else:
    print('[+]Game success install')

#####========== Create Window Game ===========
# size game screen
size_x = 720
size_y = 480
# title window game
pygame.display.set_caption('My Snake')
screen = pygame.display.set_mode((size_x, size_y))

#####==========End create Window Game ===========

#####============ game variable =============

# color
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)

# snake
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
direction = "RIGHT"
change_to = "RIGHT"

# food
food_pos = [random.randrange(1, (size_x//10)) * 10, random.randrange(5, (size_y//10)) * 10]
food_spawn = True

# background white
screen.fill(white)
pygame.display.flip()

# score  
score = 0

# sound
pygame.mixer.init()
eating = pygame.mixer.Sound('eatsong.wav')
# pygame.mixer.music.load('backsong.mp3')
# pygame.mixer.music.play()


#####============ End game variable =============

# game over funct
def game_over():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU DIED', True, white)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (size_x/2, size_y/4)
    screen.fill(black)
    screen.blit(game_over_surface, game_over_rect)
    # show_score(0, red, 'times', 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()

# show score funct
def show_score():
    score_font = pygame.font.SysFont('consolas', 20)
    score_surface = score_font.render('Your poin:' + str(score), True, black)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (72, 15)

    screen.blit(score_surface, score_rect)
    pygame.display.flip()

# running
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
    # draw snake
    screen.fill(white)
    for pos in snake_body:
        pygame.draw.ellipse(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
    # make sure move
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    # snake runner
    if direction == "RIGHT":
        snake_pos[0] += 10
    if direction == "LEFT":
        snake_pos[0] -= 10
    if direction == "UP":
        snake_pos[1] -= 10
    if direction == "DOWN":
        snake_pos[1] += 10

    snake_body.insert(0, list(snake_pos))  

    # snake eat food
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        pygame.mixer.music.pause()
        eating.play() 
        score += 1
        food_spawn = False
    else:
        snake_body.pop()
    pygame.mixer.music.unpause()
    # food spawn
    if not food_spawn:
        food_pos = [random.randrange(1, (size_x//10)) * 10, random.randrange(5, (size_y//10)) * 10]
    food_spawn = True

    # draw food
    pygame.draw.rect(screen, green, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # snake over window
    if snake_pos[0] > size_x:
        snake_pos[0] = 0
    if snake_pos[0] < 0:
        snake_pos[0] = size_x
    if snake_pos[1] > size_y:
        snake_pos[1] = 50
    if snake_pos[1] < 50:
        snake_pos[1] = size_y
    
    # snake dead eating self
    pygame.draw.rect(screen, black, pygame.Rect(snake_pos[0], snake_pos[1], 10, 10))
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    # run score
    show_score()
    # border create
    for x in range(0, 810, 10):
        pygame.draw.rect(screen, black, [x, 40, 10, 10])
        # pygame.draw.rect(screen, black, [x, 610, 10, 10])

    # display game
    pygame.display.update()

    # level
    pygame.time.Clock().tick(10)
