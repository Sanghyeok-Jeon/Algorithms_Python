def min_clock_number(numbers):
    min_number = float('inf')
    for i in range(4):
        rotated_number = int(''.join(map(str, numbers[i:]+ numbers[:i])))
        min_number = min(min_number, rotated_number)
    return min_number

def count_clock_numbers_up_to(target):
    count = 0
    for i in range(1111, target + 1):
        digits = list(map(int, str(i)))
        if 0 in digits:
            continue
        if min_clock_number(digits) == i:
            count += 1
    return count

numbers = list(map(int, input().split()))

min_number = min_clock_number(numbers)

result = count_clock_numbers_up_to(min_number)

print(result)
