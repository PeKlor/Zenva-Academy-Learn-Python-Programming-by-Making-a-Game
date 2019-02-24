# # Basics No.2
#
# x_pos = 5
# speed = 2.5
# is_game_over = False
# char_name = input("Enter your name: ")
#
# print(type(x_pos))
#
# x_pos = speed
# is_not_game_over = not is_game_over
# x_pos += speed
# print("Now your new name is " + char_name + "123")



# # Basics No.3
# # Tuples
# size = (100, 200)
# width = size[0]
# height = size[1]
# new_size = size + (300,) + size
# # del new_size
# # print(new_size)
# # print("The length of size is " + str(len(size)) + ", the max value is " + str(max(size)) + " and the min value is " + str(min(size)))
# does_contain = 100 in size   # true
# # print(does_contain)
#
# # Arrays/Lists
# movement = [5, -2, -3, 4, -1]   # 5 to the right, 2 to the left etc.
# movement[0] = 7   # movement = [7, -2, -3, 4, -1]
# movement.append(-5)   # movement = [7, -2, -3, 4, -1, -5]
# movement.remove(-3)   # movement = [7, -2, 4, -1, -5]
#
# # Dictionaries
# starting_positions = {'p_0': 50, 'p_1': 100, 'p_2': 150}
# print(starting_positions['p_0'])   # 50
# print(starting_positions.keys())   # ['p_0', 'p_1', 'p_2']



# # Basics No.4
# # if statements
# is_game_over = False
# p0_xPos = 0   # player 0
# e0_xPos = 3   # enemy 0
# e1_xPos = 5
#
# p0_xPos += 2
# if p0_xPos == e0_xPos:
#     is_game_over = True
# elif p0_xPos == e1_xPos:
#     is_game_over = True
# else:
#     e0_xPos += 1
#     e1_xPos += 1
#
# if p0_xPos == e0_xPos or p0_xPos == e1_xPos:
#     is_game_over = True
# else:
#     e0_xPos += 1
#     e1_xPos += 1


# # Basics No.5
# # while and for in loops
# is_game_over = False
# p_xPos = 2
# e_xPos = 3
# end_xPos = 10
#
# while not is_game_over:
#     print(p_xPos)
#     print(e_xPos)
#     if p_xPos == e_xPos:
#         print('You lose')
#         is_game_over = True
#     elif p_xPos >= end_xPos:
#         print('You win')
#         is_game_over = True
#     else:
#         p_xPos += 3
#         e_xPos += 1
#
# x_pos = 5
# movements = [1, -2, 6, -3, -2, 4]
# for movement in movements:
#     x_pos += movement
# print(x_pos)



# # Basics No.6
# # functions
# x_pos = 0
# e_x_pos = 4
#
# def move():
#     global x_pos # retrieves that global variable
#     x_pos += 1
#
# move()
#
# def move_by(amount):
#     global x_pos
#     x_pos += amount
#
# def check_for_collision():
#     global x_pos
#     global e_x_pos
#     if x_pos == e_x_pos:
#         return True
#     else:
#         return False
#
# move_by(3)
# did_collide = check_for_collision()
# print(x_pos)
# print(did_collide)




# # Basics No.7
# # classes and objects
#
class GameCharacter:

    speed = 5

    def __init__(self, name, width, height, x_pos, y_pos):
        self.name = name
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, by_x_amount, by_y_amount):
        self.x_pos += by_x_amount
        self.y_pos += by_y_amount
#
#
# character_0 = GameCharacter('char_0', 50, 100, 100, 100)
# print(character_0.name)   # prints char_0
# character_0.name = 'char_1'
# print(character_0.name)   # prints char_1
#
# character_0.move(50, 100)
# print(character_0.x_pos)   # prints 150
# print(character_0.y_pos)   # prints 200



# Basics No.8
# subclasses, superclasses and inheritance

# needs the above class
class PlayerCharacter(GameCharacter):

    speed = 10

    def __init__(self, name, x_pos, y_pos):
        super().__init__(name, 100, 100, x_pos, y_pos)

    def move(self, by_y_amount):
        super().move(0, by_y_amount)


player_character = PlayerCharacter('P_character', 500, 500)
print(player_character.name)
player_character.move(100)
print(player_character.x_pos)   # prints 500
print(player_character.y_pos)   # prints 600

