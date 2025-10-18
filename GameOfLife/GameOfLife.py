import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1440, 780
CELL_SIZE = 5
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255,255, 135)

# Function to create a random initial state
def create_random_state():
    return np.random.choice([0, 1], size=(ROWS, COLS), p=[0.9, 0.1])

# Function to draw the grid
def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y))

# Function to draw the current state of the game
def draw_state(state):
    for y in range(ROWS):
        for x in range(COLS):
            if state[y, x] == 1:
                pygame.draw.rect(screen, YELLOW, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Function to update the state of the game according to the rules of Conway's Game of Life
def update_state(state):
    new_state = np.zeros((ROWS, COLS), dtype=int)
    for y in range(ROWS):
        for x in range(COLS):
            neighbors = sum([state[(y + i) % ROWS, (x + j) % COLS] for i in range(-1, 2) for j in range(-1, 2)]) - state[y, x]
            if state[y, x] == 1 and (neighbors < 2 or neighbors > 3):
                new_state[y, x] = 0
            elif state[y, x] == 0 and neighbors == 3:
                new_state[y, x] = 1
            else:
                new_state[y, x] = state[y, x]
    return new_state

# Main game loop
def main():
    clock = pygame.time.Clock()

    # Create initial state
    state = create_random_state()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        draw_grid()
        draw_state(state)
        state = update_state(state)

        pygame.display.flip()
        clock.tick(10)  # Set FPS

    pygame.quit()

if __name__ == "__main__":
    main()