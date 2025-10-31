import sys
import math

input = sys.stdin.readline

def solve(s, i):
    global cnt
    if i == len(string):
        cnt += 1
        if cnt == n:
            return s
        return None
    for k in string:
        if k not in s:
            res = solve(s + k, i + 1)
            if res:
                return res
    return None

while True:
    line = input().strip()
    if not line:
        break
    string, num = line.split()
    n = int(num)

    total = math.factorial(len(string))
    if n > total:
        print(f"{string} {n} = No permutation")
        continue

    cnt = 0
    result = solve("", 0)
    print(f"{string} {n} = {result}")