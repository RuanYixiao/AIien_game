# -*- coding: utf-8 -*-

import sys

import pygame

from settings import Settings

from ship import Ship

from alien import Alien

import game_functions as gf

from pygame.sprite import Group

def run_game():
	#初始化游戏并创建一个屏幕对象
	#1、初始化游戏；
	pygame.init()
	ai_settings = Settings()
	#2、设置游戏框的长宽；
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	#3、设置游戏的名称；
	pygame.display.set_caption("Alien Invasion For NN")

	#创建一艘飞船
	ship = Ship(ai_settings, screen)
	bullets = Group()

	#创建一个外星人
	alien = Alien(ai_settings, screen)

	#

	#开始游戏的主循环
	while True:
		
		#监视键盘和鼠标的事件
		gf.check_events(ai_settings,screen, ship, bullets)

		#飞船更新位置
		ship.update()
		
		#删除已消失的子弹
		#更新子弹的位置
		gf.update_bullets(bullets)

		#每次循环时都重绘屏幕
		gf.update_screen(ai_settings, screen, ship, alien, bullets)

run_game()