import sys
input = sys.stdin.readline

while True:
    data = input()
    if not data:
        break

    N, M = data.split()

    answer = 0
    for num in range(int(N), int(M) + 1):
        if len(str(num)) == len(set(str(num))):
            answer += 1

    print(answer)