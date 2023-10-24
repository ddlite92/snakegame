import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the game window
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Initialize the snake and food
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(WIDTH), random.randrange(HEIGHT)]
food_spawn = True

# Set the direction of the snake
direction = 'RIGHT'

# Game loop
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    # Update snake position based on direction
    if direction == 'UP':
        new_head = [snake_pos[0], snake_pos[1] - 10]
    if direction == 'DOWN':
        new_head = [snake_pos[0], snake_pos[1] + 10]
    if direction == 'LEFT':
        new_head = [snake_pos[0] - 10, snake_pos[1]]
    if direction == 'RIGHT':
        new_head = [snake_pos[0] + 10, snake_pos[1]]

    snake_body.insert(0, new_head)
    snake_pos = new_head

    # Check if snake has eaten food
    if snake_pos == food_pos:
        food_spawn = False
    else:
        snake_body.pop()

    # Spawn new food if needed
    if not food_spawn:
        food_pos = [random.randrange(WIDTH), random.randrange(HEIGHT)]
        food_spawn = True

    # Draw the snake and food
    screen.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Update the display
    pygame.display.update()

    # Set the game speed
    pygame.time.Clock().tick(10)
