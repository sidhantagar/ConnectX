#Mode1: AI vs AI
#Mode2: player vs AI
import pygame
import numpy as np
import pandas as pd
from game_functions import *
class Dictionary1:
    def __init__(self, rows,columns, inarow):
        self.rows = rows
        self.columns = columns
        self.inarow = inarow
class Dictionary2:
    def __init__(self,board,mark):
        self.board = board
        self.mark = mark

def newGame(player_number,player_mode):
    df_config = pd.read_csv("config.csv")
    config = df_config[player_number-1:player_number]
    #print(config)
    rows = config.iloc[0]['Rows']
    columns = config.iloc[0]['Columns']
    inarow = config.iloc[0]['Inarow']
    game_screen = pygame.display.set_mode((1200,800))
    game_screen.fill((0,0,50))
    square_size = min(int(700/rows), int(1100/columns))
    startx = 600 - int((columns/2)*square_size)
    starty = 400 - int((rows/2)*square_size)
    for i in range (rows):
        for j in range (columns):
            x = startx + ((2*i+1)*square_size)//2
            y = starty + ((2*j+1)*square_size)//2
            pygame.draw.circle(game_screen,(150,150,200),(x,y),square_size//2-5)
            pygame.draw.circle(game_screen,(0,0,0),(x,y),square_size//2-7)
    pygame.display.update()
    if player_mode ==1:
        playervsAI(rows,columns,inarow,game_screen,square_size,startx,starty)

def playervsAI(rows,columns,inarow,game_screen,square_size,startx,starty):
    player = 1 #np.random.randint(1,3)
    board = create_board(rows,columns)
    config = Dictionary1(rows,columns,inarow)

    game_over = False
    while game_over == False:
        if player == 1:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    return 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    player_move = get_column(columns,square_size,startx,event.pos)
                    if player_move == None:
                        continue
                    print (player_move,event.pos)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                return 0
def get_column (columns,square_size,startx,pos):
    (x,y) = pos
    for i in range (columns):
        if x >= (startx + i*square_size) and x < (startx + (i+1)*square_size):
            return i

newGame(1,1)
