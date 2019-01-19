#-*-coding:utf-8-*-
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""һ���Էɴ�������ӵ����й������"""
	def __init__(self,ai_settings,screen,ship):
		super(Bullet,self).__init__()
		self.screen=screen
		#�ڣ�0,0��������һ����ʾ�ӵ��ľ��Σ����ƶ�����ȷλ��
		self.rect=pygame.Rect(0,0,ai_settings.bullet_width,
		ai_settings.bullet_height)
		self.rect.centerx=ship.rect.centerx
		self.rect.top=ship.rect.top
		#�洢��С����ʶ���ӵ�λ��
		self.y=float(self.rect.y)
		self.colour=ai_settings.bullet_colour
		self.speed_factor=ai_settings.bullet_speed_factor
	def update(self):
		"""�����ƶ��ӵ�"""
		#���±�ʾ�ӵ�λ�õ�С��ֵ
		self.y-=self.speed_factor
		#���±�ʾ�ӵ���rectλ��
		self.rect.y=self.y
		
	def draw_bullet(self):
		#���ӵ�
		pygame.draw.rect(self.screen,self.colour,self.rect)
		
