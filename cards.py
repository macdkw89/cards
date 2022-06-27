import csv
import random
import os
os.chdir('BC/python_practice')

# function to conver suit from text to unicode symbol
def suit_change():
    if your_card['suit'] == 'Club':
        print(f"{p} drew {your_card['value']}\u2663")
    elif your_card['suit'] == 'Spade':
        print(f"{p} drew {your_card['value']}\u2660")
    elif your_card['suit'] == 'Diamond':
        print(f"{p} drew {your_card['value']}\u2666")
    elif your_card['suit'] == 'Heart':
        print(f"{p} drew {your_card['value']}\u2665")


# initialize and populate full_deck
with open('resources/cards.csv', newline='') as cards:
    full_deck = []
    GAME = csv.DictReader(cards, delimiter=',')
    for row in GAME:
        full_deck.append(dict(row))

# set initial variables to default values
spent = []
cards_left = 52
your_card = {}
count = 0
index = random.randint(0, (cards_left) - 1)
deck = full_deck
play = input('play? (y/n)')
number_of_players = input('How many players?')
players = []
player_spent = []
for num in range(0, int(number_of_players)):
    players.append(f'Player {num + 1}')
    player_spent.append(f'Deck {num + 1}')
print(player_spent)
print(players)

########### THE GAME ##############
while play == 'y':
    if cards_left >= 1:
        for p in players:
            # get random number between 0 and cards left
            index = random.randint(0, int(cards_left) - 1)
            your_card = deck[index]
            if your_card['suit'] == 'Club':
                print(f"{p} drew {your_card['value']}\u2663")
            elif your_card['suit'] == 'Spade':
                print(f"{p} drew {your_card['value']}\u2660")
            elif your_card['suit'] == 'Diamond':
                print(f"{p} drew {your_card['value']}\u2666")
            elif your_card['suit'] == 'Heart':
                print(f"{p} drew {your_card['value']}\u2665")
            deck.remove(your_card)
            
            spent.append(your_card)
            cards_left = len(deck)
            
            # card counter
            if (your_card['value'] >= '2') & (your_card['value'] <= '6'):
                count = count + 1
            if (your_card['face'] == 'TRUE'):
                count = count - 1
            print(f"{cards_left} left in the deck... The count is {count}")
    else:
            play = 'GAEM OEVR'
            print('out of cardsxx')
    """"
        for row in spent:
            row['suit'] = row['suit']
            print(row)
        """
    #play = input('again?')
