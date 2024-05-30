result = []
for i in range(1, 6):
    agent = input()

    if 'FBI' in agent:
        result.append(i)

if len(result):
    print(*result)
else:
    print('HE GOT AWAY!')