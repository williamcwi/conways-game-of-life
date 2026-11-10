import pygame
from config import WIDTH, SIDEBAR_WIDTH
from patterns import PATTERNS

PADDING = 16
BUTTON_WIDTH = SIDEBAR_WIDTH - PADDING * 2

PLAY_BUTTON = pygame.Rect(WIDTH + PADDING, 48, BUTTON_WIDTH, 40)
STEP_BUTTON = pygame.Rect(WIDTH + PADDING, 96, BUTTON_WIDTH, 40)

PATTERN_BUTTONS = {}

for index, name in enumerate(PATTERNS):
    PATTERN_BUTTONS[name] = pygame.Rect(
        WIDTH + PADDING,
        228 + index * 68,
        BUTTON_WIDTH,
        60,
    )