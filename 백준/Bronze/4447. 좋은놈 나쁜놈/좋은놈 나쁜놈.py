n = int(input())
for _ in range(n):
    name = input()
    name_lower = name.lower()
    personality = 'NEUTRAL'

    if name_lower.count('g') > name_lower.count('b'):
        personality = 'GOOD'
    elif name_lower.count('g') < name_lower.count('b'):
        personality = 'A BADDY'

    print('{} is {}'.format(name, personality))