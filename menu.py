import pygame
import sys
import time

from jogo import Chao
from variaveis import *
import pygame
import sys
from pygame.locals import *
from fases import *
from variaveis import *
from cena import *


pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Castle Scape")

fontp = pygame.font.Font('Blacklettersh.ttf', 140)
fontb = pygame.font.Font('white.TTF', 140)
sfontp = pygame.font.Font('Blacklettersh.ttf', 70)
sfontb = pygame.font.Font('white.TTF', 70)

BG = pygame.image.load('BG.jpg')
BG = pygame.transform.scale(BG, (1280, 720))

pygame.mixer.music.load('retro_music.mp3')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

volume = 1.0 
contador_tempo = True  


def draw_button(text, font, x, y, w, h, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, GRAY, (x, y, w, h))
        if click[0] == 1 and action is not None:
            pygame.time.wait(150)
            action()
    else:
        pygame.draw.rect(screen, WHITE, (x, y, w, h))

    bt = font.render(text, True, BLACK)
    screen.blit(bt , (x + (w - bt.get_width()) // 2, y + (h - bt.get_height()) // 2))

def play():
    print("Iniciando o jogo...")
    start = True
    game = Chao()
    game.run()
    running = False

def options_menu():
    global volume, contador_tempo

    while running:
        screen.fill("black")
        titulo = fontb.render("Opções", True, "white")
        screen.blit(titulo, (50, 50))

        status_volume = "Habilitar Volume" if volume == 0 else "Desabilitar Volume"
        status_contador = "Habilitar Contador" if not contador_tempo else "Desabilitar Contador"

        draw_button(status_volume, sfontb, 200, 450, 700, 110, habilitar_volume)
        draw_button(status_contador, sfontb, 200, 600, 700, 110, contador)
        draw_button("Voltar", sfontb, 200, 800, 400, 110, start_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def habilitar_volume():
    global volume
    if volume == 1.0:
        volume = 0.0
    else:
        volume = 1.0
    pygame.mixer.music.set_volume(volume)


def contador():
    global contador_tempo
    contador_tempo = not contador_tempo

def quit_game():
    pygame.quit()
    sys.exit()

def start_screen():
    while running:
        screen.blit(BG, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        titulo = fontb.render("Castle Scape", True, "white")
        screen.blit(titulo, (50, 50))

        draw_button("Jogar", sfontb, 750, 400, 300, 90, play)
        draw_button("Opções", sfontb, 750, 525, 300, 90, options_menu)
        draw_button("Sair", sfontb, 750, 650, 300, 90, quit_game)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

if running == True:
    start_screen()