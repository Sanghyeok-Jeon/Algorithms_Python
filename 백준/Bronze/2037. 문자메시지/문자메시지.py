p, w = map(int, input().split())
text = input()

button = {
          2 : ['A', 'B', 'C'],
          3 : ['D', 'E', 'F'],
          4 : ['G', 'H', 'I'],
          5 : ['J', 'K', 'L'],
          6 : ['M', 'N', 'O'],
          7 : ['P', 'Q', 'R', 'S'],
          8 : ['T', 'U', 'V'],
          9 : ['W', 'X', 'Y', 'Z']
}

num_prev = 0
answer = 0
for t in text:
    num_press = ''
    for num, chars in button.items():
        if t in chars:
            num_press = num

    if num_press == '':
        answer += p
        num_prev = 0
    else:
        cnt_press = 0
        for order in range(len(button[num_press])):
            if t == button[num_press][order]:
                cnt_press = order

        if num_prev == num_press:
            answer += w + p * (cnt_press + 1)
        else:
            answer += p * (cnt_press + 1)

        num_prev = num_press

print(answer)