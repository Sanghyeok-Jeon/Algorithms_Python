def check_cat():
    for i in range(15):
        for j in range(15):
            if data[i][j] == 'w':
                return 'chunbae'
            elif data[i][j] == 'b':
                return 'nabi'
            elif data[i][j] == 'g':
                return 'yeongcheol'

data = [list(input().split()) for _ in range(15)]
print(check_cat())