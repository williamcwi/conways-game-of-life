import pygame
from config import WIDTH, HEIGHT, FPS
from renderer import draw
from controls import handle_events
from patterns import PATTERNS, place_pattern, get_start_position

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

clock = pygame.time.Clock()

cells = set()
running = True

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

while running:
    running = handle_events(cells)

    draw(screen, cells)
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()