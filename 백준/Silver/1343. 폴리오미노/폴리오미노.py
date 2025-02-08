board = input()

answer = ''
len_polyomino = 0
for i in range(len(board)):
    if board[i] == '.':
        if len_polyomino % 2:
            answer = -1
            break

        answer += 'AAAA' * (len_polyomino // 4) + 'BB' * (len_polyomino % 4 // 2)
        answer += '.'
        len_polyomino = 0
    else:
        len_polyomino += 1

if len_polyomino % 2:
    answer = -1

if answer != -1:
    answer += 'AAAA' * (len_polyomino // 4) + 'BB' * (len_polyomino % 4 // 2)

print(answer)