import pygame
from config import WINDOW_WIDTH, HEIGHT, FPS, GENERATION_INTERVAL, INITIAL_PATTERN
from renderer import draw
from controls import handle_events
from game import next_generation
from patterns import PATTERNS, place_pattern, get_start_position

pygame.init()
font = pygame.font.Font(None, 22)

screen = pygame.display.set_mode((WINDOW_WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

clock = pygame.time.Clock()

cells = set()
running = True
simulating = False

# Initial pattern
selected = PATTERNS[INITIAL_PATTERN]
start_col, start_row = get_start_position(
    selected["cells"],
    selected["placement"]
)
place_pattern(
    cells,
    selected["cells"],
    start_col,
    start_row,
)
initial_cells = cells.copy()

last_generation_time = pygame.time.get_ticks()
while running:
    running, simulating = handle_events(cells, simulating, initial_cells)
    now = pygame.time.get_ticks()

    if simulating:
        if now - last_generation_time >= GENERATION_INTERVAL:
            cells = next_generation(cells)
            last_generation_time = now
    else:
        last_generation_time = now

    draw(screen, cells, font, simulating)
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()