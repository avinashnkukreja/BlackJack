import random


def total_check(player_hand_values1):

    total = 0

    for card in player_hand_values1:

        total += player_hand_values1[card]

    if total > 21 and "A" in player_hand_values1:

        total -= 10

    return total


def value_assigner(temp_cards):

    temp_dict = {}

    for card in temp_cards:

        if "2" in card:

            temp_dict[card] = 2

        elif "3" in card:

            temp_dict[card] = 3

        elif "4" in card:

            temp_dict[card] = 4

        elif "5" in card:

            temp_dict[card] = 5

        elif "6" in card:

            temp_dict[card] = 6

        elif "7" in card:

            temp_dict[card] = 7

        elif "8" in card:

            temp_dict[card] = 8

        elif "9" in card:

            temp_dict[card] = 9

        elif "10" in card:

            temp_dict[card] = 10

        elif "J" in card:

            temp_dict[card] = 10

        elif "Q" in card:

            temp_dict[card] = 10

        elif "K" in card:

            temp_dict[card] = 10

        else:

            temp_dict[card] = 11

    return temp_dict


def info(j):

    if(show_player == True):

        print("Player", j+1, "'s hand is: ",
              player_hand[j], "Total: ", total_check(player_hand_values[j]))

    if(show_dealer == False):

        print("Dealer's hand is: ", dealer_hand[0],  ",'?'")

    else:

        print("Dealer's hand is: ", dealer_hand,
              "Total: ", total_check(dealer_hand_values))


def card_distributor():

    i = 0

    while(i < n):

        player_hand[i].append(deck[0])

        del deck[0]

        player_hand[i].append(deck[0])

        del deck[0]

        i += 1

    dealer_hand.append(deck[0])

    del deck[0]

    dealer_hand.append(deck[0])

    del deck[0]


playagain = "y"

while(playagain == "y" or playagain == "Y"):

    n = int(input("How many players do you want?(MAXIMUM: 8): "))

    deck = []

    deck_values = {}

    player_hand = [[], [], [], [], [], [], [], []]

    player_hand_values = [{}, {}, {}, {}, {}, {}, {}, {}]

    dealer_hand = []

    player_total = [0, 0, 0, 0, 0, 0, 0, 0]

    dealer_hand_values = {}

    str1 = 'h'

    hit = [True, True, True, True, True, True, True, True]

    stay = [False, False, False, False, False, False, False, False]

    push = [False, False, False, False, False, False, False, False]

    player_win = [True, True, True, True, True, True, True, True]

    blackjack = [False, False, False, False, False, False, False, False]

    player_bust = [False, False, False, False, False, False, False, False]

    show_dealer = False

    show_player = True

    dealer_bust = False

    i = 0

    for suit in '\u2665', '\u2663', '\u2666', '\u2660':

        for rank in '2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'K', 'Q', 'J':

            deck.append(rank+suit)

    random.shuffle(deck)

    deck_values = value_assigner(deck)

    card_distributor()

    i = 0

    while(i < n):

        player_hand_values[i] = value_assigner(player_hand[i])

        i += 1

    dealer_hand_values = value_assigner(dealer_hand)

    i = 0

    while(i < n):

        player_total[i] = total_check(player_hand_values[i])

        i += 1

    i = 0

    while(i < n):

        print("\n\n\nplayer ", i+1, "'s Chance:")

        if(player_total[i] == 21):

            print("Player ", i+1, "'s hand: ",
                  player_hand[i], "Total: ", total_check(player_hand_values[i]))

            print("BLACKJACK!!")

        else:

            print("Enter 0 to surrender.")

            while(hit[i] == True and player_bust[i] == False):

                info(i)

                str1 = input("Do you want to Hit(h) or Stay(s)?  ")

                if(str1 in 'hHsS'):

                    if(str1 == 'H' or str1 == 'h'):

                        hit[i] = True

                        stay[i] = False

                    elif(str1 == 'S' or str1 == 's'):

                        stay[i] = True

                        hit[i] = False

                elif(str1 == '0'):

                    print("Surrendered")

                    break

                else:

                    print("Wrong Input. Considered as Hit.")

                if(hit[i] == True):

                    player_hand[i].append(deck[0])

                    player_hand_values[i] = value_assigner(player_hand[i])

                    del deck[0]

                    player_total[i] = total_check(player_hand_values[i])

                    if(player_total[i] > 21):

                        player_win[i] = False

                        player_bust[i] = True

                        print("Player ", i+1, "'s hand: ",
                              player_hand[i], "Total: ", total_check(player_hand_values[i]))

                        print("BUST!!")

                if(stay[i] == True):

                    break

        i += 1

    print("\n\n")

    show_player = False

    info(0)

    show_dealer = True

    dealer_total = total_check(dealer_hand_values)

    while(dealer_total <= 17):

        info(i)

        if(show_dealer == True):

            dealer_hand.append(deck[0])

            del(deck[0])

        dealer_hand_values = value_assigner(dealer_hand)

        show_dealer = True

        dealer_total = total_check(dealer_hand_values)

    if(dealer_total > 21):

        dealer_bust = True

    info(0)

    print("\n\n")

    i = 0

    while(i < n):

        if(dealer_total > player_total[i] and dealer_bust == False):

            player_win[i] = False

        elif(dealer_total < player_total[i] and player_bust[i] == False):

            player_win[i] = True

        elif(player_total[i] == dealer_total and push[i] == False):

            push[i] = True

        elif(dealer_bust == True and player_bust[i] == True):

            player_win[i] = False

        i += 1

    i = 0

    while(i < n):

        if(push[i] == False):

            if(player_win[i] == True):

                print("Player ", i+1, " WINs!!")

            else:

                print("Player ", i+1, " LOOSEs!!")

        else:

            print("Player ", i+1, " PUSH!!")

        i += 1

    playagain = input("\n\nDo you want to play again?(Yes: Y, No: Any Key): ")
    print("\n\n")
