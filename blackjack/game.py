import random
import sys

# we assume that there is 1 player
# assume that there are 4 card stacks

cards = {
    'two': { 'value': 2, 'count': 16 },
    'three': { 'value': 3, 'count': 16 },
    'four': { 'value': 4, 'count': 16 },
    'five': { 'value': 5, 'count': 16 },
    'six': { 'value': 6, 'count': 16 },
    'seven': { 'value': 7, 'count': 16 },
    'eight': { 'value': 8, 'count': 16 },
    'nine': { 'value': 9, 'count': 16 },
    'ten': { 'value': 10, 'count': 16 },
    'jack': { 'value': 10, 'count': 16 },
    'queen': { 'value': 10, 'count': 16 },
    'king': { 'value': 10, 'count': 16 },
    'ace': { 'value': 11, 'count': 16 },
}

player = 0
dealer = 0

# giving player initial cards
card_nominal1, card1 = random.choice(list(cards.items()))
card_nominal2, card2 = random.choice(list(cards.items()))
print('Your first card:', card_nominal1)
print('Your second card:', card_nominal2)

player += card1['value']
player += card2['value']
print('Your total:', player)

card1['count'] = card1['count'] - 1
card2['count'] = card2['count'] - 1

# giving dealer initial cards
card_nominal1, card1 = random.choice(list(cards.items()))
card_nominal2, card2 = random.choice(list(cards.items()))
print('Dealer first card:', card_nominal1)
#print('Dealer second card:', card_nominal2)

dealer += card1['value']
print('Dealer total:', dealer)
dealer += card2['value']

card1['count'] = card1['count'] - 1
card2['count'] = card2['count'] - 1

# checking initial game

if dealer == 21 and player == 21:
    print('Tie')
    sys.exit()
if dealer == 21 and player != 21:
    print('Dealer wins')
    sys.exit()

# game loop
while player <= 21:
    if player == 21:
        break

    choice = input('choose h, s: ')
    if choice == 's':
        break

    card_nominal, card = random.choice(list(cards.items()))
    print('You got a:', card_nominal)

    if card_nominal == 'ace':
        if (player + 11) > 21:
            player += 1
        else:
            player += card['value']
    else:
        player += card['value']

    print('Your total:', player)
    card['count'] = card['count'] - 1

    if player >= 21:
        print('You lose, dealer wins')
        sys.exit()

# dealer game
while dealer <= 21:
    if dealer >= 16:
        break

    card_nominal, card = random.choice(list(cards.items()))

    if card_nominal == 'ace':
        if (dealer + 11) > 21:
            dealer += 1
        else:
            dealer += card['value']
    else:
        dealer += card['value']

    card['count'] = card['count'] - 1

    if dealer > 21:
        print('Dealer got {} and lost, you WIN!!!'.format(dealer))
        sys.exit()

print('Your score:', player)
print('Dealer score:', dealer)

if player > dealer:
    print('YOU WIN!')
if player < dealer:
    print('Dealer wins')
else:
    if dealer == 21 and player != 21:
        print('Dealer wins')
    if dealer == player:
        print('Tie!')
