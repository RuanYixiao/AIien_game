
import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
	"""docstring for Alien"Sprite"""
	def __init__(self, ai_settings, screen):
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		#加载外星人图像，并设置rect属性
		self.image = pygame.image.load('images/Alien1.png')
		self.rect = self.image.get_rect()

		#每个外星人最初都是在屏幕左上角
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#储存外星人的精确位置
		self.x = float(self.rect.x)


	def blitme(self):
		self.screen.blit(self.image, self.rect)


		
		