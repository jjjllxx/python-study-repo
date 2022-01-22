"""
File: gamelei.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-22 15:49:11
Function:


"""


class Game:
    top_score = 0

    def __init__(self, name):
        self.name = name

    @classmethod
    def show_top_score(cls):
        print('the history top score is', cls.top_score)

    @staticmethod
    def show_help():
        print('show help information')

    def start_game(self):
        print(f'{self.name} starts game')


Game.show_help()
Game.show_top_score()
player1 = Game('player1')
player1.start_game()