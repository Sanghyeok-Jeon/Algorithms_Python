import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

# "SciComLove"의 대문자 위치
origin_str = 'SciComLove'
origin_upper = [os.isupper() for os in origin_str]
origin_length = len(origin_str)

# N 길이의 문자열에 대한 대문자 여부 배열
is_upper = [origin_upper[i % origin_length] for i in range(N)]

# 초기 대문자 개수 계산
current_upper_cnt = sum(is_upper)

# 처리
for _ in range(Q):
    idx = int(input()) - 1
    if is_upper[idx]:
        current_upper_cnt -= 1
    else:
        current_upper_cnt += 1

    is_upper[idx] = not is_upper[idx]
    print(current_upper_cnt)