"""
File: plane_spirites.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-25 15:00:22
Function:


"""
import pygame

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

FRAME_PER_SEC = 60


class GameSprite(pygame.sprite.Sprite):
    """"飞机大战游戏精灵"""
    def __init__(self, image_name, speed=1):
        super().__init__()  # 调用父类初始化方法
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


