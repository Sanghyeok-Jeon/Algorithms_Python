import re

pattern = re.compile('[A-F]?A+F+C+[A-F]?$')

T = int(input())
for _ in range(T):
    chromosome = input()
    if pattern.fullmatch(chromosome):
        print('Infected!')
    else:
        print('Good')