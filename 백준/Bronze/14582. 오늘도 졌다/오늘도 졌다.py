geminis = list(map(int, input().split()))
gullivers = list(map(int, input().split()))

win_geminis_final = False
win_geminis_temp = False

total_score_geminis = 0
total_score_gullivers = 0
for i in range(9):
    total_score_geminis += geminis[i]

    if total_score_geminis > total_score_gullivers:
        win_geminis_temp = True

    total_score_gullivers += gullivers[i]

if total_score_geminis > total_score_gullivers:
    win_geminis_final = True
elif total_score_geminis < total_score_gullivers:
    win_geminis_final = False

if win_geminis_temp and not win_geminis_final:
    print('Yes')
else:
    print('No')