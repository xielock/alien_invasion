#-*-coding:utf-8-*-
import pygame.font
class Botton(object):
	def __init__(self,ai_settings,screen,msg):
		"""初始化按钮属性"""
		self.screen=screen
		self.screen_rect=screen.get_rect()
		
		#设置按钮尺寸和其他属性
		self.width,self.height=200,50
		self.botton_colour=(0,0,0)
		self.text_colour=(255,255,255)
		self.font=pygame.font.SysFont(None,48)
		#创建按钮的rect对象，并使其居中
		self.rect=pygame.Rect(0,0,self.width,self.height)
		self.rect.center=self.screen_rect.center
		
		self.prep_msg(msg)
	def prep_msg(self,msg):
		#将msg渲染为图像，并且在按钮上居中
		self.msg_image=self.font.render(msg,True,self.text_colour,
		self.botton_colour)
		self.msg_image_rect=self.msg_image.get_rect()
		self.msg_image_rect.center=self.rect.center
	def draw_botton(self):
		#绘制一个颜色填充的按钮，在绘制文本
		self.screen.fill(self.botton_colour,self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)
