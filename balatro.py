from time import sleep
import balatroFuncs as game

deck = game.generateDeck([])

hasPassed = False
rounds = 1

while True:
    ante = rounds // 3 + 1
    chipsRequired = round(300 * rounds)
    chipsScored = 0
    maxChips = 0
    hands = 4
    discards = 3

    print(f"---------------------------------\n"
          f"You're on Ante: {ante}/8 and Round: {rounds}\n"
          f"Next round's chip requirements: {chipsRequired}\n"
          f"---------------------------------\n")
    input("Press Enter to start the round...")

    currentDeck = deck.copy()
    hand = sorted(game.generateHand(currentDeck, []), key=lambda c: c['rank'])

    while chipsScored < chipsRequired:
        if len(hand) <= 0 or hands <= 0:
            break

        print("---------------------------------\n"
              f"Chips Required: {chipsRequired}\n"
              f"Chips Scored: {chipsScored}\n"
              f"Hands: {hands}; Discards: {discards}\n"
              "---------------------------------")
        for card in hand:
            rank = game.switchRank(card["rank"])
            print(f"{rank} of {card['suit']}")
        print("---------------------------------")
        while True:
            command = input("Select command (play/discard)...").lower()
            if command == "discard" and discards <= 0: print('You have no discards left')
            elif command == "play" or command == "discard": break
            else: print('Incorrect Command, try again')
        playedCards = set(input(f"Select cards (enter a number from 1 to 8) to {command}...").replace(" ", ""))
        if len(playedCards) > min(5, len(hand)) or len(playedCards) == 0:
            print("Your hand must have at LEAST 1 card and 5 cards at MOST")
            sleep(2)
        else:
            try:
                filteredHand = [x for x in playedCards if 0 < int(x) <= len(hand)]
                if len(filteredHand) != len(playedCards):
                    print("Your hand is out of range")
                    sleep(2)
                else:
                    scoreChips = 0
                    scoreMult = 1
                    print(f'You {command}ed:')
                    for index in playedCards:
                        i = int(index) - 1
                        scoreChips += hand[i]['rank']
                        rank = game.switchRank(hand[i]['rank'])
                        print(f'-- {rank} of {hand[i]['suit']} {f": +{hand[i]['rank']} Chips" if command != 'discard' else ''}')
                    hand = sorted(game.generateHand(currentDeck, [x for x in hand if str(hand.index(x) + 1) not in playedCards]), key=lambda c: c['rank'])
                    sleep(1)
                    if command == 'play':
                        chipsScored += scoreChips * scoreMult
                        hands -= 1
                        maxChips = max(maxChips, chipsScored)
                        print('\n'
                              f'Chips: {scoreChips}, Mult: {scoreMult}')
                        sleep(1)
                    else: discards -= 1
            except ValueError:
                print("Invalid literals, try again")
                sleep(1)
    else: hasPassed = True

    if not hasPassed:
        print("--------------------------------\n"
              "--------------------------------\n"
              "--------------------------------\n"
              "-------    GAME OVER      ------\n"
              "--------------------------------\n"
              "--------------------------------\n"
              "--------------------------------\n"
              "\n"
              f"Maximum Chips Scored:{maxChips}\n"
              f"Runs Lived: {rounds}\n"
              f"Antes Lived: {ante}\n")
        break
    else:
        rounds += 1
        if rounds == 24:
            print("--------------------------------\n"
                  "--------------------------------\n"
                  "--------------------------------\n"
                  "------      YOU WIN       ------\n"
                  "--------------------------------\n"
                  "--------------------------------\n"
                  "--------------------------------\n"
                  "\n"
                  f"Maximum Chips Scored:{maxChips}\n"
                  f"\n"
                  f"\n")

            isContinued = True
            while True:
                question = input('Continue? (y/n)').lower()
                if question != 'y' and question != 'n':
                    print('Incorrect command')
                else:
                    isContinued = False if question == 'n' else True
                    break
            if not isContinued: break
        hasPassed = False


        # somehow need to make it cycle through combinations and check which one is played
        # shop system
        # enhancements