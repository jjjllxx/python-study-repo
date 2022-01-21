"""
File: welcome_to_pygame.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-23 16:16:39
Function:


"""
import pygame
from plane_spirites import *

pygame.init()
game_window = pygame.display.set_mode((480, 700))  # 设置界面大小（和背景图大小一致）

background_image = pygame.image.load('./images/background.png')
hero = pygame.image.load('./images/me1.png')  # 找到背景图和飞机的素材

game_window.blit(background_image, (0, 0))
game_window.blit(hero, (189, 500))  # 设置初始的飞机和背景图

pygame.display.update()  # 更新屏幕

clock = pygame.time.Clock()

hero_rect = pygame.Rect(189, 500, 102, 126)

enemy = GameSprite('./images/enemy1.png')
enemy1 = GameSprite('./images/enemy1.png', 2)
enemy1.rect.x += 180
enemy_group = pygame.sprite.Group(enemy, enemy1)

while True:
    clock.tick(60)  # 制定循环体内部代码执行的频率

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print('退出游戏')
            pygame.quit()
            exit()  # 判断事件类型是否是退出事件

    hero_rect.y -= 1
    if hero_rect.y <= -126:
        hero_rect.y = 700  # 到顶部后从底部出现

    game_window.blit(background_image, (0, 0))  # 重新绘制背景图片遮挡之前的飞机残影
    game_window.blit(hero, hero_rect)

    enemy_group.update()  # 让组中所有精灵更新位置
    enemy_group.draw(game_window)  # 在屏幕上绘制所有的精灵

    pygame.display.update()


