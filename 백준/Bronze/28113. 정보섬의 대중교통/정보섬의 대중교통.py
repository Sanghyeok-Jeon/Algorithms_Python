N, A, B = map(int, input().split())
if A == B and N <= B:
    print('Anything')
elif A > B and N <= B:
    print('Subway')
else:
    print('Bus')