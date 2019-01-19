#-*-coding:utf-8-*-
class Settings(object):
	#�洢��Ϸ����������:��̬����
	def __init__(self):
		#��Ļ����
		self.screen_width=1200
		self.screen_height=800
		self.bg_colour=(138,43,226)
		self.ship_limit=3
		#�ӵ�����
		self.bullet_width=3
		self.bullet_height=15
		self.bullet_colour=(60,60,60)
		self.bullets_allowed=5
		#����������
		self.alien_drop_speed=10
		
		#��ʲô�ٶȼӿ���Ϸ���ࣺ��̬����
		self.speedup_scale=1.2
		self.score_scale=1.5
		
		self.initialize_dynamic_settings()
	def initialize_dynamic_settings(self):
		self.ship_speed_factor=1.5
		self.bullet_speed_factor=3
		self.alien_speed_factor=1
		#self.fleet_directionΪ1��ʾ���ƣ�Ϊ-1��ʾ�����
		self.fleet_direction=1
		self.alien_points=50
		
	def increase_speed(self):
		#����ٶ�����
		self.ship_speed_factor*=self.speedup_scale
		self.bullet_speed_factor*=self.speedup_scale
		self.alien_speed_factor*=self.speedup_scale
		self.alien_points=int(self.alien_points*self.score_scale)
