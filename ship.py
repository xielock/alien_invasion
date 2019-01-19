#-*-coding:utf-8-*-
import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
	def __init__(self,screen,ai_settings):
		super(Ship,self).__init__()
		self.screen=screen
		self.ai_settings=ai_settings
		#���طɴ�ͼ�񲢻�ȡ����Ӿ���
		self.image=pygame.image.load('ships.bmp')
		self.rect=self.image.get_rect()
		self.screen_rect=self.screen.get_rect()
		
		#���ɴ�������Ļ�ײ�����
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom
		#�洢С��ֵ
		self.center=float(self.rect.centerx)
		#�ƶ���־
		self.moving_right=False
		self.moving_left=False
	def update(self):
			#���ݱ�־�ƶ��ɴ�λ�� ���Ҽ������Ļ���ڣ���
			if self.moving_right and self.rect.right<self.screen_rect.right:
				self.center+=self.ai_settings.ship_speed_factor
			if self.moving_left and self.rect.left>0:
				self.center-=self.ai_settings.ship_speed_factor
			#����self.center����rect����
			self.rect.centerx=self.center
	def blitme(self):
		#���Ʒɴ�
		self.screen.blit(self.image,self.rect)
	def center_ship(self):
		#�ɴ�����Ļ����
		self.center=self.screen_rect.centerx
			
