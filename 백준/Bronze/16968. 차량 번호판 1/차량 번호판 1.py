plate = input()

init_num = 10
init_alpha = 26
used_num = 9
user_alpha = 25

num = init_num
alpha = init_alpha

answer = 1
for i in range(len(plate)):
    if plate[i] == 'c':
        answer *= alpha
        alpha = user_alpha
        num = init_num
    else:
        answer *= num
        num = used_num
        alpha = init_alpha

print(answer)