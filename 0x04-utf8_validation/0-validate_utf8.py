#!/usr/bin/python3
"""UTF-8 Validation Module"""


def validUTF8(data):
    """
    A function checks whether if the data is UTF-8 encoded or not

    :param data: The data to be checked

    :return: True if the data is UTF-8 encoded  False otherwise
    """
    binary_representation = []
    flag = 0
    valid = True
    for i in data:
        binary_representation.append(format(i, '08b'))
    for byte in range(len(binary_representation)):
        if binary_representation[byte][0] == '0':
            continue
        elif binary_representation[byte][0:2] == '10' and flag > 0:
            flag -= 1
        elif binary_representation[byte][0:3] == '110':
            if byte + 1 < len(binary_representation):
                if binary_representation[byte + 1][0:2] == '10':
                    flag = 1
                else:
                    valid = False
            else:
                valid = False
        elif binary_representation[byte][0:4] == '1110':
            if byte + 2 < len(binary_representation):
                if (binary_representation[byte + 1][0:2] == '10'
                        and binary_representation[byte + 2][0:2] == '10'):
                    flag = 2
                else:
                    valid = False
            else:
                valid = False
        elif binary_representation[byte][0:5] == '11110':
            if byte + 3 < len(binary_representation):
                if (binary_representation[byte + 1][0:2] == '10'
                        and binary_representation[byte + 2][0:2] == '10'
                        and binary_representation[byte + 3][0:2] == '10'):
                    flag = 3
                else:
                    valid = False
            else:
                valid = False
        else:
            valid = False
    return valid
