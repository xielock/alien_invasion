#-*-coding:utf-8-*-
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""一个对飞船发射的子弹进行管理的类"""
	def __init__(self,ai_settings,screen,ship):
		super(Bullet,self).__init__()
		self.screen=screen
		#在（0,0）处创建一个表示子弹的矩形，并移动到正确位置
		self.rect=pygame.Rect(0,0,ai_settings.bullet_width,
		ai_settings.bullet_height)
		self.rect.centerx=ship.rect.centerx
		self.rect.top=ship.rect.top
		#存储用小数标识的子弹位置
		self.y=float(self.rect.y)
		self.colour=ai_settings.bullet_colour
		self.speed_factor=ai_settings.bullet_speed_factor
	def update(self):
		"""向上移动子弹"""
		#更新表示子弹位置的小数值
		self.y-=self.speed_factor
		#更新表示子弹的rect位置
		self.rect.y=self.y
		
	def draw_bullet(self):
		#画子弹
		pygame.draw.rect(self.screen,self.colour,self.rect)
		
