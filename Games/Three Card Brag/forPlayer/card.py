"""
File: pai.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-06-09 20:32:28
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
        self.three_cards = three_cards
        self.three_cards_point = [three_cards[0].point, three_cards[1].point, three_cards[2].point]
        self.three_cards_point.sort(reverse=True)
        self.kind = ''
        self.total_score = 0
        self.compare_card = [0, 0, 0]
        self.judgeSize()
        self.judgeScore()

    def judgeFlush(self):
        if max(self.three_cards_point) - min(self.three_cards_point) == 2 and len((set(self.three_cards_point))) == \
                len(self.three_cards_point):
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

            if self.judgeFlush():
                self.kind += '顺'
                self.score = 4

        elif self.judgeFlush():
            self.kind += '顺子'
            self.score = 2

        elif len((set(self.three_cards_point))) != len(self.three_cards_point):
            self.kind += '对子'
            self.score = 1

        else:
            self.kind += '单只'
            self.score = 0

    def judgeScore(self):
        if self.judgeFlush() == 3:
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
        self.total_score = self.score*80 + 4*self.compare_card[0] + 2*self.compare_card[1] + 0.5*self.compare_card[2]

    def __str__(self):
        return f'{self.three_cards[0]} {self.three_cards[1]} {self.three_cards[2]},是一幅{self.kind}牌'


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
    return 1


def test_score():
    test_hand_card = []
    average_score = 0
    pai = CreateAPoker()
    PLAYER_NUMBER = 8
    for i in range(PLAYER_NUMBER):
        test_card = [pai[i], pai[i+PLAYER_NUMBER], pai[i+2*PLAYER_NUMBER]]
        test_hand_card.append(HandCard(test_card))
    for hand_card in test_hand_card:
        print(hand_card)
        average_score += hand_card.total_score
    print(average_score/PLAYER_NUMBER)
    return average_score/PLAYER_NUMBER


def main():
    fangcha = 0
    test_score_list = []
    TEST_NUM = 10000
    for i in range(TEST_NUM):
        test_scores = test_score()
        test_score_list.append(test_scores)
    average_score = sum(test_score_list)/TEST_NUM
    for i in test_score_list:
        fangcha += (i-average_score)*(i-average_score)
    print(average_score)
    print(fangcha/TEST_NUM)


if __name__ == '__main__':
    main()

