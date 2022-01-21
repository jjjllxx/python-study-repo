"""
File: plane_main.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-25 17:20:22
Function:


"""
import pygame
from plane_spirites import *


class PlaneGame(object):
    """main game"""

    def __init__(self):
        print('游戏初始化')
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()

    def __create_sprites(self):
        pass

    def start_game(self):
        print('游戏开始')

        while True:

            self.clock.tick(FRAME_PER_SEC)


            self.__event_handler()

            self.__check_collide()

            self.__update_sprites()

            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

    def __check_collide(self):
        pass

    def __update_sprites(self):
        pass

    @staticmethod
    def __game_over():
        print('游戏结束')
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()

