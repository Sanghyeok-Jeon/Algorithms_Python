data = input()
answer = ''

for d in data:
    if d.isupper():
        answer += chr(ord(d)+13) if ord(d)+13 <= ord('Z') else chr(ord(d)+13-ord('Z')+ord('A')-1)
    elif d.islower():
        answer += chr(ord(d)+13) if ord(d)+13 <= ord('z') else chr(ord(d)+13-ord('z')+ord('a')-1)
    else:
        answer += d

print(answer)