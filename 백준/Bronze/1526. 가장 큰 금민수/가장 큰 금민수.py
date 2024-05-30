def DFS(length, strNum):
    global result

    if strNum and int(strNum) <= N:
        result = max(result, int(strNum))

    if length == 7:
        return
    else:
        DFS(length+1, strNum + '4')
        DFS(length+1, strNum + '7')

N = int(input())
result = 0
DFS(0, '')
print(result)