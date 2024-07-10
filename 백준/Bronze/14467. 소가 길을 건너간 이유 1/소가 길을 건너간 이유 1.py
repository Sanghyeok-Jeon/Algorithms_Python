import sys
input = sys.stdin.readline

def count_crossings(observations):
    cow_positions = {}
    crossings = 0

    for cow, position in observations:
        if cow in cow_positions:
            if cow_positions[cow] != position:
                crossings += 1
                cow_positions[cow] = position
        else:
            cow_positions[cow] = position

    return crossings

N = int(input())
observations = []
index = 1
for _ in range(N):
    cow, position = map(int, input().split())
    observations.append((cow, position))

result = count_crossings(observations)
print(result)