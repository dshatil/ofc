# Author: Dan Shatil
# Date: 8/10/21
# Description: Implementation of Open-Face Chinese Poker

import random

class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __str__(self):
        return ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")[self.rank-2] + str(self.suit)

    def __gt__(self, other):
        return self.rank > other.rank
    
    def __ge__(self, other):
        return self.rank >= other.rank
    
    def __lt__(self, other):
        return self.rank < other.rank
    
    def __le__(self, other):
        return self.rank <= other.rank

class OFCPlayer:

    def __init__(self, stack=0):

        self.stack = stack
        self.bottom = PokerHand()
        self.middle = PokerHand()
        self.top = PokerHand()
        self.fantasy = False

    def clear(self):
        self.bottom = PokerHand()
        self.middle = PokerHand()
        self.top = PokerHand()

    def count(self):
        return len(self.bottom) + len(self.middle) + len(self.top)

class Deck:

    def __init__(self):
        self._cards = []
        for rank in (i for i in range(2,15)):
            for suit in ('h', 'd', 'c', 's'):
                self._cards.append(Card(rank, suit))

    def get_deck(self):
        return self._cards

    def get_size(self):
        return len(self._cards)

    def deal_card(self):
        return self._cards.pop()

    def shuffle(self):
        random.shuffle(self._cards)

class PokerHand:

    def __init__(self, cards=None):
        if cards is None:
            cards = []
        self._cards = cards

        self._rankings = {'Royal Flush': 0, 'Straight Flush': 1, 'Quads': 2, 'Full House': 3,
                              'Flush': 4, 'Straight': 5, 'Set': 6, 'Two Pair': 7, 'Pair': 8, 'High Card': 9}

    def __eq__(self, other):
        return self.get_ranks() == other.get_ranks() and self.get_type() == other.get_type()

    def __str__(self):
        return str([str(self._cards[i]) for i in range(len(self._cards))])

    def __iter__(self):
        return iter(self._cards)

    def __len__(self):
        return len(self._cards)

    def head_to_head(self, other):
        if self.get_ranking() < other.get_ranking():
            return 1
        elif self.get_ranking() > other.get_ranking():
            return -1
        else:
            s_ranks = self.get_ranks()
            o_ranks = other.get_ranks()
            if s_ranks > o_ranks:
                return 1
            elif o_ranks > s_ranks:
                return -1
            return 0

    def sorted(self, do_reverse=True):
        self._cards.sort(reverse=do_reverse)
        return self

    def get_cards(self):
        return self._cards

    def add_card(self, card):
        self._cards.append(card)

    def get_ranking(self):
        return self._rankings[self.get_type()]

    def get_ranks(self):
        return sorted([card.rank for card in self._cards], reverse=True)

    def sort_ranks(self):
        ranks = self.get_ranks()

    def get_suits(self):
        return [card.suit for card in self._cards]

    def get_size(self):
        return len(self._cards)

    def is_flush(self):
        return len(self._cards) == 5 and len(set(self.get_suits())) == 1

    def is_straight(self):
        ranks = self.get_ranks()
        if len(ranks) != 5 or len(ranks) != len(set(ranks)):
            return False
        return ranks[0] == ranks[-1] + 4 or (ranks[0] == 14 and ranks[1] == 5)

    def is_quads(self):
        ranks = self.get_ranks()
        for rank in ranks:
            if ranks.count(rank) == 4:
                return True
        return False

    def is_boat(self):
        ranks = self.get_ranks()
        return len(ranks) == 5 and len(set(ranks)) == 2 and not self.is_quads()

    def is_trips(self):
        if self.is_boat():
            return False
        ranks = self.get_ranks()
        for rank in ranks:
            if ranks.count(rank) == 3:
                return True
        return False

    def is_two_pair(self):
        ranks = self.get_ranks()
        return len(ranks) == 5 and len(set(ranks)) == 3 and not self.is_trips()

    def is_pair(self):
        ranks = self.get_ranks()
        return len(set(ranks)) == len(ranks) - 1

    def is_high_card(self):
        ranks = self.get_ranks()
        return len(ranks) == len(set(ranks)) and not self.is_flush() and not self.is_straight()

    def get_single(self):
        ranks = self.get_ranks()
        for rank in ranks:
            if ranks.count(rank) > 1:
                return rank

    def compare_paired_hand(self, other, get_func):
        if get_func(self) > get_func(other):
            return 1
        elif get_func(self) < get_func(other):
            return -1
        if self.get_ranks() > other.get_ranks():
            return 1
        elif self.get_ranks() < other.get_ranks():
            return -1
        return 0


    def get_two_pair(self):
        ranks = self.get_ranks()
        result1 = 0
        result2 = 0
        for rank in ranks:
            if ranks.count(rank) == 2 and not result1:
                result1 = rank
            elif ranks.count(rank) == 2 and not result2:
                result2 = rank
        return (result1, result2)

    def get_full_house(self):
        ranks = self.get_ranks()
        (result1, result2) = (0,0)
        for rank in ranks:
            if ranks.count(rank) == 3:
                result1 = rank
            if ranks.count(rank) == 2:
                result2 = rank
        return (result1, result2)

    def get_type(self):
        if self.is_high_card():
            return 'High Card'
        elif self.is_pair():
            return 'Pair'
        elif self.is_two_pair():
            return 'Two Pair'
        elif self.is_trips():
            return 'Set'
        elif self.is_straight() and not self.is_flush():
            return 'Straight'
        elif self.is_flush and not self.is_straight():
            return 'Flush'
        elif self.is_boat():
            return 'Full House'
        elif self.is_quads():
            return 'Quads'
        elif self.is_straight and self.is_flush():
            ranks = self.get_ranks()
            if ranks[-1] == 14:
                return 'Royal Flush'
            else:
                return 'Straight Flush'
        return None

    def compare_to(self, other):

        self_rank = self.get_ranking()
        other_rank = other.get_ranking()
        if self_rank < other_rank:
            return 1
        elif self_rank > other_rank:
            return -1
        elif self_rank == 8 or self_rank == 6 or self_rank == 2:
            return self.compare_paired_hand(other, PokerHand.get_single)
        elif self_rank == 7:
            return self.compare_paired_hand(other, PokerHand.get_two_pair)
        elif self_rank == 3:
            return self.compare_paired_hand(other, PokerHand.get_full_house)
        elif self.get_ranks() > other.get_ranks():
            return 1
        elif self.get_ranks() < other.get_ranks():
            return -1
        return 0


