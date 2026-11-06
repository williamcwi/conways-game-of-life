import pygame

CELL_SIZE = 20
COLS, ROWS = 40, 30

def handle_events(cells):
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            col = x // CELL_SIZE
            row = y // CELL_SIZE

            cell = (col, row)

            # Check if click is within grid
            if 0 <= col < COLS and 0 <= row < ROWS:

                # Left click: activate cell
                if event.button == 1:
                    cells.add(cell)

                # Right click: deactivate cell
                elif event.button == 3:
                    cells.discard(cell)

    return True