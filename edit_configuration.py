"""
Copyright 2020, Sidhant Agarwal, sidhant11136@gmail.com, All rights reserved.

Borrowed from https://github.com/sidhantagar/ConnectX under the MIT license.

"""

import pandas as pd
from draw_text import *
from draw_buttons import *
from pygame_textinput import *


def editConfig(screen, font, player_number, color = (255,255,0)): 
    from Main_Menu import mainMenu
    clock = pygame.time.Clock()
    #Importing configuration form CSV
    df_config = pd.read_csv("config.csv")
    config = df_config.set_index("Player")
    #config = df_config[player_number-1:player_number]

    #Drawing Labels and Textboxes
    draw_bordered_rounded_rect (screen, (70,145,260,280),(0,0,255),(255,255,0),10,5)
    draw_bordered_rounded_rect (screen, (310,130,35,35),(0,0,255),(255,255,0),6,5)
    pygame.draw.line(screen,(255,0,0),(322,142),(333,153),3)
    pygame.draw.line(screen,(255,0,0),(333,142),(322,153),3)
    
    #Rows
    rows_text = font.render("Rows: ",1,color)
    screen.blit (rows_text, (100,210-rows_text.get_height()//2))
    draw_bordered_rounded_rect(screen, (240,193,45,30),(255,0,0),(255,255,0),5,2)
    draw_text(font,screen,str(config['Rows'][player_number-1]),(255,255,0),262,208)
    rows_input = TextInput(initial_string = str(config['Rows'][player_number-1]))
    #Columns
    columns_text = font.render("Columns: ",1,color)
    screen.blit (columns_text, (100,285-columns_text.get_height()//2))
    draw_bordered_rounded_rect(screen, (240,268,45,30),(255,0,0),(255,255,0),5,2)
    draw_text(font,screen,str(config['Columns'][player_number-1]),(255,255,0),262,283)
    columns_input = TextInput(initial_string = str(config['Columns'][player_number-1]))
    #screen.blit (columns_input.get_surface(), (250,285-columns_text.get_height()//2))
    #Inarow
    inarow_text = font.render("Inarow: ",1,color)
    screen.blit (inarow_text, (100,360-inarow_text.get_height()//2))
    draw_bordered_rounded_rect(screen, (240,343,45,30),(255,0,0),(255,255,0),5,2)
    draw_text(font,screen,str(config['Inarow'][player_number-1]),(255,255,0),262,358)
    inarow_input = TextInput(initial_string = str(config['Inarow'][player_number-1]))
    #screen.blit (inarow_input.get_surface(), (250,360-inarow_text.get_height()//2))
    
    state = 0
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.display.quit()
                os._exit(1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if state == 1:
                        rows = rows_input.get_text()
                        config['Rows'][player_number-1] = int(rows)
                        if config['Rows'][player_number-1] >20:
                            config['Rows'][player_number-1] = 20
                        if config['Rows'][player_number-1] < 3:
                            config['Rows'][player_number-1] = 3
                        draw_bordered_rounded_rect(screen, (240,193,45,30),(255,0,0),(255,255,0),5,2)
                        draw_text(font,screen,str(config['Rows'][player_number-1]),(255,255,0),262,208)
                        rows_input = TextInput(initial_string = str(config['Rows'][player_number-1]))
                    elif state == 2:
                        columns = columns_input.get_text()
                        config['Columns'][player_number-1] = int(columns)
                        if config['Columns'][player_number-1] > 20:
                            config['Columns'][player_number-1] = 20
                        if config['Columns'][player_number-1] < 3:
                            config['Columns'][player_number-1] = 3
                        draw_bordered_rounded_rect(screen, (240,268,45,30),(255,0,0),(255,255,0),5,2)
                        draw_text(font,screen,str(config['Columns'][player_number-1]),(255,255,0),262,283)
                        columns_input = TextInput(initial_string = str(config['Columns'][player_number-1]))
                    elif state == 3:
                        inarow = inarow_input.get_text()
                        config['Inarow'][player_number-1] = int (inarow)
                        if config['Inarow'][player_number-1] <3:
                            config['Inarow'][player_number-1] = 3 
                        if config['Inarow'][player_number-1] >20:
                            config['Inarow'][player_number-1] = 20
                        draw_bordered_rounded_rect(screen, (240,343,45,30),(255,0,0),(255,255,0),5,2)
                        draw_text(font,screen,str(config['Inarow'][player_number-1]),(255,255,0),262,358)
                        inarow_input = TextInput(initial_string = str(config['Inarow'][player_number-1]))
                    state = 0
                    config.to_csv('config.csv')
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouse_pos_x , mouse_pos_y) = event.pos
                #If State is not 0 we set it to 0
                if state == 1:
                    rows = rows_input.get_text()
                    config['Rows'][player_number-1] = int(rows)
                    draw_bordered_rounded_rect(screen, (240,193,45,30),(255,0,0),(255,255,0),5,2)
                    draw_text(font,screen,str(config['Rows'][player_number-1]),(255,255,0),262,208)
                    rows_input = TextInput(initial_string = str(config['Rows'][player_number-1]))
                elif state == 2:
                    columns = columns_input.get_text()
                    config['Columns'][player_number-1] = int(columns)
                    draw_bordered_rounded_rect(screen, (240,268,45,30),(255,0,0),(255,255,0),5,2)
                    draw_text(font,screen,str(config['Columns'][player_number-1]),(255,255,0),262,283)
                    columns_input = TextInput(initial_string = str(config['Columns'][player_number-1]))
                elif state == 3:
                    inarow = inarow_input.get_text()
                    config['Inarow'][player_number-1] = int (inarow)
                    draw_bordered_rounded_rect(screen, (240,343,45,30),(255,0,0),(255,255,0),5,2)
                    draw_text(font,screen,str(config['Inarow'][player_number-1]),(255,255,0),262,358)
                    inarow_input = TextInput(initial_string = str(config['Inarow'][player_number-1]))
                state = 0
                config.to_csv('config.csv')
                #State Change Clicks
                if mouse_pos_x > 239 and mouse_pos_x < 286 and mouse_pos_y > 192 and mouse_pos_y < 224:
                    state = 1 
                elif mouse_pos_x > 239 and mouse_pos_x < 286 and mouse_pos_y > 267 and mouse_pos_y < 299:
                    state = 2
                elif mouse_pos_x > 239 and mouse_pos_x < 286 and mouse_pos_y > 342 and mouse_pos_y < 374:
                    state = 3
                elif mouse_pos_x > 309 and mouse_pos_x < 346 and mouse_pos_y > 129 and mouse_pos_y < 166:
                    mainMenu(font, screen)
                
        #Rows
        if state == 1:
            rows_input.update(events)
            draw_bordered_rounded_rect(screen, (240,193,45,30),(0,0,255),(255,255,0),5,2)
            screen.blit(rows_input.get_surface(),(250,210-rows_text.get_height()//2))
        elif state == 2:
            columns_input.update(events)
            draw_bordered_rounded_rect(screen, (240,268,45,30),(0,0,255),(255,255,0),5,2)
            screen.blit(columns_input.get_surface(),(250,285-columns_text.get_height()//2))
        elif state == 3:
            inarow_input.update(events)
            draw_bordered_rounded_rect(screen, (240,343,45,30),(0,0,255),(255,255,0),5,2)
            screen.blit(inarow_input.get_surface(), (250,360-inarow_text.get_height()//2))
        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((400,500),0,0)
    font = pygame.font.SysFont('comicsans',30)
    editConfig(screen, font, 1)