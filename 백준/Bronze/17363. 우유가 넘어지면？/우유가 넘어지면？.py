N, M = map(int, input().split())
origin_data = [input() for _ in range(N)]

dict_char_chg = {
    '.': '.',
    'O': 'O',
    '-': '|',
    '|': '-',
    '/': '\\',
    '\\': '/',
    '^': '<',
    '<': 'v',
    'v': '>',
    '>': '^'
}

for j in range(M - 1, -1, -1):
    for i in range(N):
        print(dict_char_chg[origin_data[i][j]], end='')
    print()