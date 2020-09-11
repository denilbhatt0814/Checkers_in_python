import pygame
from pygame import event
from checkers.constants import WIDTH, HEIGHT
from checkers.board import Board

FPS = 30
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Checkers")    

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)
        
        # The Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        
        # Draws all the sqaures and peices on board
        board.draw(WIN) 
        pygame.display.update() # For screen updation

    pygame.quit()                    

main()