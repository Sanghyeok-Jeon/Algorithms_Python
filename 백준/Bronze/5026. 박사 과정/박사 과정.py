N = int(input())
for _ in range(N):
    data = input()
    if data[0] == 'P':
        print('skipped')
    else:
        for i in range(len(data)):
            if data[i] == '+':
                print(int(''.join(data[:i])) + int(''.join(data[i+1:])))