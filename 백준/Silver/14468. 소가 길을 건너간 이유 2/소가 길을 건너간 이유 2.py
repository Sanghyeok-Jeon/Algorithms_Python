import sys
input = sys.stdin.readline

record = input()

meet_cow = 0
for i in range(52):
    for o in range(i + 1, 52):
        if record[i] == record[o]:
            cows = record[i:o + 1]
            
            for cow in cows:
                if cows.count(cow) == 1:
                    meet_cow += 1

            break

print(meet_cow // 2)