import pygame
from pygame import mixer
import time
import sys
from random import randint


class Image:
    def __init__(self,x,y, img):
        self.img=img
        self.rect=self.img.get_rect()
        self.rect.topleft=(x,y)

    def draw(self):
        screen.blit(self.img, (self.rect.x, self.rect.y))

pygame.init()
mixer.init()

mixer.music.set_volume(100)
clock=pygame.time.Clock()
FPS = 30
width = 800
height = 500
red = (0,0,255)
gold = (138,51,36)
screen = pygame.display.set_mode((width, height))
white = (255,255,255)
black = (0, 0,0 )
loss_list = []
win_list = []

text_list = ["Press on."
,"Move forward."
,"Don't give up."
,"Persevere."
,"Soldier on."
,"Forge ahead."
,"Keep at it."
,"Stay the course."
,"Hang in there."
,"Push through."
,"Keep pushing."
,"Keep moving."
,"Keep at it."
,"Continue the journey."
,"Keep the faith."
,"Stay persistent."
,"Persist and resist."
,"Keep on keeping on."
,"Stay determined."
,"Keep the momentum."]

slot_machine = pygame.image.load('attachment.png')
slot_machine = pygame.transform.scale(slot_machine, (800,500))
boss = pygame.image.load('boss.png')
boss = pygame.transform.scale(boss, (200,200))
bubble = pygame.image.load('bubble_text.png')
bubble = pygame.transform.scale(bubble, (200,200))



pos_1 = width - 320 
pos_2 = width - 500
pos_3 = width - 650
hei_pos = height/2 -75

screen.fill(black)
side =width/2 -100
top = height-200
list_of_image = ['money.jpg', 'fire.jpg', 'seven.jpg']
list_of_pos=[pos_1+40, pos_2+40, pos_3+40]
font = pygame.font.SysFont("Arialblack",40)
font1 = pygame.font.SysFont("Arialblack",30)
font2 = pygame.font.SysFont("Arialblack",20)
font4 = pygame.font.SysFont("Arialblack",10)
font = "ARCADE_N.TTF"  # Ensure the font file is in the same directory

def draw_text(text,font,text_col, x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))

def animate():
    val = randint(0,2)
    time.sleep(0.05)
    Imag1 = Image(pos_1 + 40, hei_pos, pygame.transform.scale(pygame.image.load(list_of_image[val]), (100,100)))    
    val = randint(0,2)
    Imag2 = Image(pos_2 + 40, hei_pos, pygame.transform.scale(pygame.image.load(list_of_image[val]), (100,100)))
    val = randint(0,2)
    Imag3 = Image(pos_3 + 40, hei_pos, pygame.transform.scale(pygame.image.load(list_of_image[val]), (100,100)))
    Imag1.draw()
    Imag2.draw()
    Imag3.draw()
    time.sleep(0.05)
    pygame.display.update()


def randomize():
    mixer.music.load("rolling_sound_final_ver.mp3")
    mixer.music.play()
    val1 = randint(0,2)
    val2 = randint(0,2)
    val3 = randint(0,2)
    Img1 = Image(pos_1 + 40, hei_pos, pygame.transform.scale(pygame.image.load(list_of_image[val1]), (100,100)))    
    Img2 = Image(pos_2 + 40, hei_pos, pygame.transform.scale(pygame.image.load(list_of_image[val2]), (100,100)))
    Img3 = Image(pos_3 + 40, hei_pos, pygame.transform.scale(pygame.image.load(list_of_image[val3]), (100,100)))

    for i in range(0,40):
        animate()

    Img1.draw()
    Img2.draw()
    Img3.draw()
    if val1 == val2 and val2 == val3:
        win_list.append(1)
        mixer.music.load("win_sound.mp3")
        mixer.music.play()
    else:      
        loss_list.append(1)
        mixer.music.load("lose_game.mp3")
        mixer.music.play()

        
    if len(loss_list) + len(win_list) > 3:
        screen.fill(black)
        display_stats()
        
        

def display_stats():
    txtsurf = text_format("YOUR STATS", font, 40, white)
    screen.blit(txtsurf,(20,40))

    wins = text_format("WINS:", font, 30, white)
    screen.blit(wins,(50,150))

    win_str = str(len(win_list))
    wins_stats = text_format(win_str, font, 30, white)
    screen.blit(wins_stats, (185,150))
    
    loss = text_format("LOSS:",font, 30, white)
    screen.blit(loss,(50,200))
    loss_str = str(len(loss_list))
    loss_stats = text_format(loss_str, font, 30, white)
    screen.blit(loss_stats, (185,200))
    screen.blit(boss, (width - 350, height - 300))
    screen.blit(bubble, (width - 250, height - 475))
    draw_text("Suicide hotline", font2, black, width - 230, height - 420)
    draw_text("780-709-0810", font2, black, width - 230, height - 390)
    pygame.display.update()
    time.sleep(3)
    pygame.quit()

# Text Renderer
def text_format(message, textFont, textSize, textColor):
   newFont = pygame.font.Font(textFont, textSize)
   newText = newFont.render(message, True, textColor)  # True for anti-aliasing
   return newText


def game_main():
    run = True

    bg = pygame.image.load('brickbg.jpg')
    screen.blit(bg,(0,0))

    screen.blit(slot_machine, (0,0))
    
    #draw_text("Press SPACE to SPIN", font, black, 150,40)
    instruction = text_format("Press SPACE to SPIN", font, 26, gold)
    screen.blit(instruction, (150,45))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    randomize()


        pygame.display.flip()

    pygame.quit()

