N = int(input())
ST = input()

while len(ST):
    if ST.count('s') == ST.count('t'):
        print(ST)
        break

    ST = ST[1:]