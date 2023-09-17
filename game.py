import pygame, sys, time
from pygame import *

pygame.init()
pygame.mixer.init()
fps = 60
fpsClock = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Thêm background
bg = pygame.image.load('Background.png')
bg = pygame.transform.scale(bg, (800, 600))

#Thêm nhạc nền
backgroud_music = pygame.mixer.Sound('Background_music.mp3')


#Tiêu đề và icon game
pygame.display.set_caption("BTL 1")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#Thêm hình ảnh phụ
bua_image = pygame.image.load('bua.png')
bua_image = pygame.transform.scale(bua_image, (150, 150))

#Tạo font
font_path = "CHILLER.TTF"
font = pygame.font.Font(font_path, 100)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_start_game():
    button_rect = pygame.Rect(300, 250, 200, 80)
    
    text = font.render("Start Game", True, BLACK)
    text_rect = text.get_rect()
    text_rect.center = button_rect.center
    screen.blit(text, text_rect)

#Code hoạt động trong game
def draw_running_game():
    angle = 0
    rotate_speed = 25
    
    bua_x, bua_y = 0, 0
    bua_visible = False
    start_time = None
    hammer_image = []
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:    
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
        pygame.display.update()
        
    pygame.quit()
    sys.exit()

#Vòng lặp chính 
game_state = "waiting"

run = True
    
while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:    
                run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "waiting":
            # Kiểm tra xem người chơi đã bấm vào nút "Start" chưa
                if 300 <= event.pos[0] <= 500 and 200 <= event.pos[1] <= 300:
                    game_state = "running"

    screen.blit(bg, (0,0))
    backgroud_music.play(-1)
    if game_state == "waiting":    
        draw_start_game()
    elif game_state == "running":
        draw_running_game()
    pygame.display.update()

pygame.quit()
sys.exit()