def check():
    N = int(input())
    for _ in range(N):
        tmpString = input()
        if tmpString not in raString:
            return 'Yes'

    return 'No'

raString = ['Never gonna give you up',
            'Never gonna let you down',
            'Never gonna run around and desert you',
            'Never gonna make you cry',
            'Never gonna say goodbye',
            'Never gonna tell a lie and hurt you',
            'Never gonna stop']

print(check())