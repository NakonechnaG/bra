#!/usr/bin/env python3.7

import random
from operator import attrgetter

PLAYERS_COUNT = 6
DECK_SIZE = 36
CARDS_TO_RECEIVES = 18
RANKS = ['6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
SUITS = ['♠', '♥', '♦', '♣']


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def __repr__(self):
        cards_str = ','.join(str(card) for card in self.cards)
        return self.name


class Card:
    def __init__(self, rank, suit, power):
        self.rank = rank
        self.suit = suit
        self.power = power

    def __eq__(self, other):
        return self.power == other.power
    def __ne__(self, other):
        return not self.__eq__(other)
    def __gt__(self, other):
        return self.power > other.power
    def __lt__(self, other):
        return self.power < other.power
    def __ge__(self, other):
        return self.power >= other.power
    def __le__(self, other):
        return self.power <= other.power

    def __hash__(self):
        return hash(f'{self.rank}:{self.suit}')

    def __repr__(self):
        return f'{self.rank}{self.suit}'


class Game:
    def __init__(self, players, deck):
        self.players = players
        self.deck = deck
        self.winner = None

    @staticmethod
    def _get_round_cards(players):
        cards_players_map = {}

        for player in players:

            # many rounds, cards has ended
            if not player.cards:
                continue

            card = player.cards.pop(0)
            cards_players_map[card] = player

        return cards_players_map

    def _shake_deck(self):
        random.shuffle(self.deck)

    def _receives_cards(self):
        while len(self.deck):
            for player in self.players:
                player.cards.append(self.deck.pop())

    def _play_round(self, players):
        cards_players_map = self._get_round_cards(players)

        cards_on_table = list(cards_players_map.keys())

        table_cards_sorted = sorted(
            cards_on_table,
            key=attrgetter('power'),
            reverse=True,
        )

        if not table_cards_sorted:
            return None

        win_card = table_cards_sorted[0]
        winner_cards = [card for card in table_cards_sorted if card == win_card]

        if len(winner_cards) == 1:
            round_winner = cards_players_map[win_card]

            # shuffle cards to avoid infinite loop
            random.shuffle(cards_on_table)

        else:
            # play more ext rounds
            round_winners = [cards_players_map[card] for card in winner_cards]
            round_winner = self._play_round(round_winners)

        # winner gets the cards from the table
        if round_winner:
            round_winner.cards = round_winner.cards + cards_on_table
        return round_winner

    def _show_state(self):
        print('Game state:')
        for player in self.players:
            print('  Player: {name}: {cards}'.format(
                name=player.name,
                cards=", ".join(str(card) for card in player.cards),
            ))
        print('-' * 80)

    def play(self):
        self.winner = None

        self._shake_deck()
        self._receives_cards()

        print('New game')
        self._show_state()

        round_num = 0
        while True:
            round_num += 1

            winner = self._play_round(self.players)
            print(f'Round {round_num} win player: {winner}')

            self._remove_losers()

            self._show_state()

            if len(self.players) == 1:
                self.winner = self.players[0].name
                break

    def _remove_losers(self):
        self.players = [player for player in self.players if player.cards]

    def show_winner(self):
        if self.winner:
            print(f'The winner is player: {self.winner}')
        else:
            print('We have draw!')


deck = []
for power, rank in enumerate(RANKS, 1):
    for suit in SUITS:
        card = Card(rank, suit, power)
        deck.append(card)

# shake deck
random.shuffle(deck)

game = Game(
    players=[Player(name=str(i)) for i in range(1, PLAYERS_COUNT + 1)],
    deck=deck[:CARDS_TO_RECEIVES],
)
game.play()
game.show_winner()
