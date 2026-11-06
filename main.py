import pygame
from config import WIDTH, HEIGHT, FPS, GENERATION_INTERVAL
from renderer import draw
from controls import handle_events
from game import next_generation
from patterns import PATTERNS, place_pattern, get_start_position

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

clock = pygame.time.Clock()

cells = set()
running = True
simulating = False

# Initial pattern
selected = PATTERNS["glider"]
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

last_generation_time = pygame.time.get_ticks()
while running:
    running, simulating = handle_events(cells, simulating)
    now = pygame.time.get_ticks()

    if simulating:
        if now - last_generation_time >= GENERATION_INTERVAL:
            cells = next_generation(cells)
            last_generation_time = now
    else:
        last_generation_time = now

    draw(screen, cells)
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()