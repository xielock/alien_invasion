#-*-coding:utf-8-*-
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	def __init__(self,ai_settings,screen):
		#��ʼ�������˲���ʼ��λ��
		super(Alien,self).__init__()
		self.screen=screen
		self.ai_settings=ai_settings
		#����������ͼ��
		self.image=pygame.image.load('alien.bmp')
		self.rect=self.image.get_rect()
		
		#������λ�������ϽǸ���
		self.rect.x=self.rect.width-50
		self.rect.y=self.rect.height-50
		
		#�洢�����˵�λ��
		self.x=float(self.rect.x)
	def blitme(self):
		#����
		self.screen.blit(self.image,self.rect)
	def check_edges(self):
		"""����ڱ�Ե���ͷ���true"""
		screen_rect=self.screen.get_rect()
		if self.rect.right>screen_rect.right:
			return True
		elif self.rect.left<0:
			return True
	def update(self):
		#������������ƶ�
		self.x+=(self.ai_settings.alien_speed_factor*
		self.ai_settings.fleet_direction)
		self.rect.x=self.x







	
