import random

def new_game():
    logo = r"""
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          `------'                           |__/           
    """

    print(logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = random.sample(cards, 2)
    comp_first_card = random.choice(cards)
    comp_cards = random.sample(cards, 2)
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    comp_score = sum(comp_cards)
    player_score = sum(player_cards)


    def add_card():
        #new_card = random.choice(cards)
        #player_cards.append(new_card)
        #print(f"     Your cards: {player_cards}, current score: {sum(player_cards)}")
        #return player_cards
        card = random.choice(cards)
        return card


    if play == "y":
        while comp_score < 21 and player_score < 21:

            print(f"     Your cards : {player_cards}, current score: {player_score}")
            print(f"     Computer's first card: {comp_first_card}")
            add = input("Type 'y' to get another card, type 'n' to pass: ")

            if add == "y":
                new_card = add_card()
                player_cards.append(new_card)
                player_score = sum(player_cards)
                print("\n" * 20)
                print(logo)
            elif add == "n":
                new_card = add_card()
                comp_cards.append(new_card)
                comp_score = sum(comp_cards)
                print("\n" * 20)
                print(logo)
        print(f"     Your final hand: {player_cards}, final score: {sum(player_cards)}")
        print(f"Computer's final hand: {comp_cards}, final score: {sum(comp_cards)} ")

        if player_score > 21:
            print("You busted. You lose. :(")
        elif comp_score > 21 or player_score > comp_score:
            print("Dealer busted. You win! :D")
        else:
            print("You lose. :(")
        new_game()
    else:
        print("Ok!")
new_game()