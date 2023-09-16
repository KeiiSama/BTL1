import pygame, random, sys, time
from pygame.locals import *

#Khởi tạo pygame
pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 896
SCREEN_hEIGHT = 665
fps = 60
fpsClock = pygame.time.Clock()

#Cửa sổ game
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_hEIGHT))

#Thêm nhạc nền
backgroud_music = pygame.mixer.Sound('E:\Lập trình Game\BTL1\Background_music.mp3')

#Tiêu đề và icon game
pygame.display.set_caption("BTL 1")
icon = pygame.image.load(r'E:\Lập trình Game\BTL1\icon.png')
pygame.display.set_icon(icon)

#Thêm hình ảnh phụ
bua_image = pygame.image.load(r'E:\Lập trình Game\BTL1\bua.png')
bua_image = pygame.transform.scale(bua_image, (100, 100))

#Thêm backgrond cho game
bg = pygame.image.load(r'E:\Lập trình Game\BTL1\Background.png')
bg = pygame.transform.scale(bg, (896, 665))

#Vòng lặp xử lí game
running = True
bua_x, bua_y = 0, 0
bua_visible = False
start_time = None
#hiển thị con trỏ chuột 
pygame.mouse.set_visible(True)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            bua_x, bua_y = mouse_x, mouse_y
            
            bua_visible = True
            
            start_time = pygame.time.get_ticks()
    DISPLAYSURF.blit(bg, (0, 0))
    if bua_visible and start_time is not None:
        current_time = pygame.time.get_ticks()
        if current_time - start_time < 250:
            DISPLAYSURF.blit(bua_image, (bua_x, bua_y))
        else:
            bua_visible = False
    backgroud_music.play(-1)
    pygame.display.update()

pygame.quit()