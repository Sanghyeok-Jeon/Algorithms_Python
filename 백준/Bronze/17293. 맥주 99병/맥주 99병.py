N = int(input())
beer = N
while beer >= 0:
    if beer == 0:
        if N == 1:
            print('No more bottles of beer on the wall, no more bottles of beer.')
            print('Go to the store and buy some more, {} bottle of beer on the wall.'.format(N))
        else:
            print('No more bottles of beer on the wall, no more bottles of beer.')
            print('Go to the store and buy some more, {} bottles of beer on the wall.'.format(N))
        break
    elif beer == 1:
        print('1 bottle of beer on the wall, 1 bottle of beer.')
        print('Take one down and pass it around, no more bottles of beer on the wall.')
    elif beer == 2:
        print('2 bottles of beer on the wall, 2 bottles of beer.')
        print('Take one down and pass it around, 1 bottle of beer on the wall.')
    else:
        print('{} bottles of beer on the wall, {} bottles of beer.'.format(beer, beer))
        print('Take one down and pass it around, {} bottles of beer on the wall.'.format(beer-1))
    print()
    beer -= 1