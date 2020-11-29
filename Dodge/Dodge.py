import pygame
import pickle

def game_loop():
    import level_1

def game_instructions():
    import instructions 

pygame.init()

display_width = 1000
display_height = 600

HW,HH = display_width / 2, display_height / 2
AREA = display_width * display_height

white = (255,255,255)
black = (0,0,0,)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

player_width = 50
player_heigth = 50

gameDisplay = pygame.display.set_mode((display_width,display_height))
screen = gameDisplay
pygame.display.set_caption("MyPy")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
pygame.font.init()

joysticks = []
for i in range(0, pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()

pygame.mixer.music.load("audio/random silly chip song.wav")
pygame.mixer.music.play(-1)

pickle_in = open("data/topscore.dat", "rb")
topscore_save = pickle.load(pickle_in)
topscore = topscore_save

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  
        self.image = pygame.image.load("images/back.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        
bg = Background('images/background_image.png', [0,0])
kenny = pygame.image.load("images/kenny.png")

button1 = pygame.image.load("images/button1.png")
button2 = pygame.image.load("images/button2.png")
quit1 = pygame.image.load("images/quit1.png")
quit2 = pygame.image.load("images/quit2.png")


def draw_instuctions(surf, text, size, x, y):
    font = pygame.font.Font('fonts/Gretoon.ttf', 20)
    text = font.render("Instructions", True, red)
    surf.blit(text, (20, 10))


def get_instructions(x, y, w, h, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if click[0] == 1 and action != None:
            if action == "instructions":
                game_instructions()

def draw_topscore(surf, text, size, x, y):
    font = pygame.font.Font('fonts/Gretoon.ttf', 20)
    text = font.render("TopScore: " + str(topscore), True, red)
    surf.blit(text, (750, 10))

def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def button(x,y,w,h, b1, b2, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    gameDisplay.blit(b2,(x,y))
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()

        gameDisplay.blit(b1,(x,y))
  
def game_intro():
    intro = True

    pickle_in = open("data/topscore.dat", "rb")
    topscore_save = pickle.load(pickle_in)
    topscore = topscore_save

    while intro:

        for event in pygame.event.get():
            print(event)
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game_loop()

            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 9:
                    game_loop()

            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 8:
                    pygame.quit()
                    quit()

            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 6:
                    pygame.quit()
                    quit()

            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 7:
                    game_loop()

        gameDisplay.blit(bg.image, bg.rect)

        gameDisplay.blit(kenny,(425, 300))

        largeText = pygame.font.Font('fonts/SnackerComic.ttf',115)
        TextSurf, TextRect = text_objects("MyPy", largeText)
        TextRect.center = ((display_width/2),(display_height/3))
        gameDisplay.blit(TextSurf, TextRect)
 
        draw_topscore(screen, str(topscore_save), 20, 550, 10)
        draw_instuctions(screen, "Instructions", 20, 20, 10)

        button(200,500,100,39,button1,button2, "play")
        button(700,500,100,39,quit1,quit2, "quit")
        get_instructions(20, 10, 200, 40, "instructions")

        pygame.display.update()
        clock.tick(15)

game_intro()
pygame.quit()
quit
