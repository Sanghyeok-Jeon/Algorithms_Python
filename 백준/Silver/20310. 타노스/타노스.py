S = list(input())

cnt_zero = S.count('0') // 2
cnt_one = S.count('1') // 2

cnt_zero_plus = 0
cnt_one_minus = 0
answer = ''
for i in range(len(S)):
    if S[i] == '0':
        if cnt_zero_plus < cnt_zero:
            answer += '0'
            cnt_zero_plus += 1
    else:
        if cnt_one_minus < cnt_one:
            cnt_one_minus += 1
        else:
            answer += '1'

print(answer)