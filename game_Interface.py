import pygame, random, sys, time
from pygame.locals import *

#Khởi tạo pygame
pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 896
SCREEN_HEIGHT = 665
fps = 60
fpsClock = pygame.time.Clock()

#Cửa sổ game
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Thêm nhạc nền
backgroud_music = pygame.mixer.Sound('E:\Lập trình Game\BTL1\Background_music.mp3')

#Tiêu đề và icon game
pygame.display.set_caption("BTL 1")
icon = pygame.image.load(r'E:\Lập trình Game\BTL1\icon.png')
pygame.display.set_icon(icon)

#Thêm hình ảnh phụ
bua_image = pygame.image.load(r'E:\Lập trình Game\BTL1\bua.png')
bua_image = pygame.transform.scale(bua_image, (150, 150))

#Thêm backgrond cho game
bg = pygame.image.load(r'E:\Lập trình Game\BTL1\Background.png')
bg = pygame.transform.scale(bg, (896, 665))

#Vòng lặp xử lí game
running = True

#Xử lí chuyển động búa
bua_x, bua_y = 0, 0
bua_visible = False
start_time = None
hammer_image = []

#Tạo hiệu ứng búa đập
angle = 0
rotate_speed = 25

#hiển thị con trỏ chuột 
pygame.mouse.set_visible(True)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Cập nhật vị trí búa theo trỏ chuột
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                bua_x, bua_y = mouse_x, mouse_y
                bua_visible = True
                start_time = pygame.time.get_ticks() 
                    
                #Cập nhật chuyển động búa
                if(angle == 25):
                        angle = 0
                angle += rotate_speed           
    #Giao diện bên trong game
    screen.blit(bg, (0, 0))
    if bua_visible and start_time is not None:
        current_time = pygame.time.get_ticks()
        if current_time - start_time < 250:
            rotated_bua = pygame.transform.rotate(bua_image, angle)
            bua_rect = rotated_bua.get_rect()
            bua_rect.center = (bua_x, bua_y)
            screen.blit(rotated_bua, bua_rect.topleft)
        else:
            bua_visible = False
    #Nhạc game
    backgroud_music.play(-1)
    pygame.display.update()

pygame.quit()
sys.exit()