#-*-coding:utf-8-*-
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from botton import Botton
from scoreboard import Scoreboard
from pygame.locals import *
import game_function as gf

def run_game():
	# ��ʼ����Ϸ������һ����Ļ����
	pygame.init()
	pygame.mixer.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,
	ai_settings.screen_height))
	pygame.display.set_caption('Alien Invasion')
	#����play��ť
	play_botton=Botton(ai_settings,screen,'Play')
	#���ñ���ɫ(����������Ļ�ϲ���
	bg_colour=ai_settings.bg_colour
	#����һ�ҷɴ�������һ�����ڴ洢�ӵ��ı��飬�����˱���
	ship=Ship(screen,ai_settings)
	bullets=Group()
	aliens=Group()
	#����������Ⱥ
	gf.create_fleet(ai_settings,screen,ship,aliens)
	#����һ���洢ͳ����Ϣ��ʵ��,�������Ƿ���
	stats=GameStats(ai_settings)
	sb=Scoreboard(ai_settings,screen,stats)
	#��������
	pygame.mixer.music.load('bg_music.ogg')
	pygame.mixer.music.set_volume(0.2)
	pygame.mixer.music.play(-1)
	pause=False
	#������Ч
	bullet_sound=pygame.mixer.Sound('bullet_music.wav')
	bullet_sound.set_volume(0.2)
	#��ʼ��ѭ��
	while True:
		gf.check_events(ai_settings,screen,stats,sb,play_botton,ship,
		aliens,bullets,bullet_sound)
		if pause:
			pygame.mixer.music.pause()
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
			gf.update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets)
		#���в�����if�жϣ�����������
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,
		play_botton)
run_game()
