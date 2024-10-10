#!/usr/bin/python3
"""
Module to solve the lock-boxes problem.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked based on the keys inside.
    Args:
        boxes (list): A list of lists, where each list contains keys for other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    unlocked = [0] 
    keys = set(boxes[0]) 

    # Continue checking boxes until there are no new keys to check
    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in unlocked:
            unlocked.append(key)
            keys.update(boxes[key])

    return len(unlocked) == len(boxes)
