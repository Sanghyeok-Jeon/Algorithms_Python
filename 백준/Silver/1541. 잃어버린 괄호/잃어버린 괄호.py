import sys
listSum = [sum(map(int, splitMinus.split('+'))) for splitMinus in sys.stdin.readline().split('-')]
print(listSum[0]-sum(listSum[1:]))