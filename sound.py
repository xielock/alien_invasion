#-*-coding:utf-8-*-
import pygame 
import sys
from pygame.locals import *
#≥ı ºªØ
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('bg_music.ogg')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

bullet_sound=pygame.mixer.sound('')
bullet_sound.set_volume(0.2)
alien_sound=pygame.mixer.sound('')
alien_sound.set_volume(0.2)

bg_size=width,height=300,200
ecreen=pagame.display.set_mode(bg_size)
pygame.display.set_caption('Alien Invasion')
