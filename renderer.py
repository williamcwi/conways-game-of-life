import pygame

CELL_SIZE = 20
COLS, ROWS = 40, 30

def draw(screen, cells):
    screen.fill((30, 30, 30))

    # Draw the grid
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(
                col * CELL_SIZE,
                row * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )

            pygame.draw.rect(screen, (70, 70, 70), rect, 1)

    # Populate cells
    for col, row in cells:
        rect = pygame.Rect(
            (col * CELL_SIZE) + 1,
            (row * CELL_SIZE) + 1,
            CELL_SIZE -2,
            CELL_SIZE -2
        )
        pygame.draw.rect(screen, (80, 220, 140), rect)