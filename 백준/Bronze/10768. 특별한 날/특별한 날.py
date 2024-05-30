month = int(input())
day = int(input())

if month == 1:
    print('Before')
elif month >= 3:
    print('After')
else:
    if day == 18:
        print('Special')
    elif day < 18:
        print('Before')
    else:
        print('After')