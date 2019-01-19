#-*-coding:utf-8-*-
import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
	def __init__(self,screen,ai_settings):
		super(Ship,self).__init__()
		self.screen=screen
		self.ai_settings=ai_settings
		#加载飞船图像并获取其外接矩形
		self.image=pygame.image.load('ships.bmp')
		self.rect=self.image.get_rect()
		self.screen_rect=self.screen.get_rect()
		
		#将飞船放在屏幕底部中央
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom
		#存储小数值
		self.center=float(self.rect.centerx)
		#移动标志
		self.moving_right=False
		self.moving_left=False
	def update(self):
			#根据标志移动飞船位置 并且检测在屏幕以内！！
			if self.moving_right and self.rect.right<self.screen_rect.right:
				self.center+=self.ai_settings.ship_speed_factor
			if self.moving_left and self.rect.left>0:
				self.center-=self.ai_settings.ship_speed_factor
			#根据self.center更新rect对象
			self.rect.centerx=self.center
	def blitme(self):
		#绘制飞船
		self.screen.blit(self.image,self.rect)
	def center_ship(self):
		#飞船在屏幕居中
		self.center=self.screen_rect.centerx
			
