# -*- coding: utf-8 -*-

class Settings(object):
	"""储存《外星人入侵》的所有设置类"""
	def __init__(self):
		"""初始化游戏的设置"""
		#屏幕设置
		self.screen_width = 1100
		self.screen_height = 700
		self.bg_color = (255,255,255)
		
		#飞船速度设置
		self.ship_speed_factor = 1.5

		#子弹设置
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		#橘色子弹
		self.bullet_color = 255, 128, 114
		self.bullets_allowed = 5
