import pygame, sys, random
from pygame import *
import game_Interface

pygame.init()

SCREEN_WIDTH = 896
SCREEN_HEIGHT = 665

#Cửa sổ game
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Tiêu đề và icon game
pygame.display.set_caption("BTL 1")
icon = pygame.image.load(r'E:\Lập trình Game\BTL1\icon.png')
pygame.display.set_icon(icon)

#Thêm backgrond cho game
bg = pygame.image.load(r'E:\Lập trình Game\BTL1\Background.png')
bg = pygame.transform.scale(bg, (896, 665))

def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    game_Interface.main()
        
        screen.blit(bg, (0, 0))            
        pygame.display.update()
        pygame.display.flip()
    pygame.quit()
    sys.exit()
                    
if __name__ == '__main__':
    main()            