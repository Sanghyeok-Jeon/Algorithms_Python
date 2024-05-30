odd = False
ans = 1
ABC = list(map(int, input().split()))
for abc in ABC:
    if abc % 2:
        ans *= abc
        odd = True

print(ans if odd else ABC[0]*ABC[1]*ABC[2])