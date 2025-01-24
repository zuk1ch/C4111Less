import random
import pygame
import sys
from pygame.locals import *


pygame.init()


WIDTH, HEIGHT = 800, 600
TILE_SIZE = 40
ROWS = HEIGHT // TILE_SIZE
COLS = WIDTH // TILE_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (192, 192, 192)
DARK_GRAY = (128, 128, 128)
RED = (255, 0, 0)


font = pygame.font.Font(None, 36)


NUM_MINES = 20

def create_field():
    field = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    mines = set()
    while len(mines) < NUM_MINES:
        mine = (random.randint(0, ROWS - 1), random.randint(0, COLS - 1))
        mines.add(mine)
    for (r, c) in mines:
        field[r][c] = -1
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and field[nr][nc] != -1:
                    field[nr][nc] += 1
    return field, mines

def draw_field(field, revealed, flagged):
    for r in range(ROWS):
        for c in range(COLS):
            x, y = c * TILE_SIZE, r * TILE_SIZE
            rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
            if revealed[r][c]:
                pygame.draw.rect(screen, WHITE, rect)
                if field[r][c] == -1:
                    pygame.draw.circle(screen, RED, rect.center, TILE_SIZE // 3)
                elif field[r][c] > 0:
                    text = font.render(str(field[r][c]), True, BLACK)
                    screen.blit(text, text.get_rect(center=rect.center))
            else:
                pygame.draw.rect(screen, DARK_GRAY, rect)
                if flagged[r][c]:
                    pygame.draw.circle(screen, RED, rect.center, TILE_SIZE // 4)
            pygame.draw.rect(screen, BLACK, rect, 1)

def reveal_cell(field, revealed, r, c):
    if revealed[r][c]:
        return
    revealed[r][c] = True
    if field[r][c] == 0:
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and not revealed[nr][nc]:
                    reveal_cell(field, revealed, nr, nc)

def check_win(revealed, mines):
    for r, c in mines:
        if revealed[r][c]:
            return False
    for r in range(ROWS):
        for c in range(COLS):
            if not revealed[r][c] and (r, c) not in mines:
                return False
    return True

field, mines = create_field()
revealed = [[False for _ in range(COLS)] for _ in range(ROWS)]
flagged = [[False for _ in range(COLS)] for _ in range(ROWS)]

running = True
while running:
    screen.fill(GRAY)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            r, c = y // TILE_SIZE, x // TILE_SIZE

            if event.button == 1:
                if not flagged[r][c]:
                    if field[r][c] == -1:
                        print("Гра закінчена!")
                        running = False
                    else:
                        reveal_cell(field, revealed, r, c)

            elif event.button == 3:
                flagged[r][c] = not flagged[r][c]

    draw_field(field, revealed, flagged)

    if check_win(revealed, mines):
        print("Ти виграв!")
        running = False


    pygame.display.flip()

pygame.quit()
sys.exit()


#робив гру трохи підгялдав у ютуб та інші джерела тому що були проблеми, все ще не виводить що гра закінчена чи виграна