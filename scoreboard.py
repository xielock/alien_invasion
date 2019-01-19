#-*-coding:utf-8-*-
import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard(object):
	"""��ʾ�÷���Ϣ"""
	def __init__(self,ai_settings,screen,stats):
		#��ʼ���÷��漰������
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.ai_settings=ai_settings
		self.stats=stats
		
		#��ʾ�÷ֵ���������
		self.text_colour=(30,30,30)
		self.font=pygame.font.SysFont(None,36)
		#׼����ʼ�÷�ͼ��
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()
	def prep_score(self):
		score_str=str(self.stats.score)
		rounded_score=int(round(self.stats.score,-1))
		score_str="{:,}".format(rounded_score)
		self.score_image=self.font.render('Score: '+score_str,True,
		self.text_colour,self.ai_settings.bg_colour)
		#�÷���ʾ�����Ͻ�
		self.score_rect=self.score_image.get_rect()
		self.score_rect.right=self.screen_rect.right-20
		self.score_rect.top=20
	def prep_high_score(self):
		high_score=int(round(self.stats.high_score,-1))
		high_score_str="{:,}".format(high_score)
		self.high_score_image=self.font.render('High score: '+high_score_str,
		True,self.text_colour,self.ai_settings.bg_colour)
		#�����м�
		self.high_score_rect=self.high_score_image.get_rect()
		self.high_score_rect.centerx=self.screen_rect.centerx
		self.high_score_rect.top=self.score_rect.top
	def prep_level(self):
		self.level_image=self.font.render('Level: '+str(self.stats.level),True,
		self.text_colour,self.ai_settings.bg_colour)
		self.level_rect=self.level_image.get_rect()
		self.level_rect.right=self.score_rect.right
		self.level_rect.top=self.score_rect.bottom+10
	def prep_ships(self):
		#��ʾ��ʣ�¼��Ҵ�
		self.ships=Group()
		for ship_number in range(self.stats.ships_left):
			ship=Ship(self.screen,self.ai_settings)
			ship.rect.x=10+ship_number*ship.rect.width
			ship.rect.y=5
			self.ships.add(ship)
		
		
	def show_score(self):
		"""��Ļ����ʾ�÷�"""
		self.screen.blit(self.score_image,self.score_rect)
		self.screen.blit(self.high_score_image,self.high_score_rect)
		self.screen.blit(self.level_image,self.level_rect)
		#���Ʒɴ�
		self.ships.draw(self.screen)











