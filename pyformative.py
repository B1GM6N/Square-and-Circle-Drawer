#################################
#       Peyton Germann          #
#     Pygame OOP Formative      #
#       Nov, 22, 2022           #
#################################
squa = ["Square", "square", "s", "S"]
BLUE = (0, 0, 255)
BROWN = (150, 75, 0)
WHITE = (255, 255, 255)
size = (700,400)
import random, pygame, time
from pygame.locals import *
def time(n):
    from time import sleep
    sleep(n)
print("Would you like to draw a square or a circle?")
sc = input(">")
screen = pygame.display.set_mode(size)

class shape:
    
    def __init__(self, color):
        self.color = color
        
    def circle(self, x, y):
        pygame.draw.circle(screen, self.color,(x, y), 20)
    
    def square(self, x, y):
        pygame.draw.rect(screen, self.color, pygame.Rect(x, y, 20, 20))
# Initialize Pygame
pygame.init()
running = True
screen.fill(WHITE)
pygame.display.update()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    shape1 = shape(BLUE)
    if sc in squa:
        shape1.square(300, 150)

    else:
        shape1.circle(300, 150)
    pygame.display.update()
    draw = True
pygame.display.quit()

