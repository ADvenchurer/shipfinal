import random
import itertools
import pgzrun

WIDTH = 4000
HEIGHT = 400

# Block positions for looping movement
BLOCK_POSITIONS = [
    (350, 50),
    (350, 350),
    (50, 350),
    (50, 50)
]

block_positions = itertools.cycle(BLOCK_POSITIONS)

# Actors
block = Actor('block', center=(50, 50))
ship = Actor('ship', center=(200, 200))

def move_block():
    """Move the block to the next position in the cycle."""
    block.center = next(block_positions)

def next_ship_target():
    """Select a new random position for the ship and rotate it towards the target."""
    ship.target = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
    animate(ship, angle=ship.angle + 90, duration=0.5, on_finished=move_ship)

def move_ship():
    """Move the ship to its target position."""
    animate(ship, center=ship.target, duration=1, on_finished=next_ship_target)

def draw():
    """Draw everything on the screen."""
    screen.clear()
    block.draw()
    ship.draw()

# Schedule block movement every 2 seconds
clock.schedule_interval(move_block, 2)

# Start the ship's random movement
next_ship_target()

pgzrun.go()

