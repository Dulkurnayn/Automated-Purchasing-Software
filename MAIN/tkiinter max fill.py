import pygame
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 200
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Loading Bar")

# Loading bar parameters
loading_bar_width = 300
loading_bar_height = 20
loading_bar_x = (WIDTH - loading_bar_width) // 2
loading_bar_y = HEIGHT // 2

# Button parameters
button_width = 130
button_height = 40
button_x = (WIDTH - button_width) // 2
button_y = HEIGHT // 2 + 50

# Font
font = pygame.font.Font(None, 36)

# Loading variables
loading_progress = 0

# Main game loop
clock = pygame.time.Clock()
running = True
loading_complete = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    # Update
    if loading_progress < 100:
        loading_progress += 1
    else:
        loading_complete = True

    # Draw
    screen.fill(WHITE)

    # Draw loading bar background
    pygame.draw.rect(screen, BLACK, (loading_bar_x - 2, loading_bar_y - 2, loading_bar_width + 4, loading_bar_height + 4))
    # Draw loading bar
    pygame.draw.rect(screen, (0, 128, 0), (loading_bar_x, loading_bar_y, loading_progress * loading_bar_width // 100, loading_bar_height))

    # Draw button
    pygame.draw.rect(screen, (0, 0, 255), (button_x, button_y, button_width, button_height))
    button_text = font.render("Press Me!", True, WHITE)
    screen.blit(button_text, (button_x + 20, button_y + 10))

    pygame.display.flip()

    # Check if loading is complete and wait for button press
    if loading_complete:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if button_x < mouse_x < button_x + button_width and button_y < mouse_y < button_y + button_height:
            click, _, _ = pygame.mouse.get_pressed()
            if click:
                running = False

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()

# Close the window
sys.exit()