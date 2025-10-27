N = int(input())
pattern = input().split('*')

for _ in range(N):
    filename = input()

    if len(filename) < len(pattern[0]) + len(pattern[1]):
        print('NE')
    elif filename.startswith(pattern[0]) and filename.endswith(pattern[1]):
        print('DA')
    else:
        print('NE')