import pygame
import os

class personagem(pygame.sprite.Sprite):
    def __init__(self, pos, z, t, *groups):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()

        base_dir = os.path.dirname(__file__)
        img_dir2 = os.path.join(base_dir, 'png')

        idle1 = os.path.join(img_dir2, 'Idle (1).png')

        self.image = pygame.image.load(idle1).convert_alpha()
        self.image = pygame.transform.scale(self.image, t)
        self.rect = self.image.get_rect(topleft=pos)
        self.zcamadas = z

        base_dir = os.path.dirname(__file__)
        img_dir2 = os.path.join(base_dir, 'png')

        self.idle2 = os.path.join(img_dir2, 'Idle (2).png')
        self. idle3 = os.path.join(img_dir2, 'Idle (3).png')
        self.idle4 = os.path.join(img_dir2, 'Idle (4).png')
        self.idle5 = os.path.join(img_dir2, 'Idle (5).png')
        self.idle6 = os.path.join(img_dir2, 'Idle (6).png')
        self.idle7 = os.path.join(img_dir2, 'Idle (7).png')
        self.idle8 = os.path.join(img_dir2, 'Idle (8).png')
        self.idle9 = os.path.join(img_dir2, 'Idle (9).png')
        self.idle10 = os.path.join(img_dir2, 'Idle (10).png')

        self.sprites_idle = []

        self.sprites_idle.append(pygame.image.load(self.idle2))
        self.sprites_idle.append(pygame.image.load(self.idle3))
        self.sprites_idle.append(pygame.image.load(self.idle4))
        self.sprites_idle.append(pygame.image.load(self.idle5))
        self.sprites_idle.append(pygame.image.load(self.idle6))
        self.sprites_idle.append(pygame.image.load(self.idle7))
        self.sprites_idle.append(pygame.image.load(self.idle8))
        self.sprites_idle.append(pygame.image.load(self.idle9))
        self.sprites_idle.append(pygame.image.load(self.idle10))

        self.hurt1 = os.path.join(img_dir2, 'Hurt (1).png')
        self.hurt2 = os.path.join(img_dir2, 'Hurt (2).png')
        self.hurt3 = os.path.join(img_dir2, 'Hurt (3).png')
        self.hurt4 = os.path.join(img_dir2, 'Hurt (4).png')
        self.hurt5 = os.path.join(img_dir2, 'Hurt (5).png')
        self.hurt6 = os.path.join(img_dir2, 'Hurt (6).png')
        self.hurt7 = os.path.join(img_dir2, 'Hurt (7).png')
        self.hurt8 = os.path.join(img_dir2, 'Hurt (8).png')

        self.sprites_hurt = []
        self.sprites_hurt.append(pygame.image.load(self.hurt1))
        self.sprites_hurt.append(pygame.image.load(self.hurt2))
        self.sprites_hurt.append(pygame.image.load(self.hurt3))
        self.sprites_hurt.append(pygame.image.load(self.hurt4))
        self.sprites_hurt.append(pygame.image.load(self.hurt5))
        self.sprites_hurt.append(pygame.image.load(self.hurt6))
        self.sprites_hurt.append(pygame.image.load(self.hurt7))
        self.sprites_hurt.append(pygame.image.load(self.hurt8))

        self.dead1 = os.path.join(img_dir2, 'Dead (1).png')
        self.dead2 = os.path.join(img_dir2, 'Dead (2).png')
        self.dead3 = os.path.join(img_dir2, 'Dead (3).png')
        self.dead4 = os.path.join(img_dir2, 'Dead (4).png')
        self.dead5 = os.path.join(img_dir2, 'Dead (5).png')
        self.dead6 = os.path.join(img_dir2, 'Dead (6).png')
        self.dead7 = os.path.join(img_dir2, 'Dead (7).png')
        self.dead8 = os.path.join(img_dir2, 'Dead (8).png')
        self.dead9 = os.path.join(img_dir2, 'Dead (9).png')
        self.dead10 = os.path.join(img_dir2, 'Dead (10).png')

        self.sprites_dead = []
        self.sprites_dead.append(pygame.image.load(self.dead1))
        self.sprites_dead.append(pygame.image.load(self.dead2))
        self.sprites_dead.append(pygame.image.load(self.dead3))
        self.sprites_dead.append(pygame.image.load(self.dead4))
        self.sprites_dead.append(pygame.image.load(self.dead5))
        self.sprites_dead.append(pygame.image.load(self.dead6))
        self.sprites_dead.append(pygame.image.load(self.dead7))
        self.sprites_dead.append(pygame.image.load(self.dead8))
        self.sprites_dead.append(pygame.image.load(self.dead9))
        self.sprites_dead.append(pygame.image.load(self.dead10))

        self.jump1 = os.path.join(img_dir2, 'Jump (1).png')
        self.jump2 = os.path.join(img_dir2, 'Jump (2).png')
        self.jump3 = os.path.join(img_dir2, 'Jump (3).png')
        self.jump4 = os.path.join(img_dir2, 'Jump (4).png')
        self.jump5 = os.path.join(img_dir2, 'Jump (5).png')
        self.jump6 = os.path.join(img_dir2, 'Jump (6).png')
        self.jump7 = os.path.join(img_dir2, 'Jump (7).png')
        self.jump8 = os.path.join(img_dir2, 'Jump (8).png')
        self.jump9 = os.path.join(img_dir2, 'Jump (9).png')
        self.jump10 = os.path.join(img_dir2, 'Jump (10).png')
        self.jump11 = os.path.join(img_dir2, 'Jump (11).png')
        self.jump12 = os.path.join(img_dir2, 'Jump (12).png')

        self.sprites_jump = []
        self.sprites_jump.append(pygame.image.load(self.jump1))
        self.sprites_jump.append(pygame.image.load(self.jump2))
        self.sprites_jump.append(pygame.image.load(self.jump3))
        self.sprites_jump.append(pygame.image.load(self.jump4))
        self.sprites_jump.append(pygame.image.load(self.jump5))
        self.sprites_jump.append(pygame.image.load(self.jump6))
        self.sprites_jump.append(pygame.image.load(self.jump7))
        self.sprites_jump.append(pygame.image.load(self.jump8))
        self.sprites_jump.append(pygame.image.load(self.jump9))
        self.sprites_jump.append(pygame.image.load(self.jump10))
        self.sprites_jump.append(pygame.image.load(self.jump11))
        self.sprites_jump.append(pygame.image.load(self.jump12))

        self.run1 = os.path.join(img_dir2, 'Run (1).png')
        self.run2 = os.path.join(img_dir2, 'Run (2).png')
        self.run3 = os.path.join(img_dir2, 'Run (3).png')
        self.run4 = os.path.join(img_dir2, 'Run (4).png')
        self.run5 = os.path.join(img_dir2, 'Run (5).png')
        self.run6 = os.path.join(img_dir2, 'Run (6).png')
        self.run7 = os.path.join(img_dir2, 'Run (7).png')
        self.run8 = os.path.join(img_dir2, 'Run (8).png')

        self.sprites_run = []
        self.sprites_run.append(pygame.image.load(self.run1))
        self.sprites_run.append(pygame.image.load(self.run2))
        self.sprites_run.append(pygame.image.load(self.run3))
        self.sprites_run.append(pygame.image.load(self.run4))
        self.sprites_run.append(pygame.image.load(self.run5))
        self.sprites_run.append(pygame.image.load(self.run6))
        self.sprites_run.append(pygame.image.load(self.run7))
        self.sprites_run.append(pygame.image.load(self.run8))

        self.slide1 = os.path.join(img_dir2, 'Slide (1).png')
        self.slide2 = os.path.join(img_dir2, 'Slide (2).png')
        self.slide3 = os.path.join(img_dir2, 'Slide (3).png')
        self.slide4 = os.path.join(img_dir2, 'Slide (4).png')
        self.slide5 = os.path.join(img_dir2, 'Slide (5).png')

        self.sprites_slide = []
        self.sprites_slide.append(pygame.image.load(self.slide1))
        self.sprites_slide.append(pygame.image.load(self.slide2))
        self.sprites_slide.append(pygame.image.load(self.slide3))
        self.sprites_slide.append(pygame.image.load(self.slide4))
        self.sprites_slide.append(pygame.image.load(self.slide5))

        self.agora = 0
        self.image = self.sprites_idle[self.agora]
        self.image = pygame.transform.scale(self.image, t)
        self.rect = self.image.get_rect(center=pos)
        self.rect.topleft = (100, 600)
        self.estado = "idle"

    def update(self):
        self.agora += 0.09
        if self.estado == "run":
            if self.agora >= len(self.sprites_run):
                self.agora = 0
            self.image = self.sprites_run[int(self.agora)]
        elif self.estado == "slide":
            if self.agora >= len(self.sprites_slide):
                self.agora = 0
            self.image = self.sprites_slide[int(self.agora)]

        else:
            if self.agora >= len(self.sprites_idle):
                self.agora = 0
            self.image = self.sprites_idle[int(self.agora)]
        self.image = pygame.transform.scale(self.image, (100, 100))
