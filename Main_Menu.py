import os
import time
import pygame
from new_game import*
from draw_text import *
from draw_buttons import *


#Initial values
player_number = 1


def mainMenu(font, screen):
    #Creating New Game Button
    screen.fill((0,0,0))
    draw_bordered_rounded_rect (screen, (100,200,200,70),(0,0,255),(255,255,0),10,5)
    screen = draw_text (font, screen, "New Game", (255,255,255), 200, 235)

    #Creating Customize Board Button
    draw_bordered_rounded_rect (screen, (100,300,200,70),(0,0,255),(255,255,0),10,5)
    screen = draw_text (font, screen, "Customize Board", (255,255,255), 200, 335)
    pygame.display.update()
    
    #Reading For Button Click
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                os._exit(1)
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouse_pos_x, mouse_pos_y) = event.pos
                #Checking for Button Click
                if mouse_pos_x > 99 and mouse_pos_x < 301 and mouse_pos_y > 199 and mouse_pos_y < 271:
                    ret = newGameMenu(screen,font)
                    if ret== 0: 
                        return
                elif mouse_pos_x > 99 and mouse_pos_x <301 and mouse_pos_y > 299 and mouse_pos_y <371:
                    print("Button 2 clicked!")

def newGameMenu(screen,font):
    draw_bordered_rounded_rect (screen, (70,145,260,280),(0,0,255),(255,255,0),10,5)
    draw_bordered_rounded_rect (screen, (310,130,35,35),(0,0,255),(255,255,0),6,5)
    pygame.draw.line(screen,(255,0,0),(322,142),(333,153),3)
    pygame.draw.line(screen,(255,0,0),(333,142),(322,153),3)
    draw_bordered_rounded_rect (screen, (100,180,200,60),(0,0,255),(255,255,0),10,5)
    screen = draw_text(font, screen, "Player vs AI", (255,255,255), 200, 210)
    draw_bordered_rounded_rect (screen, (100,255,200,60),(0,0,255),(255,255,0),10,5)
    screen = draw_text(font, screen, "Player vs Player", (255,255,255), 200, 285)
    draw_bordered_rounded_rect (screen, (100,330,200,60),(0,0,255),(255,255,0),10,5)
    screen = draw_text (font, screen, "AI vs AI", (255,255,255), 200, 360)
    pygame.display.update()
    ret = 1
    #Reading For Button Click
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                os._exit(1)
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouse_pos_x, mouse_pos_y) = event.pos
                #Checking for Button Click
                if mouse_pos_x > 99 and mouse_pos_x < 301 and mouse_pos_y > 179 and mouse_pos_y < 241:
                    ret = newGame(1,1)
                elif mouse_pos_x > 99 and mouse_pos_x <301 and mouse_pos_y > 254 and mouse_pos_y <316:
                    ret = newGame(1,2)
                elif mouse_pos_x > 99 and mouse_pos_x <301 and mouse_pos_y > 339 and mouse_pos_y < 391:
                    ret = newGame(1,3)
                elif mouse_pos_x > 309 and mouse_pos_x < 346 and mouse_pos_y > 129 and mouse_pos_y < 166:
                    mainMenu(font, screen)

            if ret == 0: 
                return 0
    


pygame.init()
pygame.font.init()
font = pygame.font.SysFont('comicsans',30)
screen = pygame.display.set_mode((400,500),0,0)
mainMenu(font,screen)
