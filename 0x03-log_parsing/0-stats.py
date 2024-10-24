#!/usr/bin/python3
"""
Log Parsing Script
"""


import sys


def print_stats(stats: dict, file_size: int) -> None:
    """Prints the statistics of HTTP status codes and total file size."""
    print("File size: {:d}".format(file_size))
    for code, count in sorted(stats.items()):
        if count:
            print("{}: {}".format(code, count))


if __name__ == '__main__':
    file_size, count = 0, 0
    valid_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {code: 0 for code in valid_codes}

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except IndexError:
                pass  # Skip lines that do not have enough data
            try:
                file_size += int(data[-1])
            except (IndexError, ValueError):
                pass  # Skip lines that do not have a valid file size
            if count % 10 == 0:
                print_stats(stats, file_size)
        print_stats(stats, file_size)
    except KeyboardInterrupt:
        print_stats(stats, file_size)
        raise
