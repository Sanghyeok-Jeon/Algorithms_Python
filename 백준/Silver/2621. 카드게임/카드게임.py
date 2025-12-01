def calculate_score(cards):
    from collections import Counter

    colors = [card[0] for card in cards]
    numbers = [int(card[1]) for card in cards]

    color_count = Counter(colors)
    number_count = Counter(numbers)

    is_flush = len(color_count) == 1
    sorted_numbers = sorted(numbers)
    is_straight = sorted_numbers == list(range(sorted_numbers[0], sorted_numbers[0]+ 5))

    if is_flush and is_straight:
        return 900 + sorted_numbers[-1]
    if 4 in number_count.values():
        four_number = max(number_count, key=lambda x: number_count[x])
        return 800 + four_number
    if 3 in number_count.values() and 2 in number_count.values():
        three_number = max(number_count, key=lambda x: number_count[x] == 3)
        two_number = max(number_count, key=lambda x: number_count[x] == 2)
        return 700 + 10 * three_number + two_number
    if is_flush:
        return 600 + sorted_numbers[-1]
    if is_straight:
        return 500 + sorted_numbers[-1]
    if 3 in number_count.values():
        three_number = max(number_count, key=lambda x: number_count[x])
        return 400 + three_number
    if list(number_count.values()).count(2) == 2:
        pairs = [num for num in number_count if number_count[num] == 2]
        return 300 + max(pairs) * 10 + min(pairs)
    if 2 in number_count.values():
        pair_number = max(number_count, key=lambda x: number_count[x])
        return 200 + pair_number
    return 100 + sorted_numbers[-1]

import sys
input = sys.stdin.readline

cards = [list(input().split()) for _ in range(5)]
score = calculate_score(cards)
print(score)