import pygame
from config import CELL_SIZE, COLS, ROWS
from game import advance_generation
from patterns import PATTERNS, get_start_position, place_pattern
from ui import PLAY_BUTTON, STEP_BUTTON, PATTERN_BUTTONS

def handle_events(cells, simulating, initial_cells):
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
            
            if event.button == 1:
                if PLAY_BUTTON.collidepoint(event.pos):
                    simulating = not simulating

                elif STEP_BUTTON.collidepoint(event.pos):
                    if not simulating:
                        advance_generation(cells)
                else:
                    for name, rect in PATTERN_BUTTONS.items():
                        if rect.collidepoint(event.pos):
                            selected = PATTERNS[name]
                            start_col, start_row = get_start_position(
                                selected["cells"],
                                selected["placement"],
                            )

                            cells.clear()
                            place_pattern(
                                cells,
                                selected["cells"],
                                start_col,
                                start_row,
                            )

                            initial_cells.clear()
                            initial_cells.update(cells)
                            simulating = False
                            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                if not simulating:
                    advance_generation(cells)

            if event.key == pygame.K_SPACE:
                simulating = not simulating

            if event.key == pygame.K_r:
                cells.clear()
                cells.update(initial_cells)
                simulating = False

    return True, simulating