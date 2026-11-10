import pygame
from config import WIDTH, HEIGHT, SIDEBAR_WIDTH, CELL_SIZE, COLS, ROWS, BACKGROUND_COLOUR, GRID_COLOUR, CELL_COLOUR, SIDEBAR_COLOUR
from patterns import PATTERNS
from ui import PLAY_BUTTON, STEP_BUTTON, PATTERN_BUTTONS

def draw(screen, cells, font, simulating):
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

    draw_sidebar(screen, font, simulating)

    # Populate cells
    for col, row in cells:
        rect = pygame.Rect(
            (col * CELL_SIZE) + 1,
            (row * CELL_SIZE) + 1,
            CELL_SIZE -2,
            CELL_SIZE -2
        )
        pygame.draw.rect(screen, CELL_COLOUR, rect)

def draw_button(screen, rect, label, font):
    pygame.draw.rect(screen, (60, 60, 60), rect, border_radius=6)
    pygame.draw.rect(screen, (90, 90, 90), rect, width=1, border_radius=6)

    text = font.render(label, True, (230, 230, 230))
    screen.blit(text, text.get_rect(center=rect.center))


def draw_sidebar(screen, font, simulating):
    sidebar = pygame.Rect(WIDTH, 0, SIDEBAR_WIDTH, HEIGHT)
    pygame.draw.rect(screen, SIDEBAR_COLOUR, sidebar)

    padding = 16
    x = WIDTH + padding

    # Simulation controls
    heading = font.render("SIMULATION", True, CELL_COLOUR)
    screen.blit(heading, (x, 16))

    label = "Pause" if simulating else "Play"
    draw_button(screen, PLAY_BUTTON, label, font)
    draw_button(screen, STEP_BUTTON, "Step one generation", font)

    shortcuts = font.render("Space: play/pause   N: step", True, (170, 170, 170))
    screen.blit(shortcuts, (x, 148))

    pygame.draw.line(
        screen,
        GRID_COLOUR,
        (x, 180),
        (WIDTH + SIDEBAR_WIDTH - padding, 180),
    )

    # Pattern templates
    heading = font.render("PATTERNS", True, CELL_COLOUR)
    screen.blit(heading, (x, 196))

    preview_size = 6

    for name, rect in PATTERN_BUTTONS.items():
        pattern = PATTERNS[name]
        x, y = rect.topleft

        pygame.draw.rect(screen, (60, 60, 60), rect, border_radius=6)

        # Draw a miniature version of the pattern.
        for col, row in pattern["cells"]:
            preview_cell = pygame.Rect(
                x + 12 + col * preview_size,
                y + 14 + row * preview_size,
                preview_size - 1,
                preview_size - 1,
            )
            pygame.draw.rect(screen, CELL_COLOUR, preview_cell)

        label = name.title() if name in ("blank", "glider") else name.upper()
        text = font.render(label, True, (230, 230, 230))
        screen.blit(text, (x + 72, y + 20))