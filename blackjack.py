import random

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    # cards = [2,2,2,2,2,2,2,2,2]
    
    card = random.choice(cards)
    return card

def calculate_score(cards):
    sum_of_cards = sum(cards)
    if sum_of_cards == 21 and len(cards)== 2:
        return 0
    if  11 in cards and sum_of_cards > 21:
        cards.remove(11)
        cards.append(1)    
        return sum(cards)
    return sum(cards)

def compare(score_1, score_2):
    if score_1 == score_2:
        print("match draw")
    elif score_1 == 0 :
        print("user Wins")
    elif score_2 == 0:
        print("Computer Wins")
    elif score_1 > 21:
        print("User lost")
    elif score_2 > 21 :
        print("computer lost")
    elif score_1 > score_2:
        print("user Wins")
    else:
        print("computer wins")


user_cards = []
computer_cards = []
is_game_over = False

for i in range(0,2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())



while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"U:- {user_cards} Current user score:- {user_score}, \nC:- {computer_cards[0]}")

    if user_score == 0 or computer_cards == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if user_should_deal == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

