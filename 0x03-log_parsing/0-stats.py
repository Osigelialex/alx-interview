#!/usr/bin/python3
"""
A module for solving the log parsing problem

functions:
  validate(line): checks if line meets requirement
  extract_file_size(line): extracts file size from line
  extract_status_code(line): extracts the status code from line
"""
import re


def validate(line):
    """checks if line matches required pattern

    Args:
        line (string): line read from stdin
    """
    pattern = r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.+)\] \"GET " \
        r"\/projects\/260 HTTP\/1\.1\" (\d{3}) (\d+)$"
    return re.match(pattern, line)


def extract_file_size(line):
    """extracts file size for string

    Args:
        line (string): line read from stdin
    """
    return line[line.rfind(' '):]


def extract_status_code(line):
    """extracts status code from line

    Args:
        line (string): line read from stdin
    """
    return line[line.rfind('"') + 2:line.rfind(' ')]


if __name__ == "__main__":
    import sys

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
            if line_count % 10 == 0 and line_count > 0:
                print(f"File size: {total_file_size}")
                for code, count in status_codes.items():
                    if count > 0:
                        print(f"{code}: {count}")
                line_count = 0
                total_file_size = 0
            if validate(line):
                line_count += 1
                total_file_size += int(extract_file_size(line))
                code = extract_status_code(line)
                status_codes[code] += status_codes[code] + 1
            else:
                print("not valid")
    except KeyboardInterrupt:
        print(f"File size: {total_file_size}")
        for code, count in status_codes.items():
            if count > 0:
                print(f"{code}: {count}")
