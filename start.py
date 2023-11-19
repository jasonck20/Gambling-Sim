import pygame
from pygame.locals import *
from pygame import mixer
import os
import sys
import random
from slot import *

# Initialize Pygame
pygame.init()
mixer.init()
mixer.music.set_volume(100)
# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen_width = 800
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

images = ['Arnold.png', 'Cristiano.png', 'Elon.png','Jordan.png','MLK.png','RFK.png']# Add paths to your images
background_images = ['Gamble1.png', 'Gamble2.png', 'Gamble3.png']

quotes = ["YOU MISS 100 percent\nOF THE SHOTS YOU DONT TAKE", "99 percents of People\nQuit Before They Hit It Big", "Greatness is just a step\nbeyond where most quit","Triumph\n whispers the tenacious","Summits\n await the persistent","Rare\n are the relentless"]

# Text Renderer
def text_format(message, textFont, textSize, textColor):
   newFont = pygame.font.Font(textFont, textSize)
   newText = newFont.render(message, True, textColor)  # True for anti-aliasing
   return newText

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
red = (170, 74, 68)

#Load Images
loaded_images = [pygame.transform.scale(pygame.image.load(img).convert(), (screen_width // 1, screen_height // 1)) for img in background_images]

# Game Fonts
font = "ARCADE_N.TTF"  # Ensure the font file is in the same directory

# Game Framerate
clock = pygame.time.Clock()
FPS = 30

# Initialize blinking variables
blinking_title_visible = True  # Controls the visibility of the title
blink_timer = 500  # Time in milliseconds to show/hide the title
last_blink = pygame.time.get_ticks()  # Last tick time of the blink

# Rolling text variables
rolling_text = "WARNING!! GAMBLING IS SUPER FUN"
rolling_pos_x = screen_width  # Start off-screen to the right
rolling_speed = 2  # Pixels per frame

# Create rectangles for menu items for mouse collision detection
start_rect = pygame.Rect(screen_width // 2 - 50, 150, 100, 30)  #
quit_rect = pygame.Rect(screen_width // 2 - 50, 180, 100, 30)  #

def loading_screen():
   selected_image = random.choice(images)
   selected_quote = random.choice(quotes)

   # Load and scale the image to half of the original size (150x150)
   image_surface = pygame.image.load(selected_image)
   image_surface = pygame.transform.scale(image_surface, (200, 200))

   screen.fill(black)  # Clear screen

   # Calculate positions for centering the image
   image_x = (screen_width - image_surface.get_width()) // 2
   image_y = (screen_height - image_surface.get_height()) // 2

   # Blit the image to the screen
   screen.blit(image_surface, (image_x, image_y))

   # Render each line of the quote and blit to the screen
   line_height = 20  # Height of each line of text
   lines = selected_quote.split('\n')
   quote_y = image_y + image_surface.get_height() + 20  # Start position for the quote

   for line in lines:
       quote_surface = text_format(line, font, 10, white)
       quote_x = (screen_width - quote_surface.get_width()) // 2
       screen.blit(quote_surface, (quote_x, quote_y))
       quote_y += line_height  # Move down for the next line

   pygame.display.flip()

   # Wait for a few seconds
   pygame.time.wait(3000)  # 3000 milliseconds = 3 seconds
   print('test')
   mixer.music.stop()
   game_main()



def quit_confirmation():
 quit_messages = [
     "Are you sure you want to quit\nYes or No",
     "Are you really sure\nYes or No",
     "Are you absolutely sure\nYes or No",
     "Dont worry\nWe got you"
 ]

 for message in quit_messages:
     screen.fill(black)  # Clear the screen with blue color

     # Render each line of the message and blit to the screen
     line_height = 30  # Height of each line of text
     lines = message.split('\n')
     message_y = screen_height // 2 - (line_height * len(lines)) // 2  # Start position for the message

     for line in lines:
         message_surface = text_format(line, font, 25, white)
         message_x = (screen_width - message_surface.get_width()) // 2
         screen.blit(message_surface, (message_x, message_y))
         message_y += line_height  # Move down for the next line

     pygame.display.update()

     # Wait for the user's response
     waiting_for_response = True
     while waiting_for_response:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 return False  # Abort quit process
             if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_y:
                     waiting_for_response = False
                 elif event.key == pygame.K_n:
                     return False  # Abort quit process

 return False

def main_menu():
 mixer.music.load("main_soundtrack.mp3")
 mixer.music.play()
 menu = True
 selected = "start"
 current_background = 0
 background_change_interval = 5000
 last_change_time = pygame.time.get_ticks()
 global blinking_title_visible, last_blink, rolling_pos_x

 rolling_text_surface = text_format(rolling_text, font, 20, white)
 last_blink = pygame.time.get_ticks()
 while menu:
   
   current_time = pygame.time.get_ticks()
   if current_time - last_change_time > background_change_interval:
       current_background = (current_background + 1) % len(loaded_images)
       last_change_time = current_time
   screen.blit(loaded_images[current_background], (0, 0))
   for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_UP:
                 selected = "start"
             elif event.key == pygame.K_DOWN:
                 selected = "quit"
             if event.key == pygame.K_RETURN:
                 if selected == "start":
                    pass
                 elif selected == "quit":
                     if quit_confirmation():
                         pygame.quit()
                         sys.exit()
         if event.type == pygame.MOUSEBUTTONDOWN:
             if event.button == 1:  # Left mouse click
                 mouse_pos = event.pos
                 if start_rect.collidepoint(mouse_pos):
                     print("click start")
                     loading_screen()  # Call loading screen
                 elif quit_rect.collidepoint(mouse_pos):
                     if quit_confirmation():
                         pygame.quit()
                         sys.exit()

   current_time = pygame.time.get_ticks()
   if current_time - last_blink > blink_timer:
         blinking_title_visible = not blinking_title_visible
         last_blink = current_time


   if blinking_title_visible:
         title_line_1 = text_format("Gambling", font, 45, yellow)
         title_line_2 = text_format("Simulator", font, 45, yellow)
         title_rect_1 = title_line_1.get_rect(center=(screen_width // 2, 120))
         title_rect_2 = title_line_2.get_rect(center=(screen_width // 2, 170))
         screen.blit(title_line_1, title_rect_1)
         screen.blit(title_line_2, title_rect_2)

   rolling_pos_x -= rolling_speed
   if rolling_pos_x < -rolling_text_surface.get_width():
         rolling_pos_x = screen_width
   screen.blit(rolling_text_surface, (rolling_pos_x, screen_height - 30))

   text_start = text_format("START", font, 25, white if selected == "start" else black)
   text_quit = text_format("QUIT", font, 25, white)
   start_rect = text_start.get_rect(center=(screen_width // 2, 240))
   quit_rect = text_quit.get_rect(center=(screen_width // 2, 280))
   screen.blit(text_start, start_rect.topleft)
   screen.blit(text_quit, quit_rect.topleft)

   if selected == "quit":
       if quit_confirmation():
           break  # Break out of the menu loop to quit
       else:
           selected = "start"


   pygame.display.update()
   clock.tick(FPS)
   pygame.display.set_caption("Python - Pygame Simple Main Menu Selection")



main_menu()
pygame.quit()
sys.exit()