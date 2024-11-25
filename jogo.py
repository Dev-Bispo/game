import pygame
import sys
from pygame.locals import *
from fases import *
from variaveis import *
from cena import *
from variaveis import *
from menu import *

pygame.init()


#classes
class Chao(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        pygame.init()
        self.display = pygame.display.set_mode([lar, alt])
        self.Block = Cena()
        self.mapa()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Castle Scape")





    def update(self):
        pass


    def run(self):

        # loop
        while True:
            mov = 250
            keys = pygame.key.get_pressed()
            camera = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        camera += mov

                    elif event.key == pygame.K_d:
                        camera -= mov


            for bloco in self.Block.block:
                bloco.rect.x += camera
                self.display.blit(bloco.image, bloco.rect)

            self.display.blit(fundo,(0,0))

            


            self.Block.run()
            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(60)






    def mapa(self):
        pass

if start == True:
    game = Chao()
    game.run()

