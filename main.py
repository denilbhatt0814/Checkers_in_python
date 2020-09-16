import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE 
from checkers.game import Game

FPS = 30
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Checkers")    

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y//SQUARE_SIZE
    col = x//SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        game = Game(WIN)

        # The Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                
            
        
        # Draws all the sqaures and peices on board
        game.update() # For screen updation

    pygame.quit()                    

main()