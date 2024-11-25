import pygame
import os
from cena import *

#variaveis

#image
base_dir= os.path.dirname(__file__)
img_dir = os.path.join(base_dir, 'imagens')
img_dir2 = os.path.join(base_dir, 'png')
image_path8 = os.path.join(img_dir2, 'ai-generated-8469399_1280.jpg')

image_path10 = os.path.join(img_dir2, 'fogo1.png')
image = pygame.image.load(image_path8)
fogo = pygame.image.load(image_path10)
lar = 1280
alt = 720
lar_fogo = 150
alt_fogo =150
tel = pygame.display.set_mode((lar, alt))
running = True
start = False
clock = pygame.time.Clock()
image_fogo = pygame.transform.scale(fogo,(lar_fogo,alt_fogo))
fundo = pygame.transform.scale(image,(lar,alt))




camera = 0
x = 0




#grupos
block = pygame.sprite.Group()