"The purpose of this program is to demonstrate how to simulate the results "
" of a series of racquetball games between two players, Player A and Player B"
" This allows us to determine with some confidence which player will win"


from random import random
#what we're importing is a pseudo-random number generator that always
#returns a value between 0, non-inclusive and 1 inclusive. That is, it can
#return 1.0 but it can never return 0.0

def printIntro ():
    """
    This function prints out introductory text for the user
    :param: none
    :return: none
    """
    print("This program simulates a game of racquetball between two")
    print("players called 'A' and 'B' The skill of each player is")
    print("represented by the probability of that player winning a point")
    print("when that player serves. This probability is expressed as a")
    print("floating point number between 0 and 1")
    print("PLayer A will always serve first")

def getInputs():
    """
    This function prompts the user for three input values: the probability of
    A winning a point on serve; the probability of B winning a point on
    serve; and the number of games to simulate. (More games gives a truer
    probability of winning)
    :return: a: A's probability of winning; b: B's probability of winning;
    n: Number of games to simulate
    """
    a = float(input("Please enter the probability of A winning a point when serving: "))
    b = float(input("Please enter the probability of B winning a point when serving: "))
    n = int(input("Please enter the number of games to simulate: "))
    return a, b, n

def simNgames(n, pA, pB):
    """

    :param n: number of games to simulate
    :param pA: probablity of A winning a point on serve
    :param pB: probablity of B winning a point on serve
    :return: winA: the number of games won by A; winB: the number of games won by B
    """
    winA = 0
    winB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(pA, pB)
        if scoreA > scoreB:
            winA += 1
        else:
            winB += 1
    return winA, winB

def simOneGame(pA, pB):
    """

    :param pA: probablity of A winning a point on serve
    :param pB: probablity of B winning a point on serve
    :return: the score of the game for A, and for B
    """
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < pA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < pB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver(scoreA, scoreB):
    """

    :param scoreA:
    :param scoreB:
    :return: True if one player has 15 points; False otherwise
    """
    if scoreA == 15 or scoreB == 15:
        return True
    else:
        return False

def printSummary(winA, winB):
    """

    :param winA: the number of games won by A
    :param winB: the number of games won by B
    :return: None
    """
    n = winA + winB
    print("Games played: " + str(n))
    print("Wins for A: ", winA, "or :", 100*winA/n, " %")
    print("Wins for B: ", winB, "or :", 100*winB/n, " %")

if __name__ == "__main__":
    printIntro()
    a, b, n = getInputs()
    winA, winB = simNgames(n, a, b)
    printSummary(winA, winB)




