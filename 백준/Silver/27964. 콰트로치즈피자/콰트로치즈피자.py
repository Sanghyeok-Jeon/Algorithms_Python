N = int(input())
data = list(input().split())

cheese = set()
for d in data:
    if len(d) >= 6 and d[-6:] == 'Cheese':
        cheese.add(d)

if len(cheese) >= 4:
    print('yummy')
else:
    print('sad')