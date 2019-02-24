import pygame

pygame.init()

# size of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Crossy RPG'

WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

clock = pygame.time.Clock()
# FPS with the typical rate of 60
TICK_RATE = 60
is_game_over = False

# sdoinsgnosnfosf

# create the window of the specified size in white to display the game
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# set the game window color to white
game_screen.fill(WHITE_COLOR)
pygame.display.set_caption(SCREEN_TITLE)

# load the player image from the file directory
player_image = pygame.image.load('player.png')
# scale the image up
player_image = pygame.transform.scale(player_image, (50, 50))

# main game loop, used to update all gameplay such as movement, checks, and graphics
while not is_game_over:

    # the loop to get all of the events occurring at any given time
    # events are most often mouse movement, mouse and button clicks, or exit events
    for event in pygame.event.get():
        # if we have a quit type event (exit out) then exit out of the game loop
        if event.type == pygame.QUIT:
            is_game_over = True
        print(event)

    # draw a rectangle on top of the game screen canvas (x, y, width, height)
    # pygame.draw.rect(game_screen, BLACK_COLOR, [350, 350, 100, 100])
    # draw a circle on top of the game screen (x, y, radius)
    # pygame.draw.circle(game_screen, BLACK_COLOR, (400, 300), 50)

    # draw the player image on top of the screen at (x, y) position
    game_screen.blit(player_image, (375, 375))

    # update all game graphics
    pygame.display.update()
    # tick the clock to update everything within the game
    clock.tick(TICK_RATE)

# quit pygame and the program
pygame.quit()
quit()
