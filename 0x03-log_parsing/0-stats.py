#!/usr/bin/python3
"""
Log Parsing Script
"""


import sys


def print_statistics(stats: dict, total_size: int) -> None:
    """Prints the statistics of HTTP status codes and total file size."""
    print(f"Total file size: {total_size}")
    for code, count in sorted(stats.items()):
        if count:
            print(f"{code}: {count}")


def process_log_lines():
    """Processes incoming log lines from standard input."""
    total_size = 0
    line_count = 0
    valid_status_codes = [
        "200", "301", "400", "401", "403", "404", "405", "500"
    ]
    stats = {code: 0 for code in valid_status_codes}

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            # Extract the status code and file size
            try:
                status_code = parts[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except IndexError:
                continue  # Skip lines that do not have enough data

            try:
                total_size += int(parts[-1])
            except (IndexError, ValueError):
                continue  # Skip lines that do not have a valid file size

            # Print statistics every 10 lines processed
            if line_count % 10 == 0:
                print_statistics(stats, total_size)

        # Print final statistics
        print_statistics(stats, total_size)

    except KeyboardInterrupt:
        print_statistics(stats, total_size)
        raise


if __name__ == '__main__':
    process_log_lines()
