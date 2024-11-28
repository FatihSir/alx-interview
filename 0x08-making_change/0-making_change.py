#!/usr/bin/python3
"""Coins Module"""


def makeChange(coins, total):
    """
    A function that determines how many coins you have to make up the total

    :param coins: the list of coins available
    :param total: the total number of coins to meet the total
    :return: 0 if the total is 0 or less,
            -1 if the total can not be met by the coins,
            number of coins that make up the total
    """
    solution = {}
    if total <= 0:
        return 0

    while total != 0:
        passed_coins = [x for x in coins if total >= x]
        if len(passed_coins) > 0:
            coin = max(passed_coins)
            if total // coin > 1:
                if total % coin == 0:
                    solution[coin] = total / coin
                    return solution
                else:
                    solution[coin] = total // coin
                    total -= coin * (total // coin)
            else:
                solution[coin] = 1
                total -= coin
        else:
            return -1
    return sum(solution.values())
