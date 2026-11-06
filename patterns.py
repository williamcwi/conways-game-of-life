from config import COLS, ROWS

GLIDER = {
            (1, 0),
                    (2, 1),
    (0, 2), (1, 2), (2, 2),
}

LWSS = {
            (1, 0),                 (4, 0),
    (0, 1),
    (0, 2),                         (4, 2),
    (0, 3), (1, 3), (2, 3), (3, 3),
}

MWSS = {
                            (3, 0),
            (1, 1),                         (5, 1),
    (0, 2),
    (0, 3),                                 (5, 3), 
    (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
}

HWSS = {
                            (3, 0), (4, 0),
            (1, 1),                                 (6, 1),
    (0, 2),
    (0, 3),                                         (6, 3),
    (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4),
}

PATTERNS = {
    "glider": {
        "cells": GLIDER,
        "placement": "top_left",
    },
    "lwss": {
        "cells": LWSS,
        "placement": "middle_right",
    },
    "mwss": {
        "cells": MWSS,
        "placement": "middle_right",
    },
    "hwss": {
        "cells": HWSS,
        "placement": "middle_right",
    },
}

def get_start_position(pattern, placement):
    width = max(col for col, row in pattern) + 1
    height = max(row for col, row in pattern) + 1
    margin = 2

    if placement == "top_left":
        return margin, margin
    elif placement == "middle_right":
        return COLS - width - margin, (ROWS - height) // 2

    raise ValueError(f"Unknown placement: {placement}")

def place_pattern(cells, pattern, start_col, start_row):
    for col, row in pattern:
        cells.add((col + start_col, row + start_row))