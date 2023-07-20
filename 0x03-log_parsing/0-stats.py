#!/usr/bin/python3
"""
A module for solvin the log_parsing problem
"""
import sys


status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

total_file_size = 0


def print_stats():
    """displays the metrics"""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print("{}: {}".format(status, status_codes[code]))


if __name__ == "__main__":
    line_count = 0
    try:
        for line in sys.stdin:
            try:
                comp = line.split()
                total_file_size += int(comp[-1])
                if comp[-2] in status_codes:
                    status_codes[comp[-2]] += 1
            except Exception:
                pass
            if count == 9:
                print_stats()
                count = -1
            count += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
