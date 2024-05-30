T = int(input())
for tc in range(T):
    arrayString = list(input().split())
    newString = ''
    for str in arrayString:
        newString += str[::-1] + ' '
    print(newString)