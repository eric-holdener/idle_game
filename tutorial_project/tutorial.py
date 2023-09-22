import pygame

# Initialize pygame
pygame.init()

# Class with colors I'll use for the game to avoid retyping
class Colors:
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    white = (255, 255, 255)
    black = (0, 0, 0)
    purple = (127, 0, 255)
    orange = (255, 165, 0)

# Variables for the game
class GameVariables:
    background = Colors.black
    framerate = 60
    font = pygame.font.Font('freesansbold.ttf', 16)
    timer = pygame.time.Clock()
    green_value = 1
    red_value = 2
    orange_value = 3
    white_value = 4
    purple_value = 5

# Set screen size and caption on the window
screen = pygame.display.set_mode([300,450])
pygame.display.set_caption('Not Adventure Capitalist')

# Running the game variable
running = True

def draw_task(color, y_coord, value):
    # Draw circle for the task circle(display, what color, coordinates(x,y), radius, thickness)
    pygame.draw.circle(screen, color, (30, y_coord), 20, 5)

    # Draw rectangle for progress bar(display, color, [x coord, y coord, length, height])
    pygame.draw.rect(screen, color, [70, y_coord - 15, 200, 30])

    # Rectangle for progress bar
    pygame.draw.rect(screen, Colors.black, [75, y_coord - 10, 190, 20])

    # Define text for task
    value_text = GameVariables.font.render(str(value), True, Colors.white)

    # Draw text on screen
    screen.blit(value_text, (16, y_coord - 10))


# Run the game while running = true
while running:

    # Control ticks - 60 ticks per second
    GameVariables.timer.tick(GameVariables.framerate)

    for event in pygame.event.get():
        # If X button is clicked, exit the loop
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with the background color
    screen.fill(GameVariables.background)

    draw_task(Colors.green, 50, GameVariables.green_value)
    draw_task(Colors.red, 110, GameVariables.red_value)
    draw_task(Colors.orange, 170, GameVariables.orange_value)
    draw_task(Colors.white, 230, GameVariables.white_value)
    draw_task(Colors.purple, 290, GameVariables.purple_value)

    # Writes everything onto the screen
    pygame.display.flip()
    

# quit the game
pygame.quit()