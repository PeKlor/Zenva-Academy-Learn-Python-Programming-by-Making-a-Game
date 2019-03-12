import pygame

# size of the screen
SCREEN_TITLE = 'Crossy RPG'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('comicsans', 75)


class Game:

    # FPS with the typical rate of 60
    TICK_RATE = 60

    def __init__(self, image_path, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        # create the window of the specified size in white to display the game
        self.game_screen = pygame.display.set_mode((width, height))
        # set the game window color to white
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

        # load and set the background image for the scene
        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image, (width, height))

    def run_game_loop(self):
        is_game_over = False
        did_win = False
        direction = 0

        player_character = PlayerCharacter('player.png', 375, 700, 50, 50)
        enemy_0 = NonPlayerCharacter('enemy.png', 20, 400, 50, 50)
        treasure = GameObject('treasure.png', 375, 50, 50, 50)

        # main game loop, used to update all gameplay such as movement, checks, and graphics
        while not is_game_over:

            # the loop to get all of the events occurring at any given time
            # events are most often mouse movement, mouse and button clicks, or exit events
            for event in pygame.event.get():
                # if we have a quit type event (exit out) then exit out of the game loop
                if event.type == pygame.QUIT:
                    is_game_over = True
                # detect when key is pressed down
                elif event.type == pygame.KEYDOWN:
                    # move up if the Up-Key is pressed
                    if event.key == pygame.K_UP:
                        direction = 1
                    # move down if the Down-Key is pressed
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                # detect when key is released
                elif event.type == pygame.KEYUP:
                    # stop movement when a key is no longer pressed
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                print(event)

            # redraw the screen to be a blank white window
            self.game_screen.fill(WHITE_COLOR)
            # draw the image onto the background
            self.game_screen.blit(self.image, (0, 0))

            # draw the treasure
            treasure.draw(self.game_screen)

            # update the player position
            player_character.move(direction, self.height)
            # draw the player at the new position
            player_character.draw(self.game_screen)

            # move and draw the enemy character
            enemy_0.move(self.width)
            enemy_0.draw(self.game_screen)

            # end the game if there is a collision between enemy or treasure
            # close the game if we lose, restart the game loop if we win
            if player_character.detect_collision(enemy_0):
                is_game_over = True
                did_win = False
                text = font.render('You lose! :(', True, BLACK_COLOR)
                self.game_screen.blit(text, (275, 350))
                pygame.display.update()
                clock.tick(1)
                break
            elif player_character.detect_collision(treasure):
                is_game_over = True
                did_win = True
                text = font.render('You win! :)', True, BLACK_COLOR)
                self.game_screen.blit(text, (275, 350))
                pygame.display.update()
                clock.tick(1)
                break

            # update all game graphics
            pygame.display.update()
            # tick the clock to update everything within the game
            clock.tick(self.TICK_RATE)

        # restart the game loop if we won
        # break out of game loop and quit if we lose
        if did_win:
            # recursion
            self.run_game_loop()
        else:
            return


class GameObject:

    def __init__(self, image_path, x, y, width, height):
        # load the player image from the file directory
        object_image = pygame.image.load(image_path)
        # scale the image up
        self.image = pygame.transform.scale(object_image, (width, height))

        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height

    def draw(self, background):
        # "blit" means draw; we draw the background with the image, the left corner of it being (x, y)
        background.blit(self.image, (self.x_pos, self.y_pos))


# the class to represent the character controlled by the player
class PlayerCharacter(GameObject):

    # how many tiles the character moves per second
    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    # move function will move character up if direction > 0 and down if < 0
    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED
        # make sure the character never goes past the bottom of the screen
        if self.y_pos >= max_height - 40:
            self.y_pos = max_height - 40

    # return False (no collision) if y positions and x positions do not overlap
    # return True (collision) if x and y positions overlap
    def detect_collision(self, other_body):
        # if the character is below the other body
        if self.y_pos > other_body.y_pos + other_body.height:
            return False
        # if the character is above the other body
        elif self.y_pos + self.height < other_body.y_pos:
            return False
        # if the character is to the right of the other body
        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        # if the character is to the left of the other body
        elif self.x_pos + self.width < other_body.x_pos:
            return False
        # any other case
        return True


# the class to represent the enemies moving left to right and right to left
class NonPlayerCharacter(GameObject):

    # how many tiles the character moves per second
    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    # move function will move the character right once it hits the far left of the screen
    # and left once it hits the far right of the screen
    def move(self, max_width):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - 40:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED


pygame.init()

new_game = Game('background.png', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()

# Load the player image from the file directory
# player_image = pygame.image.load('player.png')
# Scale the image up
# player_image = pygame.transform.scale(player_image, (50, 50))

# quit pygame and the program
pygame.quit()
quit()

# draw a rectangle on top of the game screen canvas (x, y, width, height)
# pygame.draw.rect(game_screen, BLACK_COLOR, [350, 350, 100, 100])
# draw a circle on top of the game screen (x, y, radius)
# pygame.draw.circle(game_screen, BLACK_COLOR, (400, 300), 50)

# draw the player image on top of the screen at (x, y) position
# game_screen.blit(player_image, (375, 375))
