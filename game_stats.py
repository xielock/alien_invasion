#-*-coding:utf-8-*-
class GameStats(object):
	"""������Ϸͳ����Ϣ"""
	def __init__(self,ai_settings):
		#��ʼ��ͳ����Ϣ
		self.ai_settings=ai_settings
		self.reset_stats()
		self.game_active=False
		with open ('high_score.txt')as hs:
			lines=hs.read()
			self.high_score=float(lines)
	def reset_stats(self):
		self.ships_left=self.ai_settings.ship_limit
		self.score=0
		self.level=1
