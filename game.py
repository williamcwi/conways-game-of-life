from config import COLS, ROWS

cells = set()

# Initial cells
cells.add((5, 5))
cells.add((6, 5))
cells.add((7, 5))

NEIGHBOUR_OFFSETS = (
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
)

def count_neighbours(cells, col, row):
    live_count = 0
    for x, y in NEIGHBOUR_OFFSETS:
        new_col, new_row = col + x, row + y
        if (new_col, new_row) in cells:
            live_count += 1
    return live_count

def next_generation(cells):
    next_cells = set()

    for col in range(COLS):
        for row in range(ROWS):
            neighbours = count_neighbours(cells, col, row)
            if neighbours <= 1 or neighbours >= 4:
                pass
            if (col, row) in cells and neighbours == 2:
                next_cells.add((col, row))
            if neighbours == 3:
                next_cells.add((col, row))
    return next_cells