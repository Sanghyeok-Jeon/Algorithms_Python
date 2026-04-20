import sys

input = sys.stdin.readline

n = int(input())          # 사진틀 개수
m = int(input())          # 추천 횟수
votes = list(map(int, input().split()))

frames = {}  # 학생번호: [추천수, 게시된시각]

for time, student in enumerate(votes):
    if student in frames:
        frames[student][0] += 1
    else:
        if len(frames) < n:
            frames[student] = [1, time]
        else:
            # 추천 수가 가장 적고, 그중 가장 오래된 학생 제거
            remove_student = min(frames, key=lambda x: (frames[x][0], frames[x][1]))
            del frames[remove_student]
            frames[student] = [1, time]

print(*sorted(frames.keys()))