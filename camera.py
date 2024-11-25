import pygame

from fases import *
from variaveis import *
lar = 1280
alt = 720
class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

        self.display = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def seguindop(self, player):
        self.offset.x = player.rect.centerx - lar / 2
        self.offset.y = player.rect.centery - alt / 2

    def seguindo(self):
        for layer in camadas.values():
            for sprite in self.sprites():
                if sprite.zcamadas == layer:
                    off_rect = sprite.rect.copy()
                    off_rect.center -= self.offset
                    self.display.blit(sprite.image, off_rect)
