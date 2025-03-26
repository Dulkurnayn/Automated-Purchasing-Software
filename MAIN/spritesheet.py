import pygame

class Spritesheet:
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert_alpha()
        
       
       
        #self.sprite_sheet  = self.sprite_sheet .convert_alpha()
          
    

    def get_sprite(self, x, y, w, h):
        sprite = pygame.Surface((w, h))
        DEFAULT_IMAGE_SIZE = (100, 100)

        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprite_sheet,(0, 0),(x, y, w, h))
        sprite= pygame.transform.scale(sprite, DEFAULT_IMAGE_SIZE)

        return sprite

   ## def parse_sprite(self, name):
     #   sprite = self.data['frames'][name]['frame']
      #  x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
       # image = self.get_sprite(x, y, w, h)
        #return image
    """
import pygame
from pygame.locals import *
display = pygame.display.set_mode((1024,1024)) # window size is determined here
pygame.init()
character = pygame.image.load("/home/mustafashakil6/GAME/car.png")
#background = pygame.image.load("/home/mustafashakil6/aro.png")
characterx = 0
charactery = 0
while True:
    #display.blit(background,(0,0))
    #display.bgcolor("black")
    display.blit(character,(characterx,charactery))
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            exit()

    keys= pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        characterx -= 20
    if keys[pygame.K_RIGHT]:
        characterx += 20
    if keys[pygame.K_UP]:
        charactery += 20
    if keys[pygame.K_DOWN]:
        charactery -= 20
    
    pygame.display.update()
    """
    """if event.type == KEYDOWN:
            while event.key == K_a:
                characterx -= 20
            if event.key == K_d:
                characterx += 20
            if event.key == K_w:
                charactery -= 20
            if event.key == K_s:
                charactery += 20
                if event.type = pygame.key.get_pressed:
            if event.key == K_a:
                index = (index + 1) % len(spritel)
                characterx -= 2
                canvas.blit(spriteL[index], (0, HEIGHT- 128))
            if event.key == K_d:
                index = (index + 1) % len(trainerr)
                characterx += 2
                canvas.blit(trainer[index], (0, HEIGHT - 128))
            if event.key == K_w
                index = (index + 1) % len(trainerd)
                charactery -= 2
                canvas.blit(trainer[index], (0, HEIGHT - 128))
            if event.key == K_s:
                index = (index + 1) % len(traineru)
                charactery += 2
                canvas.blit(trainer[index], (0,HEIGHT - 128)"""
    
"""
 pygame.transform.scale(trainer[index], (636, 520))
import pygame
import json

class Spritesheet:
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert()
        self.meta_data = self.filename.replace('png', 'json')
        with open(self.meta_data) as f:
            self.data = json.load(f)
        f.close()



    def get_sprite(self, x, y, w, h):
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprite_sheet,(0, 0),(x, y, w, h))
        return sprite

    def parse_sprite(self, name):
        sprite = self.data['frames'][name]['frame']
        x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = self.get_sprite(x, y, w, h)
        return image
        import pygame
from spritesheet import Spritesheet

################################# LOAD UP A BASIC WINDOW #################################
pygame.init()
DISPLAY_W, DISPLAY_H = 480, 270
canvas = pygame.Surface((DISPLAY_W,DISPLAY_H))
window = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))
running = True
###########################################################################################

my_spritesheet = Spritesheet('trainer_sheet.png')
trainer = [my_spritesheet.parse_sprite('trainer1.png'), my_spritesheet.parse_sprite('trainer2.png'),my_spritesheet.parse_sprite('trainer3.png'),
           my_spritesheet.parse_sprite('trainer4.png'),my_spritesheet.parse_sprite('trainer5.png')]
f_trainer = [my_spritesheet.parse_sprite('f_trainer1.png'), my_spritesheet.parse_sprite('f_trainer2.png'),my_spritesheet.parse_sprite('f_trainer3.png'),
           my_spritesheet.parse_sprite('f_trainer4.png'),my_spritesheet.parse_sprite('f_trainer5.png')]
index = 0

while running:
    ################################# CHECK PLAYER INPUT #################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            ############### UPDATE SPRITE IF SPACE IS PRESSED #################################
            if event.key == pygame.K_SPACE:
                index = (index + 1) % len(trainer)


    ################################# UPDATE WINDOW AND DISPLAY #################################
    canvas.fill((255,255,255))
    canvas.blit(trainer[index], (0, DISPLAY_H - 128))
    canvas.blit(f_trainer[index], (128, DISPLAY_H - 128))
    window.blit(canvas, (0,0))
    pygame.display.update()

"""
