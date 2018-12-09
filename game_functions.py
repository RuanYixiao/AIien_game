# -*- coding: utf-8 -*-

import sys

import pygame

from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""按键按下"""
	if event.key == pygame.K_RIGHT:
		#向右移动飞船标志位
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		#向左移动飞船标志位
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
	elif event.key == pygame.K_q:
		sys.exit()


def check_keyup_events(event, ship):
	"""按键松开"""
	if event.key == pygame.K_RIGHT:
		#向右移动标志位置0
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		#向左移动飞船标志位
		ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
	"""响应按键和鼠标事件"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, alien, bullets):
	"""更新屏幕上的图像，并切换到新屏幕"""
	#每次循环时都重新绘制屏幕
	screen.fill(ai_settings.bg_color)

	#在飞船和外星人后面重绘所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	#将ship图片覆盖到背景上
	ship.blitme()
	#将外星人绘制到屏幕上
	alien.blitme()

	#让最近绘制的屏幕可见
	#pygame.display.flip()
	pygame.display.update()


def update_bullets(bullets):
	"""更新子弹的位置，并删除已消失的子弹"""
	#更新子弹的位置

	bullets.update()

	#删除子弹的位置
	#删除已消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
			#print(len(bullets))	

def fire_bullet(ai_settings, screen, ship, bullets):
	#如果子弹数量还没达到限制就发射一发子弹
	#创建一个子弹，并将其加入到编组的bullets中
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship) #new_bullet是子弹Bullet的一个实例
		bullets.add(new_bullet) #将new_bullet加入到编组中
	