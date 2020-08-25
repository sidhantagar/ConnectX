def draw_text(font, screen, text, color, midx, midy):
    text = font.render(text,1,color)
    x = midx - text.get_width()//2
    y = midy - text.get_height()//2
    screen.blit(text,(x,y))
    return screen