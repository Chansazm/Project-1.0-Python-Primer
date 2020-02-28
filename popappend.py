card_deck = [2,4,6,7,8,9,5,1,3]
hand = []

while sum(hand) <= 17:
    hand.append(card_deck.pop())
print(hand)
