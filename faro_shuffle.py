card_deck = input().split()
number_of_shuffles = int(input())
final_deck = []
for shuffle in range(number_of_shuffles):
    final_deck = []
    middle_of_the_deck = len(card_deck) // 2
    left_half = card_deck[0:middle_of_the_deck]
    right_half = card_deck[middle_of_the_deck::]
    for index_of_the_card in range(len(left_half)):
        final_deck.append(left_half[index_of_the_card])
        final_deck.append(right_half[index_of_the_card])
    card_deck = final_deck
print(card_deck)