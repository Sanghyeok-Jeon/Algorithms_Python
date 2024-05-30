T = int(input())

for tc in range(T):
    ox = list(input())
    ans = 0

    count = 1
    for i in range(len(ox)):
        if ox[i] == 'O':
            ans += count
            count += 1
        else:
            count = 1

    print(ans)