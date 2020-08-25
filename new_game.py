#Mode1: player vs AI
#Mode2: player vs player
#Mode3: AI vs AI

import pygame
import numpy as np
import pandas as pd
from game_functions import *
from agent import agent
class Dictionary1:
    def __init__(self, rows,columns, inarow,square_size,startx,starty):
        self.rows = rows
        self.columns = columns
        self.inarow = inarow
        self.square_size = square_size
        self.startx = startx
        self.starty = starty
class Dictionary2:
    def __init__(self,board,mark):
        self.board = board
        self.mark = mark
    def update(self,board):
        self.board = board
    def update_all(self,board,mark):
        self.board = board
        self.mark = mark

def newGame(player_number,player_mode):
    df_config = pd.read_csv("config.csv")
    config = df_config[player_number-1:player_number]
    #Initializing base variables
    rows = config.iloc[0]['Rows']
    columns = config.iloc[0]['Columns']
    inarow = config.iloc[0]['Inarow']
    square_size = min(int(700/rows), int(1100/columns))
    startx = 600 - int((columns/2)*square_size)
    starty = 400 - int((rows/2)*square_size)
    #Creating class for base variables
    config = Dictionary1(rows,columns,inarow,square_size,startx,starty)
    ret = 1
    if player_mode == 1:
        ret = playervsAI(config)
        if ret == 0:
            return 0
    if player_mode == 2:
        ret = playervsPlayer(config)
        if ret == 0:
            return 0
    if player_mode == 3:
        ret = AIvsAI(config)
        if ret == 0:
            return 0


def playervsAI(config):
    player = np.random.randint(1,3)
    game_screen, board = create_board(config)
    current = Dictionary2(board,2)
    
    game_over = False
    while game_over == False:
        if player == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    return 0
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    player_move = get_column(config,event.pos)
                    if player_move == None or is_valid(board,player_move)== False:
                        continue
                    else:
                        board,game_screen = drop_piece(config,board, player_move, player,game_screen)
                        connected,p1,p2 = count_windows (board,config.inarow,player,config,True)
                        if (connected>=1):
                            draw_line(config,p1,p2,player,game_screen)
                            pygame.display.update()
                            print ("Player " + str(player)+"Won!!")
                            game_over = True
                        player = 2
        else:
            current.update(board)
            player_move = agent(current,config)
            if player_move == None or is_valid(board,player_move)== False:
                continue
            else:
                board,game_screen = drop_piece(config,board, player_move, player,game_screen)
                connected,p1,p2 = count_windows (board,config.inarow,player,config, True)
                if (connected>=1):
                    draw_line(config,p1,p2,player,game_screen)
                    pygame.display.update()
                    print ("AI Won!!")
                    game_over = True
                player = 1
        if np.count_nonzero(board==0)==0:
            game_over = True
        pygame.display.update()
    if game_over == True:
        pygame.display.quit()
        return 0

def playervsPlayer(config):
    player = np.random.randint(1,3)
    game_screen, board = create_board(config)
    
    game_over = False
    while game_over == False:
        if player == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    return 0
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    player_move = get_column(config,event.pos)
                    if player_move == None or is_valid(board,player_move)== False:
                        continue
                    else:
                        board,game_screen = drop_piece(config,board, player_move, player,game_screen)
                        connected,p1,p2 = count_windows (board,config.inarow,player,config,True)
                        if (connected>=1):
                            draw_line(config,p1,p2,player,game_screen)
                            pygame.display.update()
                            print ("Player " + str(player)+"Won!!")
                            game_over = True
                        player = 2
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    return 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    player_move = get_column(config,event.pos)
                    if player_move == None or is_valid(board,player_move)== False:
                        continue
                    else:
                        board,game_screen = drop_piece(config,board, player_move, player,game_screen)
                        connected,p1,p2 = count_windows (board,config.inarow,player,config, True)
                        if (connected>=1):
                            draw_line(config,p1,p2,player,game_screen)
                            pygame.display.update()
                            print ("Player " + str(player)+"Won!!")
                            game_over = True
                        player = 1
        pygame.display.update()
        if np.count_nonzero(board==0)==0:
            game_over = True
        pygame.display.update()
    if game_over == True:
        pygame.display.quit()
        return 0
def AIvsAI(config):
    player = np.random.randint(1,3)
    game_screen, board = create_board(config)
    current = Dictionary2(board,2)
    
    game_over = False
    while game_over == False:
        if player == 1:
            current.update_all(board,player)
            player_move = agent(current,config)
            if player_move == None or is_valid(board,player_move)== False:
                continue
            else:
                board,game_screen = drop_piece(config,board, player_move, player,game_screen)
                connected,p1,p2 = count_windows (board,config.inarow,player,config, True)
                if (connected>=1):
                    draw_line(config,p1,p2,player,game_screen)
                    pygame.display.update()
                    print ("Player " + str(player)+"Won!!")
                    game_over = True
                player = 2
        else:
            current.update_all(board,player)
            player_move = agent(current,config)
            if player_move == None or is_valid(board,player_move)== False:
                continue
            else:
                board,game_screen = drop_piece(config,board, player_move, player,game_screen)
                connected,p1,p2 = count_windows (board,config.inarow,player,config, True)
                if (connected>=1):
                    draw_line(config,p1,p2,player,game_screen)
                    pygame.display.update()
                    print ("Player " + str(player)+"Won!!")
                    game_over = True
                player = 1
        if np.count_nonzero(board==0)==0:
            game_over = True
        pygame.display.update()
    if game_over == True:
        pygame.display.quit()
        return 0
#newGame(1,1)
