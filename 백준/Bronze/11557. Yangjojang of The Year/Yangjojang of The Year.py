T = int(input())
for tc in range(T):
    N = int(input())
    lst = []
    for _ in range(N):
        univ, drink = input().split()
        lst.append([univ, int(drink)])
    lst.sort(key=lambda x:-x[1])
    print(lst[0][0])