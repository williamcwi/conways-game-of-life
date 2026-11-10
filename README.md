# Conway's Game of Life

An interactive Python implementation of Conway's Game of Life, built with Pygame. Draw your own starting cells or choose a built-in pattern, then watch the simulation evolve or advance it one generation at a time.

## Getting started

You need Python 3, pip, and a desktop environment to display the Pygame window.

From the project directory, install Pygame and start the application:

```sh
python -m pip install pygame
python main.py
```

On Windows, you can use `py` instead of `python`. On macOS or Linux, you may need `python3`.

The application opens paused with a blank grid. Click cells to create a pattern, or select one from the sidebar, then press **Space** or click **Play**.

## Controls

| Input | Action |
| --- | --- |
| Left-click a grid cell | Make the cell alive |
| Right-click a grid cell | Make the cell dead |
| **Space** or **Play / Pause** | Start or pause the simulation |
| **N** or **Step one generation** | Advance one generation while paused |
| **R** | Restore the most recently selected pattern and pause |
| Click a pattern in the sidebar | Replace the grid with that pattern and pause |
| Close the window | Exit the application |

Cells can be edited while paused or running. Reset restores the selected template (or the configured startup pattern), so manual edits are not saved as the reset state. Select **Blank** to clear the grid.

## Built-in patterns

- **Blank**: an empty grid for creating your own patterns.
- **Glider**: a small pattern that travels diagonally.
- **LWSS**: a lightweight spaceship.
- **MWSS**: a middleweight spaceship.
- **HWSS**: a heavyweight spaceship.

The glider starts near the top-left corner; the spaceships start near the right edge, vertically centred. Sidebar buttons include miniature pattern previews.

## Rules

Each cell has eight neighbours, including diagonals. Every generation updates all cells using the previous generation:

- A live cell survives with two or three live neighbours.
- A dead cell becomes alive with exactly three live neighbours.
- All other cells die or remain dead.

The grid is finite and does not wrap around at the edges.

## Configuration

Edit [config.py](config.py) before starting the application to change the display and simulation settings.

| Setting | Default | Purpose |
| --- | --- | --- |
| `WIDTH` / `HEIGHT` | `800` / `600` | Grid area dimensions in pixels |
| `SIDEBAR_WIDTH` | `240` | Sidebar width in pixels |
| `CELL_SIZE` | `20` | Cell size in pixels |
| `FPS` | `60` | Frame rate limit for rendering and input |
| `GENERATION_INTERVAL` | `200` | Milliseconds between generations; lower values run faster |
| `INITIAL_PATTERN` | `"blank"` | Startup pattern: `"blank"`, `"glider"`, `"lwss"`, `"mwss"`, or `"hwss"` |

The defaults produce a 40-column by 30-row grid in a 1040 by 600 pixel window, advancing approximately five generations per second while running. Colours are also defined in `config.py` as RGB tuples.

## Project structure

| File | Responsibility |
| --- | --- |
| [main.py](main.py) | Pygame setup and the main simulation loop |
| [game.py](game.py) | Neighbour counting and generation updates |
| [controls.py](controls.py) | Mouse, keyboard, and sidebar interactions |
| [renderer.py](renderer.py) | Drawing the grid, live cells, and sidebar |
| [ui.py](ui.py) | Button positions and dimensions |
| [patterns.py](patterns.py) | Pattern definitions and placement helpers |
| [config.py](config.py) | Display, colour, and timing settings |

## License

Licensed under the Apache License 2.0. See [LICENSE](LICENSE).
