import random

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    sum_of_cards = sum(cards)
    if sum_of_cards == 21:
        return 0
    elif sum_of_cards > 21:
        for i in cards:
            if i == 11:
                cards.remove(11)
                cards.append(1)    
        return sum(cards)
    else:
        return sum(cards)



user_cards = []
computer_cards = []

for i in range(0,2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
print(user_cards, computer_cards)


print(calculate_score(user_cards))
print(calculate_score(computer_cards))