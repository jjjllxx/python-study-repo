"""
File: liucheng0.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-06-15 10:46:31
Function:


"""
from card0 import *
from player0 import *
import random


class GameProcess:
    def __init__(self, player_list):
        self.player_list = player_list
        self.player_num = len(player_list)
        self.player_exist = len(player_list)
        self.base_chip = 20
        self.field_chip = 0
        self.round_num = 1
        self.banker_no = 0
        self.all_poker = []
        self.action_time = 0

    def initialGame(self):
        # 洗牌
        all_suit = ['红桃', '方片', '黑桃', '梅花']
        for i in range(2, 15):
            for j in all_suit:
                self.all_poker.append(Poker(j, i))
        random.shuffle(self.all_poker)
        # 判断庄家
        for player in self.player_list:
            if player.isBanker == 1:
                self.banker_no = player.player_no
        # 从庄家开始发牌
        j = 0
        for i in range(self.banker_no, self.banker_no+self.player_num):
            k = i % self.player_num
            hand_card_input = HandCard([self.all_poker[j], self.all_poker[j + self.player_num],
                                        self.all_poker[j + 2*self.player_num]])
            self.player_list[k].deliverCard(hand_card_input)
            j += 1
        # 下底注
        for player in self.player_list:
            player.chip_on += 10
            player.chip -= 10
            self.field_chip += 10

    def judgeAction(self, player):
        if player.action_coin == 0:
            self.player_exist -= 1

        elif player.action_coin == 1:
            pass

        elif player.action_coin == 2:
            self.base_chip = self.base_chip*2
            for player0 in self.player_list:
                player0.field_chip = self.base_chip

        elif player.action_coin == 3:
            result = compareHandCard(player.hand_card, self.player_list[player.player_choice.player_no].hand_card)
            if result == 1:
                print(player.player_name, '获胜', end=' ')
                self.player_list[player.player_choice.player_no].throwCard()
                player.chip += self.player_list[player.player_choice.player_no].chip_on
                self.field_chip -= self.player_list[player.player_choice.player_no].chip_on
                self.player_list[player.player_choice.player_no].chip_on = 0
                self.player_exist -= 1
            else:
                print(player.player_name, '失败', end=' ')
                player.throwCard()
                self.player_exist -= 1
        self.field_chip += player.chip_on

    def judgeGameEnd(self):
        if self.player_exist == 1:
            for player in self.player_list:
                if player.isOut == 0:
                    player.chip += self.field_chip
                    player.isBanker = 1
                    player.win_game += 1
                    print('')
                    print(f'本局游戏结束,{player.player_name}获胜')
                else:
                    player.isBanker = 0

    def oneGame(self):
        self.initialGame()
        j = self.banker_no
        while self.player_exist != 1:
            i = j % self.player_num
            if self.player_list[i].isOut == 0 and self.player_exist != 1:
                self.field_chip -= self.player_list[i].chip_on
                self.action_time += 1
                self.player_list[i].takeAction(self.player_list)
                self.judgeAction(self.player_list[i])
                self.judgeGameEnd()
            self.round_num += 1
            j += 1
        self.EndSituation()

    def EndSituation(self):
        for player in self.player_list:
            print(player.player_name, end='手牌为')
            print(player.hand_card, end='，还剩')
            print(player.chip, '筹码')
        print(f'人均行动{self.action_time/self.player_num}次')
        print('')

        for player in self.player_list:
            player.isOut = 0
            player.isBlind = 1
            player.round_num = 1
            player.chip_on = 0
            player.field_chip = 20


def createPlayer():
    player_list = []
    player_num = int(input('请输入游戏玩家数：'))
    for num in range(player_num):
        player0 = AIPlayer(player_no=num)
        player_list.append(player0)
    return player_list


def totalGame(player_list):
    game_list = []
    game_num = int(input('请输入比赛局数：'))
    for i in range(game_num):
        game_list.append(GameProcess(player_list))
    return game_list


def finalRank(player_list, game_list):
    print(f'{len(game_list)}局游戏结束，最终排名：')
    player_chip = []
    player_by_chip = []
    player_score = []
    action_time = 0
    for player in player_list:
        player_chip.append(player.chip)
    player_chip.sort(reverse=True)
    for i in range(len(player_chip)):
        for player in player_list:
            if player.chip == player_chip[i] and player not in player_by_chip:
                player_by_chip.append(player)
                break
    i = 1
    for player in player_by_chip:
        print(f'第{i}名,', player, f'手牌均分为{sum(player.hand_card_list)/len(player.hand_card_list)},'
                                 f'手牌标准差为{StandardDeviation(player.hand_card_list)}')
        i += 1
    for player in player_list:
        player_score.append(sum(player.hand_card_list)/len(game_list))
    print(f'手牌均值极差{max(player_score)-min(player_score)},手牌离散程度（标准差）{StandardDeviation(player_score)}')
    # for game in game_list:
    #     action_time += game.action_time
    # print(f'局均人均行动次数为{action_time/len(player_list)/len(game_list)}')


def main():
    i = 1
    test_player_list = createPlayer()
    test_game_list = totalGame(test_player_list)
    print('')
    for test_game in test_game_list:
        print(f'第{i}局游戏开始')
        test_game.oneGame()
        print(f'还剩{len(test_game_list)-i}局游戏')
        i += 1
    finalRank(test_player_list, test_game_list)
    input()


if __name__ == '__main__':
    main()
