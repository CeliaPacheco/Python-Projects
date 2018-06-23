def facedown(player_deck, war_deck, num_card):
    """
    Function creates a list of facedown cards from the main player deck
    player_deck is the players main deck
    war_deck is the face down cards
    num_car is number of cards to take from player_deck and place into war_deck
    """
    for i in range(num_card):
        war_deck.append(player_deck.pop(0))


def add_to_deck(player_deck, cards):
    """
    Function appends numbers from a list onto another list
     player_deck is the main player deck
     cards is a list of cards of which to pop off and append to the player deck
    """
    for i in range(len(cards)):
        player_deck.append(cards[i])


# def sub_war(player1, player2):
#     """
#     Function determines the winner of a war
#     :param player1: Player 1 deck
#     :param player2: Player 2 deck
#     :return: 1 if player 1 wins battle 2 if player 2 wins battle followed by battle cards
#     """
#     if (len(player1) and len(player2) == 0):
#         return 0
#     player1_card = player1.pop(0)
#     player2_card = player2.pop(0)
#     if player1_card == player2_card:
#         war(player1, player2, player1_card, player2_card)
#     if player1_card > player2_card:
#         return [1, player1_card, player2_card]
#     else:
#         return [2, player1_card, player2_card]


def war(player1, player2, player1_card, player2_card):
    """
    Function runs the war portion of the game
    :param player1: List of player 1 cards
    :param player2: List of player 2 cards
    :param player1_card: Player 1 battle card
    :param player2_card: Player 2 battle card
    :return:
    """
    p1_facedown = []
    p2_facedown = []
    print("Player1:",len(player1))
    print("Player2:",len(player2))
    print((len(player1) == 3 or len(player2) == 3))
    if len(player1) == 3 or len(player2) == 3:
        facedown(player1, p1_facedown, 2)
        facedown(player2, p2_facedown, 2)
    elif (len(player1) or len(player2)) == 2:
        facedown(player1, p1_facedown, 1)
        facedown(player2, p1_facedown, 1)
    elif (len(player1) and len(player2)) > 3:
        facedown(player1, p1_facedown, 3)
        facedown(player2, p2_facedown, 3)
    battle_card_1 = player1.pop(0)
    battle_card_2 = player2.pop(0)
    p1_facedown.append(battle_card_1)
    p2_facedown.append(battle_card_2)
    # player 1 won sub_war
    if battle_card_1 > battle_card_2:
        add_to_deck(player1, p1_facedown)
        add_to_deck(player1, p2_facedown)
        player1.append(player1_card)
        player1.append(player2_card)
        return 1
    elif battle_card_2 > battle_card_1:
        add_to_deck(player2, p2_facedown)
        add_to_deck(player2, p1_facedown)
        player2.append(player2_card)
        player2.append(player1_card)
        return 2
    else:
        sub_war = war(player1, player2, battle_card_1, battle_card_2)
        if sub_war == 1:
            add_to_deck(player1, p1_facedown)
            add_to_deck(player1, p2_facedown)
            player1.append(player1_card)
            player1.append(player2_card)
        elif sub_war == 2:
            add_to_deck(player2, p2_facedown)
            add_to_deck(player2, p1_facedown)
            player2.append(player2_card)
            player2.append(player1_card)


def game(player1, player2):
    """
    function runs the game and every battle. If a war is encountered
    then a new function is called to handle the war
    player1 is a list containing the player's cards
    player2 is the same as player1 but for player2.
    """
    player1_card = player1.pop(0)  # battle card
    player2_card = player2.pop(0)  # battle card
    #    print("player1 {}, player2 {}".format(player1_card, player2_card))
    if player1_card == player2_card:
        war(player1, player2, player1_card, player2_card)
        #    print("player1 {}, player2 {}".format(player1_card, player2_card))
    elif player1_card > player2_card:
        player1.append(player1_card)
        player1.append(player2_card)
    else:
        player2.append(player2_card)
        player2.append(player1_card)
    return 1


def main():
    filename = input("File name: ")
    #    filename = "war1.txt"
    file = open(filename, "r")
    line = file.readline()
    player1_deck = line.split(" ")
    player1_deck = [int(i) for i in player1_deck]
    line = file.readline()
    player2_deck = line.split(" ")
    player2_deck = [int(i) for i in player2_deck]
    file.close()
    #    print(player1_deck, "\n", player2_deck)
    while len(player1_deck) != 0 and len(player2_deck) != 0:
        #    print("player1 length {}, player2 length {}".format(len(player1_deck), len(player2_deck)))
        game(player1_deck, player2_deck)
    if len(player1_deck) == 0:
        print("2")
    else:
        print("1")
    return 1

if __name__ == '__main__':
    main()
