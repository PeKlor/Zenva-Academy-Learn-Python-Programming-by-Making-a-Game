import pygame

# size of the screen
SCREEN_TITLE = 'Crossy RPG'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
clock = pygame.time.Clock()


class Game:

    # FPS with the typical rate of 60
    TICK_RATE = 60

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        # create the window of the specified size in white to display the game
        self.game_screen = pygame.display.set_mode((width, height))
        # set the game window color to white
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

    def run_game_loop(self):
        is_game_over = False
        # main game loop, used to update all gameplay such as movement, checks, and graphics
        while not is_game_over:

            # the loop to get all of the events occurring at any given time
            # events are most often mouse movement, mouse and button clicks, or exit events
            for event in pygame.event.get():
                # if we have a quit type event (exit out) then exit out of the game loop
                if event.type == pygame.QUIT:
                    is_game_over = True

                print(event)

            # update all game graphics
            pygame.display.update()
            # tick the clock to update everything within the game
            clock.tick(self.TICK_RATE)


class GameObject:

    def __init__(self, image_path, x, y, width, height):
        # load the player image from the file directory
        object_image = pygame.image.load(image_path)
        # scale the image up
        self.image = pygame.transform.scale(object_image, (width, height))

        self.x_pos = x
        self.y_pos = y

    def draw(self, background):
        # "blit" means draw; we draw the background with the image, the left corner of it being (x, y)
        background.blit(self.image, (self.x_pos, self.y_pos))


pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()


# quit pygame and the program
pygame.quit()
quit()


# draw a rectangle on top of the game screen canvas (x, y, width, height)
# pygame.draw.rect(game_screen, BLACK_COLOR, [350, 350, 100, 100])
# draw a circle on top of the game screen (x, y, radius)
# pygame.draw.circle(game_screen, BLACK_COLOR, (400, 300), 50)

# draw the player image on top of the screen at (x, y) position
# game_screen.blit(player_image, (375, 375))
