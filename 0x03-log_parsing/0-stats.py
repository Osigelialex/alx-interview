#!/usr/bin/python3
"""
A module for solving the log parsing problem
"""


total_file_size = 0
line_count = 0
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

def print_stat():
    """
    prints the metrics
    """
    print(f"File size: {total_file_size}")
    for code, count in status_codes.items():
        if count > 0:
            print(f"{code}: {count}")


if __name__ == "__main__":
    import sys

    try:
        for line in sys.stdin:
            if line_count == 10:
                print_stat()
                line_count = 0

            line_count += 1
            total_file_size += int(line.split()[-1])
            code = line.split()[-2]
            status_codes[code] = status_codes[code] + 1

    except KeyboardInterrupt:
        print_stat()
