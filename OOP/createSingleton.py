"""
File: danli.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-22 16:27:43
Function:


"""


class MusicPlayer(object):

    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if MusicPlayer.init_flag:
            return
        print('player is initialized')
        MusicPlayer.init_flag = True


player1 = MusicPlayer()
player2 = MusicPlayer()
print(player1)
print(player2)