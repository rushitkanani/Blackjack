import random

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    # cards = [2,2,2,2,2,2,2,2,2]
    
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
a = 0
while a < 10:
    user_cards = []
    computer_cards = []
    print("--------------NEW GAME--------------------------")
    for i in range(0,2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    print(f"U:- {user_cards}, C:- {computer_cards}")


    if calculate_score(computer_cards)== 21:
        print("Computer Wins")
    elif calculate_score(user_cards) == 21:
        print("User Wins")

    ask_user = input("want to draw another card ? ").lower()
    if ask_user == "yes":
        user_cards.append(deal_card())
        
        calculate_score(user_cards)
        if calculate_score(computer_cards) < 17:
            computer_cards.append(deal_card())
    print(f"user_cards- {user_cards}")
    print(f"pc_cards- {computer_cards}")
    print(f"pc_score- {calculate_score(computer_cards)}")
    print(f"user_score-{calculate_score(user_cards)}")

    compare(calculate_score(user_cards),calculate_score(computer_cards))
    print("--------------GAME  OVER--------------------------")
    a+=1
