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

    if total <= 0:
        return 0

    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        if total <= 0:
            break

        num_coins = total // coin
        count += num_coins
        total -= num_coins * coin

    if total > 0:
        return -1

    return count
