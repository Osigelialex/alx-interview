#!/usr/bin/python3
"""
A module that solves the log parsing problem
"""
import sys


def parse_line(line):
    """extracts data from line"""
    line = line.split()
    if len(line) < 7:
        return None, None
    file_size = line[-1]
    status_code = line[-2]
    return int(file_size), status_code


def print_stats(codes, file_size):
    """prints the metrics"""
    print("File size: {}".format(file_size))
    for status_code in sorted(codes.keys()):
        code = codes[status_code]
        if isinstance(code, int) and code > 0:
            print("{}: {}".format(status_code, code))


def main():
    """main function"""
    total_file_size = 0
    line_count = 0
    status_codes = {}

    try:
        for line in sys.stdin:
            file_size, code = parse_line(line)
            line_count += 1

            if code and file_size:
                total_file_size += file_size
                status_codes[code] = status_codes.get(code, 0) + 1

            if line_count % 10 == 0 and line_count > 0:
                print_stats(status_codes, total_file_size)
    except KeyboardInterrupt:
        print_stats(status_codes, total_file_size)


if __name__ == '__main__':
    main()
