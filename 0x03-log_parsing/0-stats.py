#!/usr/bin/python3
"""
A module for solving the log parsing problem

functions:
  validate(line): checks if line meets requirement
"""
import re
import sys


def validate(line):
    """checks if line matches required pattern

    Args:
        line (string): line read from stdin
    """
    pattern = r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.+)\] \"GET " \
        r"\/projects\/260 HTTP\/1\.1\" (\d{3}) (\d+)$"
    return re.match(pattern, line)


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

try:
    for line in sys.stdin:
        if line_count == 10:
            print(f"File size: {total_file_size}")
            for code, count in status_codes.items():
                if count > 0:
                    print(f"{code}: {count}")
            line_count = 0

        if validate(line):
            line_count += 1
            total_file_size += int(line.split()[-1])
            code = line.split()[-2]
            status_codes[code] = status_codes[code] + 1
        else:
            line_count += 1
            pass

except KeyboardInterrupt:
    print(f"File size: {total_file_size}")
    for code, count in status_codes.items():
        if count > 0:
            print(f"{code}: {count}")
