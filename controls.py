import pygame
from config import CELL_SIZE, COLS, ROWS
from game import next_generation

def handle_events(cells, simulating):
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            return False, simulating

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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                new_cells = next_generation(cells)
                cells.clear()
                cells.update(new_cells)

            if event.key == pygame.K_SPACE:
                simulating = not simulating
    return True, simulating