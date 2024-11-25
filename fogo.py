import pygame
from variaveis import *


base_dir= os.path.dirname(__file__)
img_dir = os.path.join(base_dir, 'imagens')
img_dir2 = os.path.join(base_dir, 'png')

image_path1 = os.path.join(img_dir2, 'bloco.png')
image_path2 = os.path.join(img_dir2, 'fogo3.png')
image_path2_1 = os.path.join(img_dir2, 'fogo2.png')
image_path2_2 = os.path.join(img_dir2, 'fogo1.png')

class Anima(pygame.sprite.Sprite):

     def __init__(self, pos, z, t, *groups):
        super().__init__(*groups)

        self.frame = [
            image_path2,
            image_path2_1,
            image_path2_2
        ]


        self.speed = 0
        self.frame = [pygame.transform.scale(pygame.image.load(frame), t) for frame in self.frame]
        self.image = self.frame[self.speed]
        self.rect = self.image.get_rect(topleft=pos)
        self.zcamadas = z

        self.time = 185
        self.updatetime = pygame.time.get_ticks()

     def update(self):
        now = pygame.time.get_ticks()
        if now - self.updatetime > self.time:
            self.updatetime = now
            self.speed = (self.speed + 1) % len(self.frame)
            self.image = self.frame[self.speed]





