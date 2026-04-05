from random import randint

combinations = {
    'straightFlush': {
        'chips': 100,
        'mult': 8,
        'level': 1
    },
    'fourOfAKind': {
        'chips': 60,
        'mult': 7,
        'level': 1
    },
    'fullHouse': {
        'chips': 40,
        'mult': 4,
        'level': 1
    },
    'straight': {
        'chips': 35,
        'mult': 4,
        'level': 1
    },
    'flush': {
        'chips': 30,
        'mult': 4,
        'level': 1
    },
    'threeOfAKind': {
        'chips': 30,
        'mult': 3,
        'level': 1
    },
    'twoPair': {
        'chips': 20,
        'mult': 2,
        'level': 1
    },
    'pair': {
        'chips': 10,
        'mult': 2,
        'level': 1
    },
    'highCard': {
        'chips': 5,
        'mult': 1,
        'level': 1
    }
}

def generateDeck(arr):
    for i in range(2, 15):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        for suit in suits:
            arr.append({
                "rank": i,
                "suit": suit,
                "bonusChips": 0,
                "bonusMult": 0
            })
    return arr
def generateHand(deck, currentHand):
    while len(currentHand) < 8:
        if len(deck) > 0:
            number = randint(0, len(deck) - 1)
            currentHand.append(deck[number])
            deck.remove(deck[number])
        else: break
    return currentHand

def switchRank(rank):
    match rank:
        case 11: rank = "Jack"
        case 12: rank = "Queen"
        case 13: rank = "King"
        case 14: rank = "Ace"
    return rank