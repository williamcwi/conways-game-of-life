import pygame
from config import WIDTH, HEIGHT, FPS
from renderer import draw
from controls import handle_events

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

clock = pygame.time.Clock()

cells = set()
running = True

# Initial cells
cells.add((5, 5))
cells.add((6, 5))
cells.add((7, 5))

while running:
    running = handle_events(cells)

    draw(screen, cells)
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()