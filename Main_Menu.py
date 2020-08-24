import sys
import time
import pygame
from new_game import*
from drawbuttons import *

#Initial values
player_number = 1
mode = 2

def main_menu(font):
    draw_bordered_rounded_rect (screen, (100,200,200,70),(0,0,255),(255,255,0),10,5)
    new_game_text = font.render("New Game",1,(255,255,255))
    screen.blit(new_game_text,(148,225))
    draw_bordered_rounded_rect (screen, (100,300,200,70),(0,0,255),(255,255,0),10,5)
    Customise_board_text = font.render("Customize Board",1,(255,255,255))
    screen.blit(Customise_board_text,(115,325))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouse_pos_x, mouse_pos_y) = event.pos
                #Checking for button1
                if mouse_pos_x > 99 and mouse_pos_x < 301 and mouse_pos_y > 199 and mouse_pos_y < 271:
                    ret = newGame(player_number,mode)
                    if ret== 0: 
                        return
                elif mouse_pos_x > 99 and mouse_pos_x <301 and mouse_pos_y > 299 and mouse_pos_y <371:
                    print("Button 2 clicked!")


pygame.init()
pygame.font.init()
font = pygame.font.SysFont('comicsans',30)
screen = pygame.display.set_mode((400,500))
main_menu(font)
