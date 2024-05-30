k = list(map(int, list(input())))
l = len(k)

if l == 1:
    answer = '◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!'
else:
    answer = '◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!'
    d = k[0] - k[1]
    for i in range(l-1):
        if k[i] - k[i+1] != d:
            answer = '흥칫뿡!! <(￣ ﹌ ￣)>'
            break

print(answer)