import pygame
import os
import pickle
import time

WIDTH = 1000
HEIGHT = 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()
pygame.mixer.init()
pygame.joystick.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("MyPy")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

joysticks = []
for i in range(0, pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()
    print("Detected Joystick '", joysticks[-1].get_name(), "'")

kenny = pygame.image.load("images/kenny.png")

pickle_in = open("data/score.dat", "rb")
score_save = pickle.load(pickle_in)
score = score_save

pickle_in = open("data/topscore.dat", "rb")
topscore_save = pickle.load(pickle_in)
topscore = topscore_save

#BACKGROUND
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/back.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

bg = Background('images/background_image.png', [0, 0])

#drawing surfaces
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font('fonts/Gretoon.ttf', 20)
    text = font.render("Score: " + str(score), True, RED)
    surf.blit(text, (20, 10))

def text_objects(text, font):
    textSurface = font.render(text, True, RED)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('fonts/SnackerComic.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((WIDTH/2), (HEIGHT/2))
    screen.blit(TextSurf, TextRect)

def draw_topscore(surf, text, size, x, y):
    font = pygame.font.Font('fonts/Gretoon.ttf', 20)
    text = font.render("TopScore: " + str(topscore), True, RED)
    surf.blit(text, (750, 10))

button1 = pygame.image.load("images/button1.png")
button2 = pygame.image.load("images/button2.png")
quit1 = pygame.image.load("images/quit1.png")
quit2 = pygame.image.load("images/quit2.png")

#BUTTON
def button(x, y, w, h, b1, b2, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    screen.blit(b2, (x, y))
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()
            if action == "unpause":
                unpause()
                pause = False
            elif action == "quit":
                pygame.quit()

        screen.blit(b1, (x, y))

def unpause():
    global pause
    pause = False

pause = True
#PAUSE

while pause:
        
        screen.blit(bg.image, bg.rect)
        screen.blit(kenny, (425, 300))
        largeText = pygame.font.Font('fonts/SnackerComic.ttf', 115)
        TextSurf, TextRect = text_objects("Level Cleared", largeText)
        TextRect.center = ((WIDTH/2), (HEIGHT/3))
        screen.blit(TextSurf, TextRect)

        draw_topscore(screen, str(topscore_save), 20, 550, 10)
        draw_text(screen, str(score), 20, WIDTH, HEIGHT)
        
        pygame.display.update()
        clock.tick(15)
        time.sleep(5)
        import Level_4
