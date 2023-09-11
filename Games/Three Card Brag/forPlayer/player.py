"""
File: wanjia.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-06-10 20:13:51
Function:


"""
import time
import random

class Player:
    def __init__(self, player_no=0, init_chip=500):
        self.isBlind = 1
        self.chip = init_chip
        self.chip_on = 0
        self.field_chip = 20
        self.isOut = 0
        self.action_coin = 1
        self.isBanker = 0
        self.round_num = 1
        self.player_no = player_no
        self.player_choice = self.player_no
        self.win_times = 0
        if self.player_no == 0:
            self.player_name = input('请输入您的游戏昵称： ')
        else:
            self.player_name = '玩家'+str(self.player_no)

    def deliverCard(self, hand_card):
        self.hand_card = hand_card

    def openEyes(self):
        print(self.hand_card)
        self.isBlind = 0
        print(self.player_name, '看牌', end=' ')

    def putChip(self):
        if self.isBlind == 1:
            self.chip -= self.field_chip / 2
            self.chip_on += self.field_chip / 2
        else:
            self.chip -= self.field_chip
            self.chip_on += self.field_chip
        self.action_coin = 1
        if self.isBlind == 1:
            print(self.player_name, '不看牌 跟牌')
        else:
            print(self.player_name, '跟牌')

    def doubleChip(self):
        self.chip -= self.field_chip * 2
        self.chip_on += self.field_chip * 2
        self.action_coin = 2
        print(self.player_name, '加倍')

    def openSomebody(self, player_l):
        while True:
            try:
                i = int(input('请输入玩家序号(请输入尚未离场的玩家的代号)'))
                self.player_choice = player_l[i]
                if player_l[i].isOut != 1:
                    break
                else:
                    print('该玩家已离场，请重新输入')
            except:
                print('该玩家不存在，请重新输入')

        if self.isBlind == 1:
            self.chip -= self.field_chip
            self.chip_on += self.field_chip
        else:
            self.chip -= self.field_chip * 2
            self.chip_on += self.field_chip * 2
        print(self.player_name, '开玩家', self.player_choice.player_name)
        self.action_coin = 3

    def throwCard(self):
        self.isOut = 1
        self.action_coin = 0
        print(self.player_name, '扔牌')

    def __str__(self):
        if self.isOut == 1:
            return f'{self.player_name}已经离场'
        else:
            if self.isBlind == 1:
                return f'{self.player_name}是盲人，这局已经投入{self.chip_on}筹码'
            else:
                return f'{self.player_name}是明眼人，这局已经投入{self.chip_on}筹码'


class RealPlayer(Player):
    def takeAction(self, player_choice0, player_l):
        while True:
            if self.round_num == 1:
                if self.isBlind == 1:
                    self.putChip()
                else:
                    if player_choice0 == '2':
                        self.doubleChip()
                    elif player_choice0 == '3':
                        self.throwCard()
                    else:
                        self.putChip()
            else:
                if self.isBlind == 1:
                    if player_choice0 == '2':
                        self.openSomebody(player_l)
                    else:
                        self.putChip()
                else:
                    if player_choice0 == '2':
                        self.doubleChip()
                    elif player_choice0 == '3':
                        self.throwCard()
                    elif player_choice0 == '4':
                        self.openSomebody(player_l)
                    else:
                        self.putChip()
            break

    def ActionList(self, player_l):
        open_or_not = input(f'{self.player_name}是否看牌？ 1.看牌 2.不看牌 ')
        if open_or_not == '1':
            print(self.hand_card)
            self.isBlind = 0
        if self.round_num == 1:
            if self.isBlind == 1:
                player_choice = input(f'第1轮，你现在是盲人，有{self.chip}筹码，可以 1.跟牌（{self.field_chip/2}筹码）')
                self.takeAction(player_choice, player_l)
            else:
                player_choice = input(f'第1轮，你现在是明眼人，有{self.chip}筹码，可以 1.跟牌（{self.field_chip}筹码） '
                                      f'2.加倍（{self.field_chip*2}筹码） 3.扔牌 ')
                self.takeAction(player_choice, player_l)
        else:
            if self.isBlind == 1:
                player_choice = input(f'第{self.round_num}轮，你现在是盲人，有{self.chip}筹码，可以 '
                                      f'1.跟牌（{self.field_chip/2}筹码） 2.开某位玩家（{self.field_chip}筹码） ')
                self.takeAction(player_choice, player_l)
            else:
                player_choice = input(f'第{self.round_num}轮，你现在是明眼人，有{self.chip}筹码，可以 '
                                      f'1.跟牌 （{self.field_chip}筹码）2.加倍（{self.field_chip*2}筹码） 3.扔牌 '
                                      f'4.开某位玩家（{self.field_chip*2}筹码） ')
                self.takeAction(player_choice, player_l)
        self.round_num += 1


class AIPlayer(Player):
    def __init__(self, player_no=0, init_chip=500):
        super().__init__(player_no, init_chip)
        self.bravery_value = random.uniform(0.85, 1.15)
        self.honesty_value = random.uniform(0.85, 1.15)
        self.strategy_value = 0

    def judgeStrategy(self):
        self.strategy_value = self.hand_card.total_score * self.bravery_value + (self.chip-500) * 0.02 - self.field_chip

    def openEyes(self):
        roll = random.random()
        self.isBlind = 0
        print(self.player_name, '看牌', end=' ')
        self.judgeStrategy()
        if self.strategy_value < 50:
            self.throwCard()
        else:
            if roll < 0.8:
                self.putChip()
            else:
                self.doubleChip()

    def openSomebody(self, player_l):
        self.player_choice = random.choice(player_l)
        while self.player_choice.player_no == self.player_no or player_l[self.player_choice.player_no].isOut == 1:
            self.player_choice = random.choice(player_l)
        if self.isBlind == 1:
            self.chip -= self.field_chip
            self.chip_on += self.field_chip
        else:
            self.chip -= self.field_chip * 2
            self.chip_on += self.field_chip * 2
        print(self.player_name, '开玩家', self.player_choice.player_name)
        self.action_coin = 3

    def takeStrategy(self, player_l):
        roll1 = random.random()
        if self.round_num == 1:
            if roll1 > 0.5:
                self.openEyes()
            else:
                self.putChip()
        elif self.round_num == 2:
            if self.isBlind == 1:
                if roll1 > 0.2:
                    self.openEyes()
                else:
                    self.openSomebody(player_l)
            else:
                if roll1 > 0.5:
                    self.putChip()
                else:
                    self.openSomebody(player_l)
        elif self.round_num == 3:
            if self.isBlind == 1:
                self.openEyes()
            else:
                self.openSomebody(player_l)
        else:
            self.openSomebody(player_l)

    def ActionList(self, player_l):
        time.sleep(1)
        self.takeStrategy(player_l)
        self.round_num += 1
        time.sleep(1)



