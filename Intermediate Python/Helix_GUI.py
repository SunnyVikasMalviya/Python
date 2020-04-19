import pygame
import random

HELIX_LENGTH = 26

WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HELIX")
clock = pygame.time.Clock()

class Blob(object):
    def __init__(self, color, x, i):
        self.color = color
        self.x = x
        self.y = 300+i
        self.size = 10
        self.direction = 1
        return
    def move(self):
        if self.y > 500 or self.y < 100:
            self.direction = -self.direction
        self.y += (2 * self.direction)

def draw_environment(blobs):
    game_display.fill(WHITE)
    for blob in blobs:
        pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
        blob.move()
    pygame.display.update()
    

def main():
    blobs = [Blob(ORANGE, 20+(i*30), 5*i) for i in range(HELIX_LENGTH)]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_environment(blobs)
        clock.tick(60)

if __name__ == '__main__':
    main()
