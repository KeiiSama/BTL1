import pygame, random, sys, time
from pygame.locals import *

#Khởi tạo pygame
pygame.init()

SCREEN_WIDTH = 900
SCREEN_hEIGHT = 550
fps = 60
fpsClock = pygame.time.Clock()

#Cửa sổ game
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_hEIGHT))

#Tiêu đề và icon game
pygame.display.set_caption("BTL 1")
icon = pygame.image.load(r'E:\Lập trình Game\BTL1\icon.png')
pygame.display.set_icon(icon)

#Thêm backgrond cho game
bg = pygame.image.load(r'E:\Lập trình Game\BTL1\Background.png')
bg = pygame.transform.scale(bg, (900, 620))

#Vòng lặp xử lí game
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg, (0, 0))
    pygame.display.update()