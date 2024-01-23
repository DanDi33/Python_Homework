# Первый из них указывает на номинал карты (от 2 до 9, T (десятка), J, Q, K или A), а второй – на масть (s = пики (
# spades), h = червы (hearts), d = бубны (diamonds) и c = трефы (clubs))
import random


def create_deck():
    nominal = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    card_suit = ["s", "h", "d", "c"]
    deck_of_cards = []
    for i in range(len(nominal)):
        for j in range(len(card_suit)):
            deck_of_cards.append(nominal[i] + card_suit[j])
    return deck_of_cards


def shuffle(arr):
    new_arr = []
    rand_index_set = set()
    while len(rand_index_set) != 52:
        rand_index_set.add(str(random.randint(0, 51)))
    for el in rand_index_set:
        new_arr.append(arr[int(el)])
    return new_arr


def deal(quantity_players, quantity_cards, arr_cards):
    game = []
    for i in range(quantity_players):
        game.append([])
    index = 0
    for i in range(quantity_cards):
        for j in range(quantity_players):
            if index < 52:
                game[j].append(arr_cards[index])
            index += 1
    return game, arr_cards[quantity_players * quantity_cards:]


if __name__ == '__main__':
    print(f"Колода карт: {create_deck()}")
    shuffled_cards = shuffle(create_deck())
    print(f"Переменная колода карт: {shuffled_cards}")
    print(f"Раздача: {deal(5, 4, shuffled_cards)[0]}")
    print(f"Оставшиеся в колоде карты: {deal(5, 4, shuffled_cards)[1]}")


