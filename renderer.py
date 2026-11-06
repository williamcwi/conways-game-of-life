import pygame
from config import CELL_SIZE, COLS, ROWS, BACKGROUND_COLOUR, GRID_COLOUR, CELL_COLOUR

def draw(screen, cells):
    screen.fill(BACKGROUND_COLOUR)

    # Draw the grid
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(
                col * CELL_SIZE,
                row * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )

            pygame.draw.rect(screen, GRID_COLOUR, rect, 1)

    # Populate cells
    for col, row in cells:
        rect = pygame.Rect(
            (col * CELL_SIZE) + 1,
            (row * CELL_SIZE) + 1,
            CELL_SIZE -2,
            CELL_SIZE -2
        )
        pygame.draw.rect(screen, CELL_COLOUR, rect)