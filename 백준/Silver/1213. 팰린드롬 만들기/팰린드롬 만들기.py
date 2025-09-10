from collections import Counter

name = input()
count = Counter(name)

odd_count = 0
mid_char = ''
front = ''

for char in sorted(count):
    if count[char] % 2:
        odd_count += 1
        mid_char = char

    front += char * (count[char] // 2)

if odd_count > 1:
    print("I'm Sorry Hansoo")
else:
    print(front + (mid_char if odd_count == 1 else '') + front[::-1])