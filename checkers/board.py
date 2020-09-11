import pygame
from .constants import BLACK, ROWS, RED, SQUARE_SIZE, COLS, WHITE
from .piece  import Piece

class Board:
    def __init__(self):
        self.board = []
        self.selected_pecie = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    def draw_sqaures(self,win):
        """DRAWS SQUARES ON THE BOARD"""
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row%2, COLS, 2):
                pygame.draw.rect(win,RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE,SQUARE_SIZE))

    def create_board(self):
        """CODE FOR ADDING PEICES ONTO THE BOARD LIST"""
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col %2 == ((row + 1) % 2):
                    # Adding peices to board structure list
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE)) # white piece
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED)) # Red piece
                    else:
                        self.board[row].append(0) # No peice
                
                # We append zero for no peice present                        
                else:
                    self.board[row].append(0)
        
    def draw(self,win):
        """ DRAWS PIECES AND SQUARES ON TO BOARD """
        # For drawing sqaures
        self.draw_sqaures(win) 

        # For drawing pieces
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

