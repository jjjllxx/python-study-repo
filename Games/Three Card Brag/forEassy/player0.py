"""
File: wanjia0.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-06-15 10:45:48
Function:


"""
import random


class AIPlayer:
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
        self.player_name = '玩家'+str(self.player_no)
        if player_no == 0:
            self.bravery_value = 0.6
        else:
            self.bravery_value = 1 + 0.05 * self.player_no
        self.blind_tendency = 1
        self.strategy_value = 0
        self.win_game = 0
        self.hand_card_list = []
        self.handcard_distribution = {}

    def deliverCard(self, hand_card):
        self.hand_card = hand_card
        self.hand_card_list.append(self.hand_card.total_score)
        if hand_card.total_score not in self.handcard_distribution.keys():
            self.handcard_distribution[hand_card.total_score] = 1
        else:
            self.handcard_distribution[hand_card.total_score] += 1

    def judgeStrategy(self):
        self.strategy_value = self.hand_card.total_score*self.bravery_value-self.field_chip*2+self.chip_on+self.isBanker*5+self.chip/300

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

    def throwCard(self):
        self.isOut = 1
        self.action_coin = 0
        print(self.player_name, '扔牌')

    def PutorFight(self, player_l):
        roll = random.random()
        if roll*self.bravery_value > self.chip_on/200+0.08*self.round_num:
            self.putChip()
        else:
            self.openSomebody(player_l)

    def normalAction(self, player_l):
        if self.round_num == 1:
            self.putChip()
        else:
            self.PutorFight(player_l)

    def NotBlindAction(self, player_l):
        self.judgeStrategy()
        if self.strategy_value < 160:
            self.throwCard()
            return
        roll0 = random.random()
        if roll0*self.bravery_value*self.strategy_value/500 > 0.4 + self.field_chip/200:
            self.doubleChip()
        else:
            self.normalAction(player_l)

    def BlindAction(self, player_l):
        roll = random.random()
        if (roll-self.isBanker/10)*self.blind_tendency < self.round_num*0.25+self.field_chip/100:
            self.isBlind = 0
            print(self.player_name, '看牌', end=' ')
            self.NotBlindAction(player_l)
        else:
            self.normalAction(player_l)

    def takeAction(self, player_l):
        if self.isBlind == 1:
            self.BlindAction(player_l)
        else:
            self.NotBlindAction(player_l)
        self.round_num += 1

    def __str__(self):
        return f'{self.player_name}最终还剩{self.chip}筹码，勇敢系数为{self.bravery_value},盲人倾向为{self.blind_tendency}' \
               f',总计获胜{self.win_game}次'