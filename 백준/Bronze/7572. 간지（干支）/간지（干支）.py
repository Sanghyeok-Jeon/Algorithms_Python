iji = 'ABCDEFGHIJKL'
gan = '0123456789'

N = int(input()) - 4
target = N % 60
print(iji[target % 12] + gan[target % 10])