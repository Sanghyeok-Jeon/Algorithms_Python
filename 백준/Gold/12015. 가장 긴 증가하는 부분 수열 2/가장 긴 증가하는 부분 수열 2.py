from bisect import bisect_left

# 가장 긴 증가하는 부분 수열의 길이를 구하는 함
def get_lis_length(arr):
    lis = [arr[0]]    # 가장 긴 증가하는 부분 수열을 저장하는 리스트

    for num in arr[1:]:
        if num > lis[-1]:
            lis.append(num)
        else:
            idx = bisect_left(lis, num)
            lis[idx] = num

    return len(lis)

N = int(input())
arr = list(map(int, input().split()))

# 가장 긴 증가하는 부분 수열의 길이 구하기
result = get_lis_length(arr)

print(result)