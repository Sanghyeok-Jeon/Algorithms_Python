import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    t = n % 25    # 25시간 주기 상 위치

    if t < 17:
        print("ONLINE")
    else:
        print("OFFLINE")
