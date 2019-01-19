#-*-coding:utf-8-*-
import pygame.font
class Botton(object):
	def __init__(self,ai_settings,screen,msg):
		"""��ʼ����ť����"""
		self.screen=screen
		self.screen_rect=screen.get_rect()
		
		#���ð�ť�ߴ����������
		self.width,self.height=200,50
		self.botton_colour=(0,0,0)
		self.text_colour=(255,255,255)
		self.font=pygame.font.SysFont(None,48)
		#������ť��rect���󣬲�ʹ�����
		self.rect=pygame.Rect(0,0,self.width,self.height)
		self.rect.center=self.screen_rect.center
		
		self.prep_msg(msg)
	def prep_msg(self,msg):
		#��msg��ȾΪͼ�񣬲����ڰ�ť�Ͼ���
		self.msg_image=self.font.render(msg,True,self.text_colour,
		self.botton_colour)
		self.msg_image_rect=self.msg_image.get_rect()
		self.msg_image_rect.center=self.rect.center
	def draw_botton(self):
		#����һ����ɫ���İ�ť���ڻ����ı�
		self.screen.fill(self.botton_colour,self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)
