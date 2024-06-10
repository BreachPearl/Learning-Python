import random
card_list=[11,2,3,4,5,6,7,8,9,10,10,10,10]
player_card_list=[]
dealer_card_list=[]
player_score=0
dealer_score=0
def pick_another_card_player():
    global player_score
    player_card_list.append(random.choice(card_list))
    adjust_ace(player_card_list)
    player_score = sum(player_card_list)
    print(f"Your cards: {player_card_list}, current score: {player_score}")
    print(f"Dealer's first card: {dealer_card_list[0]}")
def pick_another_card_dealer():
    global dealer_score
    dealer_card_list.append(random.choice(card_list))
    adjust_ace(dealer_card_list)
    dealer_score = sum(dealer_card_list)
def adjust_ace(card_list):
    while sum(card_list) > 21 and 11 in card_list:
        ace_index = card_list.index(11)
        card_list[ace_index] = 1
def win_check():
    global player_score
    global dealer_score
    
    if player_score == 21:
        print(f"Your cards: {player_card_list}, current score: {player_score}")
        print(f"Dealer's hand: {dealer_card_list}, dealer score: {dealer_score}")
        print("You win, you lucky little bastard")
    elif player_score > 21:
        
        print(f"Your cards: {player_card_list}, current score: {player_score}")
        print(f"Dealer's hand: {dealer_card_list}, dealer score: {dealer_score}")
        print("Dealer wins, It's a BUST you little loser!")
    elif dealer_score > 21:
        print(f"Your cards: {player_card_list}, current score: {player_score}")
        print(f"Dealer's hand: {dealer_card_list}, dealer score: {dealer_score}")
        print("You win, dealer busts!")
    elif player_score > dealer_score:
        print(f"Your cards: {player_card_list}, current score: {player_score}")
        print(f"Dealer's hand: {dealer_card_list}, dealer score: {dealer_score}")
        print("You win, you little bastard")
    elif player_score < dealer_score:
        print(f"Your cards: {player_card_list}, current score: {player_score}")
        print(f"Dealer's hand: {dealer_card_list}, dealer score: {dealer_score}")
        print("Dealer wins, you are a loser!")
    else:
        print(f"Your cards: {player_card_list}, current score: {player_score}")
        print(f"Dealer's hand: {dealer_card_list}, dealer score: {dealer_score}")
        print("Draw, hahaha")
want_to_play = input("Do you want to play blackjack game type 'y' for Yes and 'n' for No: ")
if want_to_play=="y":
    print(r'''
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
          |  \/ K|                            _/ |                
          `------'                           |__/           
    ''')
    for i in range(2):
        player_card_list.append(random.choice(card_list))
        adjust_ace(player_card_list)
        player_score=player_score+player_card_list[i]
    for i in range(2):
        dealer_card_list.append(random.choice(card_list))
        adjust_ace(dealer_card_list)
        dealer_score=dealer_score+dealer_card_list[i]
    print(f"your cards: {player_card_list}, current score: {player_score}")
    print(f"dealer's first Card: {dealer_card_list[0]}")
    while player_score < 21:
        wanna_pick_another_card = input('Type "y" to get another card, "n" to pass: ').lower()
        if wanna_pick_another_card == "y":
            pick_another_card_player()
        elif wanna_pick_another_card == "n":
            while dealer_score < 17:
                pick_another_card_dealer()
            break

    win_check()
else:
    print("Maybe next time!")