from .constants import RED, SQUARE_SIZE, GREY, CROWN
import pygame

class Piece:

    PADDING = 15
    OUTLINE = 3

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False

        #setting direction for peice to move
        if self.color == RED:
            self.dircetion = -1
        else:
            self.direction = 1 

        self.x = 0 
        self.y = 0 
        self.calc_pos()

    def calc_pos(self):
        self.x = (SQUARE_SIZE * self.col) + (SQUARE_SIZE // 2)
        self.y = (SQUARE_SIZE * self.row) + (SQUARE_SIZE // 2)
            
    def make_king(self):
        self.king  = True

    def draw(self, win):
        radius = (SQUARE_SIZE//2) - self.PADDING # Calc. of radius of main circle
        
        # Adding a bigger circle for outline
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        
        # Finall creating the main circle peice over the outline circle
        pygame.draw.circle(win, self.color, (self.x, self.y),radius)

        # Draws crown on king piece
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    def move(self,row,col):
        """THIS MOVES THE PIECE ON BOARD"""
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)
            