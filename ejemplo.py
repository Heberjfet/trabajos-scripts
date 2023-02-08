#chuflux
# def work(dato):
    # if dato != 'cafe':
        # print('descansando')
    # else:
        # print('programando')

# work(input('ingrese cafe:'))

# prueba de worksapce
# segir haciendo mas pruebas 
# mejorar mas el uso de esta herramienta

import turtle
import time

# Initialize pygame
turtle.Turtle()

# Set the width and height of the screen (width, height).
size = (700, 500)
screen = turtle.display.set_mode(size)

turtle.display.set_caption("My Snake Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = turtle.time.Clock()

# Initial snake block position
snake_block = turtle.Surface((10,10))
snake_block.fill((255,255,255))
snake_x = 300
snake_y = 300

# Main game loop
while not done:
    # --- Main event loop
    for event in turtle.event.get():
        if event.type == turtle.QUIT:
            done = True

# ---