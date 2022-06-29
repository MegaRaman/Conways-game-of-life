import sys
import random
import copy
import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("PyGame")
screen.fill((0, 0, 0))
clock = pygame.time.Clock()


def draw_cell(x, y, color):
    size = 9
    pygame.draw.rect(screen, color, (x * 10, y * 10, size, size))


def random_field(cells):
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            if random.random() <= 0.15:
                cells[i][j] = True
                draw_cell(i, j, (0, 255, 0))
            else:
                draw_cell(i, j, (0, 0, 0))
    return cells


def neighbours(x, y, world):
    count = 0
    list_of_neighbours = [(x - 1, y + 1), (x, y + 1), (x + 1, y + 1),
                          (x - 1, y),                   (x + 1, y),
                          (x - 1, y - 1), (x, y - 1), (x + 1, y - 1)]
    for neighbourX, neighbourY in list_of_neighbours:
        if 0 <= neighbourX < len(world) and 0 <= neighbourY < len(world[0]):
            if world[neighbourX][neighbourY]:
                count += 1
    return count == 3 or count == 2 and world[x][y]


def evolution(world):
    new_world = copy.deepcopy(world)
    for i in range(len(world)):
        for j in range(len(world[i])):
            if neighbours(i, j, world):
                new_world[i][j] = True
                draw_cell(i, j, (0, 255, 0))
            else:
                new_world[i][j] = False
                draw_cell(i, j, (0, 0, 0))
    return new_world


cells = [[False for _ in range(40)] for _ in range(60)]
cells = random_field(cells)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    cells = evolution(cells)
    pygame.display.update()
    clock.tick(10)