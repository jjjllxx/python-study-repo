"""
File: pai0.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-06-15 10:45:06
Function:


"""
import random


class Poker(object):
    def __init__(self, suit, point):
        self.suit = suit
        self.point = point
        self.point_show = ''
        self.judgeSuit()

    def judgeSuit(self):
        if self.point == 14:
            self.point_show += 'A'
        elif self.point == 13:
            self.point_show += 'K'
        elif self.point == 12:
            self.point_show += 'Q'
        elif self.point == 11:
            self.point_show += 'J'
        else:
            self.point_show += str(self.point)

    def __str__(self):
        return self.suit + self.point_show


def CreateAPoker():
    all_suit = ['红桃', '方片', '黑桃', '梅花']
    all_poker = []
    for i in range(2, 15):
        for j in all_suit:
            all_poker.append(Poker(j, i))
    random.shuffle(all_poker)
    return all_poker


class HandCard(object):
    def __init__(self, three_cards):
        self.score = 0
        self.kind = ''
        self.three_cards = three_cards
        self.three_cards_point = [three_cards[0].point, three_cards[1].point, three_cards[2].point]
        self.three_cards_point.sort(reverse=True)
        self.total_score = 0
        self.compare_card = [0, 0, 0]
        self.judgeSize()
        self.judgeScore()

    def judgeFlash(self):
        if max(self.three_cards_point) - min(self.three_cards_point) == 2 and len((set(self.three_cards_point))) \
                == len(self.three_cards_point):
            return max(self.three_cards_point)
        elif 2 in self.three_cards_point and 3 in self.three_cards_point and 14 in self.three_cards_point:
            return 3
        else:
            return 0

    def judgeSize(self):
        if self.three_cards_point[0] == self.three_cards_point[2]:
            self.kind += '豹子'
            self.score = 5

        elif self.three_cards[0].suit == self.three_cards[1].suit == self.three_cards[2].suit:
            self.kind += '同花'
            self.score = 3

            if self.judgeFlash():
                self.kind += '顺'
                self.score = 4

        elif self.judgeFlash():
            self.kind += '顺子'
            self.score = 2

        elif len((set(self.three_cards_point))) != len(self.three_cards_point):
            self.kind += '对子'
            self.score = 1

        else:
            self.kind += '单只'
            self.score = 0

    def judgeScore(self):
        if self.judgeFlash() == 3:
            self.compare_card[0] = 3
            self.compare_card[1] = 2
            self.compare_card[2] = 1
        elif self.score == 1 and self.three_cards_point[0] != self.three_cards_point[1]:
            self.compare_card[0] = self.three_cards_point[1]
            self.compare_card[1] = self.three_cards_point[2]
            self.compare_card[2] = self.three_cards_point[0]
        else:
            self.compare_card[0] = self.three_cards_point[0]
            self.compare_card[1] = self.three_cards_point[1]
            self.compare_card[2] = self.three_cards_point[2]
        self.total_score = self.score*167 + 12.5*self.compare_card[0] + self.compare_card[1] + 0.5*self.compare_card[2]

    def __str__(self):
        return f'{self.three_cards[0]} {self.three_cards[1]} {self.three_cards[2]},是一幅{self.kind}牌，' \
               f'总计{self.total_score}分'


def compareHandCard(hand_card_one, hand_card_two):
    if hand_card_one.score > hand_card_two.score:
        return 1
    elif hand_card_two.score > hand_card_one.score:
        return 0
    else:
        for i in range(3):
            if hand_card_one.compare_card[i] > hand_card_two.compare_card[i]:
                return 1
            elif hand_card_one.compare_card[i] < hand_card_two.compare_card[i]:
                return 0
            else:
                continue
    return 0


def StandardDeviation(score_list):
    score_variance = 0
    average = sum(score_list)/len(score_list)
    for score in score_list:
        score_variance += (score-average)**2
    return (score_variance / len(score_list))**0.5


def game_score(player_num, game_num):
    average_list = []
    max_average_list = []
    min_average_list = []
    med_average_list = []
    game_score_list = []
    standard_deviation_list = []
    for game in range(game_num):
        pai = CreateAPoker()
        score_list = []
        for player in range(player_num):
            hand_card_list = [pai[player], pai[player + player_num], pai[player + 2 * player_num]]
            hand_card = HandCard(hand_card_list)
            score_list.append(hand_card.total_score)
        game_score_list.append(score_list)
    for list0 in game_score_list:
        average_list.append(sum(list0)/len(list0))
        max_average_list.append(max(list0))
        min_average_list.append(min(list0))
        standard_deviation_list.append(StandardDeviation(list0))
        list0.sort()
        if len(list0) % 2 == 0:
            med_average_list.append((list0[int(len(list0)/2-1)]+list0[int(len(list0)/2)])/2)
        else:
            med_average_list.append(list0[int((len(list0)-1)/2)])
    print(f'{player_num}人游戏时,模拟{game_num}局的结果')
    print('每局游戏手牌均值', sum(average_list)/len(average_list), '对应标准差', StandardDeviation(average_list))
    print('每局游戏最大手牌均值', sum(max_average_list)/len(max_average_list), '对应标准差', StandardDeviation(max_average_list))
    print('每局游戏最小手牌均值', sum(min_average_list)/len(min_average_list), '对应标准差', StandardDeviation(min_average_list))
    print('每局游戏中位数手牌均值', sum(med_average_list) / len(med_average_list), '对应标准差', StandardDeviation(med_average_list))
    print('每局游戏手牌标准差均值', sum(standard_deviation_list) / len(med_average_list), '对应标准差', StandardDeviation(standard_deviation_list))


def main():
    GAME_NUM = 100000
    for PLAYER_NUM in range(1, 18):
        game_score(PLAYER_NUM, GAME_NUM)


if __name__ == '__main__':
    main()
