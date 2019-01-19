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
	# 初始化游戏并创建一个屏幕对象
	pygame.init()
	pygame.mixer.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,
	ai_settings.screen_height))
	pygame.display.set_caption('Alien Invasion')
	#创建play按钮
	play_botton=Botton(ai_settings,screen,'Play')
	#设置背景色(可与填满屏幕合并）
	bg_colour=ai_settings.bg_colour
	#创建一艘飞船，创建一个用于存储子弹的编组，外星人编组
	ship=Ship(screen,ai_settings)
	bullets=Group()
	aliens=Group()
	#创建外星人群
	gf.create_fleet(ai_settings,screen,ship,aliens)
	#创建一个存储统计信息的实例,并创建记分牌
	stats=GameStats(ai_settings)
	sb=Scoreboard(ai_settings,screen,stats)
	#背景音乐
	pygame.mixer.music.load('bg_music.ogg')
	pygame.mixer.music.set_volume(0.2)
	pygame.mixer.music.play(-1)
	pause=False
	#创建音效
	bullet_sound=pygame.mixer.Sound('bullet_music.wav')
	bullet_sound.set_volume(0.2)
	#开始主循环
	while True:
		gf.check_events(ai_settings,screen,stats,sb,play_botton,ship,
		aliens,bullets,bullet_sound)
		if pause:
			pygame.mixer.music.pause()
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
			gf.update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets)
		#此行不依赖if判断！！！！！！
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,
		play_botton)
run_game()
