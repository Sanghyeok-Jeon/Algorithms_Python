N = int(input())
divisor = sorted(list(map(int, input().split())))

print(divisor[0] * divisor[-1])