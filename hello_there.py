import pygame as pg
from pygame.locals import *

def main():
    pg.init()
    screen = pg.display.set_mode((3000, 1000))
    pg.display.set_caption("hello_there.py")

    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    font = pg.font.Font(None, 36)
    text = font.render("Hello There", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    screen.blit(background, (0, 0))
    pg.display.flip()

    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                return
        
        screen.blit(background, (0, 0))
        pg.display.flip()

if __name__ == "__main__": main()