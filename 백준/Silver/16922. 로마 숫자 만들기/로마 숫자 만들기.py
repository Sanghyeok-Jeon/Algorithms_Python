from itertools import combinations_with_replacement

n = int(input())
roman_numbers = [1, 5, 10, 50]

result = set()
for combo in combinations_with_replacement(roman_numbers, n):
    result.add(sum(combo))

print(len(result))