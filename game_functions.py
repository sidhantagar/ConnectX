import numpy as np    
import pygame

def create_board(config):
    #Initialising board array
    board = np.zeros((config.rows, config.columns))
    #Initialising board graphic
    game_screen = pygame.display.set_mode((1200,800),0,0)
    game_screen.fill((0,0,50))
    for i in range (config.rows):
        for j in range (config.columns):
            x = config.startx + ((2*i+1)*config.square_size)//2
            y = config.starty + ((2*j+1)*config.square_size)//2
            pygame.draw.circle(game_screen,(150,150,200),(x,y),config.square_size//2-5)
            pygame.draw.circle(game_screen,(0,0,0),(x,y),config.square_size//2-7)
    pygame.display.update()
    return game_screen,board

def is_valid(board,column):
    if board[0][column]==0:
        return True
    else:
        return False

def drop_piece(config, board, col, mark, game_screen):
    #Determining the location of the drop
    square_size = config.square_size
    next_board = board.copy()
    for row in range(config.rows-1, -1, -1):
        if next_board[row][col] == 0:
            break
    #Updating the board
    next_board[row][col] = mark
    #Updating the board graphic
    x = config.startx + ((2*col+1)*square_size)//2
    y = config.starty + ((2*row+1)*square_size)//2
    if mark == 1:
        pygame.draw.circle(game_screen,(255,0,0),(x,y),square_size//2-7)
    else:
        pygame.draw.circle(game_screen,(0,255,0),(x,y),square_size//2-7)
    return next_board,game_screen

def count_windows(grid, num_discs, piece, config,ret=False):
    num_windows = 0
    # horizontal
    for row in range(config.rows):
        for col in range(config.columns-(config.inarow-1)):
            window = list(grid[row, col:col+config.inarow])
            if check_window(window, num_discs, piece, config):
                num_windows += 1
                if ret==True:
                    return num_windows,(row, col),(row,col+config.inarow)
    # vertical
    for row in range(config.rows-(config.inarow-1)):
        for col in range(config.columns):
            window = list(grid[row:row+config.inarow, col])
            if check_window(window, num_discs, piece, config):
                num_windows += 1
                if ret == True:
                    return num_windows,(row, col),(row+config.inarow, col)
    # positive diagonal
    for row in range(config.rows-(config.inarow-1)):
        for col in range(config.columns-(config.inarow-1)):
            window = list(grid[range(row, row+config.inarow), range(col, col+config.inarow)])
            if check_window(window, num_discs, piece, config):
                num_windows += 1
                if ret == True:
                    return num_windows,(row, col),(row+config.inarow, col+config.inarow)
    # negative diagonal
    for row in range(config.inarow-1, config.rows):
        for col in range(config.columns-(config.inarow-1)):
            window = list(grid[range(row, row-config.inarow, -1), range(col, col+config.inarow)])
            if check_window(window, num_discs, piece, config):
                num_windows += 1
                if ret == True:
                    return num_windows,(row, col),(row-config.inarow, col+config.inarow)
    if ret == True:
        return num_windows,0,0
    else:
        return num_windows

def check_window(window, num_discs, piece, config):
    return (window.count(piece) == num_discs and window.count(0) == config.inarow-num_discs)

def get_column (config,pos):
    (x,y) = pos
    for i in range (config.columns):
        if x >= (config.startx + i*config.square_size) and x < (config.startx + (i+1)*config.square_size):
            return i
def draw_line(config,p1,p2,player,game_screen):
    j,i = p1
    x1 = config.startx + ((2*i+1)*config.square_size)//2
    y1 = config.starty + ((2*j+1)*config.square_size)//2
    j,i = p2
    x2 = config.startx + ((2*i+1)*config.square_size)//2
    y2 = config.starty + ((2*j+1)*config.square_size)//2
    if (x1>x2):
        x2+=config.square_size
    elif(x1<x2):
        x2-=config.square_size
    if (y1>y2):
        y2+=config.square_size
    elif(y1<y2):
        y2-=config.square_size
    pygame.draw.line(game_screen,(255,255,255),(x1,y1),(x2,y2),5)
    pygame.draw.circle(game_screen,(255,255,255),(x1,y1),5)
    pygame.draw.circle(game_screen,(255,255,255),(x2,y2),5)

    if player ==1:
        pygame.draw.circle(game_screen,(155,0,0),(x1,y1),3)
        pygame.draw.circle(game_screen,(155,0,0),(x2,y1),3)
        pygame.draw.line(game_screen,(155,0,0),(x1,y1),(x2,y2),3)
    else:
        pygame.draw.line(game_screen,(0,155,0),(x1,y1),(x2,y2),3)
