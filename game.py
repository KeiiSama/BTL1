import pygame, sys, time, random
from pygame import *
from dataclasses import dataclass

@dataclass
class Score:
    success: int
    missing: int

pygame.init()
pygame.mixer.init()
fps = 60
fpsClock = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
score = Score(success=0, missing=0)

#Thêm background
bg = pygame.image.load('Background.png')
bg = pygame.transform.scale(bg, (800, 600))

#Thêm nhạc nền
backgroud_music = pygame.mixer.Sound('Background_music.mp3')

#Thêm zombie background
bg_zom1 = pygame.image.load('bg_zom1.png')
bg_zom1 = pygame.transform.scale(bg_zom1, (160, 300))
bg_zom2 = pygame.image.load('bg_zom2.png')
bg_zom2 = pygame.transform.scale(bg_zom2, (160, 300))

#Thêm zombi trong màn hình trò chơi
zom_image = pygame.image.load('zombie.png')
zom_image = pygame.transform.scale(zom_image,(100, 100))
zom_points = pygame.Rect(0, 300, 750, 200)
zom_rect = zom_image.get_rect()
zom_rect_radius = max(zom_rect.size)/2
zom_visible = False

def choose_random_zom_point():
    x = random.randint(zom_points.left,zom_points.right)
    y = random.randint(zom_points.top,zom_points.bottom)
    return x, y

#Tiêu đề và icon game
pygame.display.set_caption("BTL 1")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#Thêm hình ảnh phụ
bua_image = pygame.image.load('bua.png')
bua_image = pygame.transform.scale(bua_image, (150, 150))
current_zom_pos = choose_random_zom_point()

#Tạo font
font_path = "c:\WINDOWS\Fonts\CHILLER.TTF"
font = pygame.font.Font(font_path, 100)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_start_game():
    button_rect = pygame.Rect(300, 250, 200, 80)
    
    text = font.render("Start Game", True, BLACK)
    text_rect = text.get_rect()
    text_rect.center = button_rect.center
    screen.blit(text, text_rect)
    
def show_score():
    score_font = pygame.font.Font(font_path, 50)
    score_text = score_font.render(f"Score: {score.success}", True, WHITE)
    missing_score_text = score_font.render(f"Missing: {score.missing}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(missing_score_text, (10, 60))

def is_dammed(zombie_pos, dam_pos):
    if ((dam_pos[0]-zombie_pos[0])**2 + (dam_pos[1]-zombie_pos[1])**2) <= zom_rect_radius**2:
        return True
    return False

#Code hoạt động trong game
def draw_running_game():
    global current_zom_pos
    global zom_visible
    angle = 0
    rotate_speed = 25
    
    bua_x, bua_y = 0, 0
    bua_visible = False
    start_time = None
    hammer_image = []

    zom_timer = 1500

    current_zom_start_time = 0
    
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
                    print(bua_x, bua_y)
                    bua_visible = True
                    start_time = pygame.time.get_ticks() 
                        
                    #Cập nhật chuyển động búa
                    if(angle == 25):
                            angle = 0
                    angle += rotate_speed   
                    
                    #Process score
                    if zom_visible and is_dammed((current_zom_pos[0] + zom_rect.size[0]/2, current_zom_pos[1] + zom_rect.size[1]/2), (bua_x, bua_y)):
                        zom_visible = False
                        score.success +=1
                    else:
                        score.missing+= 1
                            
        #Giao diện bên trong game
        screen.blit(bg, (0, 0))
        show_score()
        
        current_time = pygame.time.get_ticks()
        if current_time - current_zom_start_time >= zom_timer:                         
        # Chọn ngẫu nhiên một điểm xuất hiện zombie mới
            current_zom_pos = choose_random_zom_point()
            current_zom_start_time = current_time
            zom_visible = True

        if zom_visible:
            screen.blit(zom_image, current_zom_pos)
        
        if bua_visible and start_time is not None:
            #current_time = pygame.time.get_ticks()
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

#Màn hình Game Over
def draw_game_over():
    button_rect = pygame.Rect(300, 250, 200, 80)
    
    text = font.render("Game Over", True, BLACK)
    text_rect = text.get_rect()
    text_rect.center = button_rect.center
    screen.blit(text, text_rect)

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
    screen.blit(bg_zom1, (50, 250))
    screen.blit(bg_zom2, (600, 270))
    backgroud_music.play(-1)
    if game_state == "waiting":    
        draw_start_game()
    elif game_state == "running":
        draw_running_game()
    pygame.display.update()

pygame.quit()
sys.exit()