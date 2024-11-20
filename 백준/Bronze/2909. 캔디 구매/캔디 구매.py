c, k = map(int, input().split())

money = 10 ** k
result = c // money * money

if c % money >= money / 2:
    result += money

print(result)