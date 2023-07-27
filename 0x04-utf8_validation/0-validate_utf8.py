#!/usr/bin/python3
"""module for validating utf-8 encoding
"""
from typing import List


def convert_to_binary(data: List) -> List:
    """Converts a list of integers to binary
    """
    return list(map(lambda x: bin(x)[2:].zfill(8), data))


def get_header(byte: str) -> int:
    """Get number of bytes from header
    """
    if byte.startswith('0'):
        return 0

    header = byte[:byte.find('0')]
    return len(header)


def validUTF8(data: List) -> bool:
    """checks if utf8 encoding is valid
    """
    if data is None:
        return False
    binary_data = convert_to_binary(data)

    for i in range(len(binary_data)):
        header = get_header(binary_data[i])
        if header > 0:
            extra_bytes = binary_data[i + 1: i + header]
            if extra_bytes == [] and i == len(binary_data) - 1:
              return False
            if any([not x.startswith('10') for x in extra_bytes]):
                return False
    return True
