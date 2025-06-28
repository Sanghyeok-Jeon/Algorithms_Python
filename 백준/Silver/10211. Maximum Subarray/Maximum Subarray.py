def max_subarr_sum(arr):
    max_current = arr[0]
    answer = arr[0]

    for num in arr[1:]:
        max_current = max(num, max_current + num)
        answer = max(answer, max_current)

    return answer

T = int(input())
for _ in range(T):
    N = int(input())
    X = list(map(int, input().split()))

    print(max_subarr_sum(X))