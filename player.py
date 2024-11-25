import pygame
from objetos import *
from variaveis import *
import os
import time
from pygame.locals import *
from cena import *
import os



base_dir= os.path.dirname(__file__)
img_dir = os.path.join(base_dir, 'imagens')
img_dir2 = os.path.join(base_dir, 'png')
image_path9= os.path.join(img_dir2, 'Idle (1).png')

class Player(pygame.sprite.Sprite):
  
    
    def __init__(self, img, pos, z, collision_sprite, t, *groups):
        super().__init__(*groups)
        self.time = time.time()

        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, t)
        self.rect = self.image.get_rect(topleft = pos)
        self.collision_rect = self.rect.inflate(-1000, -1000)
        self.zcamadas = z
        self.collision_sprite = collision_sprite
        self.direction = pygame.math.Vector2()
        self.speed = 4
        self.frame = 0
        self.gravity = 1
        self.player_pos = pygame.Vector2(300, 300)  
        self.player_velocity = pygame.Vector2(0, 0)
         

 


    def colidir(self, path):
        

        if path == "horizontal":
            for sprite in self.collision_sprite:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    elif self.direction.x < 0:
                        self.rect.left = sprite.rect.right
                    
        if path == "vertical":
            for sprite in self.collision_sprite:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    elif self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
                    
                    
        

    def Run(self, speed, limit, t):
        self.base_dir = os.path.dirname(__file__)
        self.img_dir2 = os.path.join(base_dir, 'png')

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



        self.frame = (self.frame + speed) % limit
        self.frame = int(self.frame)
        self.image = self.sprites_run[self.frame]
        self.image = pygame.transform.scale(self.image, t)

    def Idle(self, speed, limit, t):
        self.idle2 = os.path.join(img_dir2, 'Idle (1).png')
        self.idle2 = os.path.join(img_dir2, 'Idle (2).png')
        self.idle3 = os.path.join(img_dir2, 'Idle (3).png')
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

        self.frame = (self.frame + speed) % limit
        self.frame = int(self.frame)
        self.image = self.sprites_idle[self.frame]
        self.image = pygame.transform.scale(self.image, t)

    def Hurt(self, speed, limit, t):
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

        self.frame = (self.frame + speed) % limit
        self.frame = int(self.frame)
        self.image = self.sprites_hurt[self.frame]
        self.image = pygame.transform.scale(self.image, t)

    def Dead(self, speed, limit, t):
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

        self.frame = (self.frame + speed) % limit
        self.frame = int(self.frame)
        self.image = self.sprites_dead[self.frame]
        self.image = pygame.transform.scale(self.image, t)

    def Jump(self, speed, limit, t):
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

        self.frame = (self.frame + speed) % limit
        self.frame = int(self.frame)
        self.image = self.sprites_jump[self.frame]
        self.image = pygame.transform.scale(self.image, t)

    def Runv(self, speed, limit, t):
        self.base_dir = os.path.dirname(__file__)
        self.img_dir2 = os.path.join(base_dir, 'png')

        self.run1 = os.path.join(img_dir2, 'Run (1)v.png')
        self.run2 = os.path.join(img_dir2, 'Run (2)v.png')
        self.run3 = os.path.join(img_dir2, 'Run (3)v.png')
        self.run4 = os.path.join(img_dir2, 'Run (4)v.png')
        self.run5 = os.path.join(img_dir2, 'Run (5)v.png')
        self.run6 = os.path.join(img_dir2, 'Run (6)v.png')
        self.run7 = os.path.join(img_dir2, 'Run (7)v.png')
        self.run8 = os.path.join(img_dir2, 'Run (8)v.png')

        self.sprites_run = []
        self.sprites_run.append(pygame.image.load(self.run1))
        self.sprites_run.append(pygame.image.load(self.run2))
        self.sprites_run.append(pygame.image.load(self.run3))
        self.sprites_run.append(pygame.image.load(self.run4))
        self.sprites_run.append(pygame.image.load(self.run5))
        self.sprites_run.append(pygame.image.load(self.run6))
        self.sprites_run.append(pygame.image.load(self.run7))
        self.sprites_run.append(pygame.image.load(self.run8))

        self.frame = (self.frame + speed) % limit
        self.frame = int(self.frame)
        self.image = self.sprites_run[self.frame]
        self.image = pygame.transform.scale(self.image, t)

    def Idlev(self, speed, limit, t):
        self.idle1 = os.path.join(img_dir2, 'Idle (1)v.png')
        self.idle2 = os.path.join(img_dir2, 'Idle (2)v.png')
        self.idle3 = os.path.join(img_dir2, 'Idle (3)v.png')
        self.idle4 = os.path.join(img_dir2, 'Idle (4)v.png')
        self.idle5 = os.path.join(img_dir2, 'Idle (5)v.png')
        self.idle6 = os.path.join(img_dir2, 'Idle (6)v.png')
        self.idle7 = os.path.join(img_dir2, 'Idle (7)v.png')
        self.idle8 = os.path.join(img_dir2, 'Idle (8)v.png')
        self.idle9 = os.path.join(img_dir2, 'Idle (9)v.png')
        self.idle10 = os.path.join(img_dir2, 'Idle (10)v.png')
        self.sprites_idle = []
        self.sprites_idle.append(pygame.image.load(self.idle1))
        self.sprites_idle.append(pygame.image.load(self.idle2))
        self.sprites_idle.append(pygame.image.load(self.idle3))
        self.sprites_idle.append(pygame.image.load(self.idle4))
        self.sprites_idle.append(pygame.image.load(self.idle5))
        self.sprites_idle.append(pygame.image.load(self.idle6))
        self.sprites_idle.append(pygame.image.load(self.idle7))
        self.sprites_idle.append(pygame.image.load(self.idle8))
        self.sprites_idle.append(pygame.image.load(self.idle9))
        self.sprites_idle.append(pygame.image.load(self.idle10))

        self.frame = (self.frame + speed) % limit
        self.frame = int(self.frame)
        self.image = self.sprites_idle[self.frame]
        self.image = pygame.transform.scale(self.image, t)

    def Hurdv(self, speed, limit, t):
        self.hurt1 = os.path.join(img_dir2, 'Hurt (1)v.png')
        self.hurt2 = os.path.join(img_dir2, 'Hurt (2)v.png')
        self.hurt3 = os.path.join(img_dir2, 'Hurt (3)v.png')
        self.hurt4 = os.path.join(img_dir2, 'Hurt (4)v.png')
        self.hurt5 = os.path.join(img_dir2, 'Hurt (5)v.png')
        self.hurt6 = os.path.join(img_dir2, 'Hurt (6)v.png')
        self.hurt7 = os.path.join(img_dir2, 'Hurt (7)v.png')
        self.hurt8 = os.path.join(img_dir2, 'Hurt (8)v.png')

        self.sprites_hurt = []
        self.sprites_hurt.append(pygame.image.load(self.hurt1))
        self.sprites_hurt.append(pygame.image.load(self.hurt2))
        self.sprites_hurt.append(pygame.image.load(self.hurt3))
        self.sprites_hurt.append(pygame.image.load(self.hurt4))
        self.sprites_hurt.append(pygame.image.load(self.hurt5))
        self.sprites_hurt.append(pygame.image.load(self.hurt6))
        self.sprites_hurt.append(pygame.image.load(self.hurt7))
        self.sprites_hurt.append(pygame.image.load(self.hurt8))
        self.frame = (self.frame + speed) % limit
        self.frame = int(self.frame)
        self.image = self.sprites_hurt[self.frame]
        self.image = pygame.transform.scale(self.image, t)

    def Deadv(self, speed, limit, t):
        self.dead1 = os.path.join(img_dir2, 'Deadv (1).png')
        self.dead2 = os.path.join(img_dir2, 'Deadv (2).png')
        self.dead3 = os.path.join(img_dir2, 'Deadv (3).png')
        self.dead4 = os.path.join(img_dir2, 'Deadv (4).png')
        self.dead5 = os.path.join(img_dir2, 'Deadv (5).png')
        self.dead6 = os.path.join(img_dir2, 'Deadv (6).png')
        self.dead7 = os.path.join(img_dir2, 'Deadv (7).png')
        self.dead8 = os.path.join(img_dir2, 'Deadv (8).png')
        self.dead9 = os.path.join(img_dir2, 'Deadv (9).png')
        self.dead10 = os.path.join(img_dir2, 'Deadv (10).png')

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

        self.frame = (self.frame + speed) % limit
        self.frame = int(self.frame)
        self.image = self.sprites_dead[self.frame]
        self.image = pygame.transform.scale(self.image, t)

    def Jumpv(self, speed, limit, t):
        self.jump1 = os.path.join(img_dir2, 'Jump (1)v.png')
        self.jump2 = os.path.join(img_dir2, 'Jump (2)v.png')
        self.jump3 = os.path.join(img_dir2, 'Jump (3)v.png')
        self.jump4 = os.path.join(img_dir2, 'Jump (4)v.png')
        self.jump5 = os.path.join(img_dir2, 'Jump (5)v.png')
        self.jump6 = os.path.join(img_dir2, 'Jump (6)v.png')
        self.jump7 = os.path.join(img_dir2, 'Jump (7)v.png')
        self.jump8 = os.path.join(img_dir2, 'Jump (8)v.png')
        self.jump9 = os.path.join(img_dir2, 'Jump (9)v.png')
        self.jump10 = os.path.join(img_dir2, 'Jump (10)v.png')
        self.jump11 = os.path.join(img_dir2, 'Jump (11)v.png')
        self.jump12 = os.path.join(img_dir2, 'Jump (12)v.png')

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

        self.frame = (self.frame + speed) % limit
        self.frame = int(self.frame)
        self.image = self.sprites_jump[self.frame]
        self.image = pygame.transform.scale(self.image, t)

    def input(self):
        
        self.player_velocity.y += self.gravity
        self.player_pos.y += self.player_velocity.y
        self.direction = pygame.math.Vector2(0, 0)
        
        self.slide_duration = 1

        keys = pygame.key.get_pressed()
        self.speed = int(5)

        if keys[pygame.K_RIGHT]:
            self.direction.x += self.speed
            self.Run(2, 8, [100, 100])
            
        elif keys[pygame.K_LEFT]:
            self.direction.x -= self.speed
            self.Runv(2, 8, [100, 100])


        elif keys[pygame.K_SPACE]:
            self.direction.y -= self.speed
            self.Jump(2, 10, [100, 100])
            
        elif keys[pygame.K_SPACE] and keys[pygame.K_RIGHT]:
            self.direction.y -= self.speed
            self.direction.x += self.speed
            self.Jump(2, 10, [100, 100])

        elif keys[pygame.K_d]:
            self.direction.y += 4

        elif self.direction == pygame.math.Vector2(0, 0):
            self.Idle(2, 10, [100, 100])




    def move(self):
        


        self.rect.x += self.direction.x * self.speed
        self.colidir("horizontal")
        

        self.rect.y += self.direction.y * self.speed
        self.colidir("vertical")
        
        self.collision_rect.center = self.rect.center

                     
    def verificador(self):
        
        self.rect.x += self.direction.x
        self.colidir("horizontal")
        
        self.rect.y += self.direction.y
        self.colidir("vertical")
        




    def update(self):
        self.input()
        self.move()






