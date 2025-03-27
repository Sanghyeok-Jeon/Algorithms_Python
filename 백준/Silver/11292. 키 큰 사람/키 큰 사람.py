while True:
    N = int(input())

    if N == 0:
        break

    data = [list(input().split()) for _ in range(N)]

    max_height = 0
    list_student_max_height = []
    for i in range(N):
        height = float(data[i][1])
        if height > max_height:
            max_height = height
            list_student_max_height = [data[i][0]]
        elif height == max_height:
            list_student_max_height.append(data[i][0])

    print(*list_student_max_height)