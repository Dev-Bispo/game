import pygame


class Obj(pygame.sprite.Sprite):
    def __init__(self, img, pos, z, t, grupos):
        super().__init__(grupos)

        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, t)
        self.rect = self.image.get_rect(topleft = pos)
        self.zcamadas = z

        if not isinstance(grupos, list):
            grupos = [grupos]
            
        
        # Adicionando a sprite a cada grupo na lista
        for grupo in grupos:
            grupo.add(self)
        print(f"Adicionado ao grupo: {grupo}, posição: {self.rect.topleft}")

