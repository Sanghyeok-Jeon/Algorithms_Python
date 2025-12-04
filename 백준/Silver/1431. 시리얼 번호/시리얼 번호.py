def sum_of_digits(s):
    return sum(int(char) for char in s if char.isdigit())

def sort_serial_numbers(serial_numbers):
    serial_numbers.sort(key=lambda x: (len(x), sum_of_digits(x), x))

import sys
input = sys.stdin.readline

n = int(input().strip())
serial_numbers = [input().strip() for _ in range(n)]

sort_serial_numbers(serial_numbers)

for serial in serial_numbers:
    print(serial)