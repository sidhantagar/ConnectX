"""
Copyright 2020, Sidhant Agarwal, sidhant11136@gmail.com, All rights reserved.

Borrowed from https://github.com/sidhantagar/ConnectX under the MIT license.

"""

def draw_text(font, screen, text, color, midx, midy):
    text = font.render(text,1,color)
    x = midx - text.get_width()//2
    y = midy - text.get_height()//2
    screen.blit(text,(x,y+2))
    return screen