class OFCGame:

    def __init__(self, players=2):

        self._pl = {i : OFCPlayer() for i in range(1, players+1)}
        self._fantasy = {i : False for i in range(1, players+1)}
        self._deck = Deck()
        self._deck.shuffle()

    def add_card_to_hand(self, player, new_card, hand):
        """
        Takes an integer for player, Card object, and string indicating bottom, middle, or top
        """
        if hand == 'b':
            self._pl[player].bottom.add_card(new_card)
        if hand == 'm':
            self._pl[player].middle.add_card(new_card)
        if hand == 't':
            self._pl[player].top.add_card(new_card)

    def foul(self, player):
        return self._pl[player].top.compare_to(self._pl[player].middle) == 1 or \
               self._pl[player].middle.compare_to(self._pl[player].bottom) == 1

    def get_hand_bonus(self, ofc_player, location):
        if location == 'b':
            return (25, 15, 10, 6, 4, 2, 0, 0, 0, 0)[ofc_player.bottom.get_ranking()]
        if location == 'm':
            return (50, 30, 20, 12, 8, 4, 2, 0, 0, 0)[ofc_player.middle.get_ranking()]
        if location == 't' and ofc_player.top.get_type() == 'Pair':
            return max(ofc_player.top.get_single() - 5, 0)
        elif location == 't' and ofc_player.top.get_type() == 'Set':
            return ofc_player.top.get_single() + 8
        else:
            return 0

    def show_hand(self, player):
        print("Player " + str(player) + ": " + ("Not Foul", "Foul")[self.foul(player)])
        print(str(self._pl[player].top.sorted()) + ": " + str(self._pl[player].top.get_type()))
        print(str(self._pl[player].middle.sorted()) + ": " + str(self._pl[player].middle.get_type()))
        print(str(self._pl[player].bottom.sorted()) + ": " + str(self._pl[player].bottom.get_type()))


    def head_to_head(self, player1, player2):
        total = 0
        total += player1.bottom.compare_to(player2.bottom)
        total += player1.middle.compare_to(player2.middle)
        total += player1.top.compare_to(player2.top)
        if abs(total) == 3:
            total *= 2
        for loc in ('b', 'm', 't'):
            total += self.get_hand_bonus(player1, loc) - self.get_hand_bonus(player2, loc)
        return total

    def settle(self, p1, p2):
        player1 = (self._pl[p1], OFCPlayer())[self.foul(p1)]
        player2 = (self._pl[p2], OFCPlayer())[self.foul(p2)]
        total = self.head_to_head(player1, player2)
        self._pl[p1].stack += total
        self._pl[p2].stack -= total

    def end_round(self):
        self._deck = Deck()
        self._deck.shuffle()
        for player in self._pl:
            self._pl[player].clear()

    def new_round(self, dealer):
        players = [(dealer + i) % len(self._pl) for i in range(len(self._pl))]
        players = [len(self._pl) if num == 0 else num for num in players]
        for player in players:
            start_hand = PokerHand([self._deck.deal_card() for i in range(5)]).sorted()
            print(start_hand)
            for card in start_hand:
                hand = input("Player " + str(player) + ", " + str(card) + ": ")
                self.add_card_to_hand(player, card, hand)
        for turn in range(8):
            for player in players:
                for p in players:
                    self.show_hand(p)
                deal_card = self._deck.deal_card()
                print("turn = " + str(turn+1) + ", players: " + str(players))
                hand = input("Player " + str(player) + ", " + str(deal_card) + ": ")
                self.add_card_to_hand(player, deal_card, hand)
        self.settle(players[0], players[1])
        for p in players:
            self.show_hand(p)
            print("Player " + str(p) + " new total: " + str(self._pl[p].stack))




def main():

    p = OFCGame()
    print(p._pl[1].top)
    p._pl[1].top.add_card(Card(4, 'c'))
    p._pl[1].top.add_card(Card(5, 'c'))

    p._pl[1].top.add_card(Card(7, 'c'))
    print(p._pl[1].top)
    print(p._pl[1].top.get_type())
    for i in range(5):
        p._pl[1].bottom.add_card(p._deck.deal_card())
    print(p._pl[1].bottom)
    print(p._pl[1].bottom.get_type())
    p._pl[2].top.add_card(Card(4,'s'))
    p._pl[2].top.add_card(Card(2, 's'))
    p._pl[2].top.add_card(Card(7, 's'))
    print(p._pl[2].top.compare_to(p._pl[1].top))
    p.end_round()
    p.new_round(1)


if __name__ == '__main__':
    main()
