#!/usr/bin/python3
"""Prime Game Module"""


def isWinner(x, nums):
    """
    Determines the overall winner of a prime number removal game played over
    multiple rounds. In each round, players take turns removing numbers from
    a set of consecutive integers (1 to n) based on prime numbers. The player
    unable to make a move loses the round.

    Args:
        x (int): The number of rounds to be played.
        nums (list of int): A list where each element represents the maximum
        number in the set for a given round (e.g., 1 to nums[i]).

    Returns:
        str: "Maria" if Maria wins the most rounds, "Ben" if Ben wins the most
        rounds, or None if there is no clear winner.

    Raises:
        None: This function does not raise exceptions directly.
    """
    # Validate inputs
    if not isinstance(x, int) or x <= 0\
            or not isinstance(nums, list) or not nums:
        return None

    # Determine the maximum number for prime computation
    max_num = max(nums)

    # Generate prime numbers up to max_num using Sieve of Eratosthenes
    primes = sieve_of_eratosthenes(max_num)

    # Initialize scores for Maria and Ben
    ben_score = 0
    maria_score = 0

    # Play each round
    for n in nums:
        # Count the number of prime numbers in the range 1 to n
        prime_count = sum(primes[:n + 1])

        # Decide the winner of this round based on the prime count
        if prime_count % 2 == 0:
            ben_score += 1  # Ben wins if the count is even
        else:
            maria_score += 1  # Maria wins if the count is odd

    # Determine the overall winner
    if ben_score > maria_score:
        return "Ben"
    if maria_score > ben_score:
        return "Maria"
    return None


def sieve_of_eratosthenes(n):
    """
    Generates a boolean list that indicates whether each number up to `n` is
    prime using the Sieve of Eratosthenes algorithm.

    Args:
        n (int): The upper limit for generating prime numbers.

    Returns:
        list: A list of size `n+1` where the value at index `i` is 1 if `i`
        is a prime number, and 0 otherwise.

    Raises:
        None: This function does not raise exceptions directly.
    """
    if n < 2:
        return [0] * (n + 1)  # No primes below 2

    # Initialize all numbers as prime
    primes = [1] * (n + 1)
    primes[0], primes[1] = 0, 0  # Mark 0 and 1 as non-prime

    # Mark multiples of each prime starting from 2
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:  # If i is a prime
            for multiple in range(i * i, n + 1, i):
                primes[multiple] = 0  # Mark multiples as non-prime
    return primes
