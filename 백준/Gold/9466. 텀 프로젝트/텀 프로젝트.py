import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(student, visited, cycle, team):
    visited[student] = True    # 선택됨으로 변경
    cycle.append(student)    # 사이클에 추가

    next_student = team[student]    # 다음 학생 = 선택된 학생이 선택한 학생
    if visited[next_student]:    # 다음 학생이 이미 선택된 학생인 경우
        if next_student in cycle:    # 사이클을 이루는 학생인 경우
            start = cycle.index(next_student)    # 사이클 시작 지검 인덱스
            return cycle[start:]    # 사이클을 이루는 학생들
        else:
            return []    # 사이클을 이루지 않는 경우
    else:
        return dfs(next_student, visited, cycle, team)    # 다음 학생으로 재귀 호출

def solve(n, team):
    visited = [False] * (n + 1)
    result = []    # 사이클이 생기는 학생들 저장할 리스트

    for i in range(1, n+1):
        if not visited[i]:    # 아직 선택하지 않은 학생의 경우
            cycle = dfs(i, visited, [], team)
            result.extend(cycle)    # 학생값만 추가하기 위해 extend 사용

    return n - len(result)    # 사이클을 이루지 않는 학생들의 수 반환

T = int(input())
for _ in range(T):
    n = int(input())
    team = [0] + list(map(int, input().split()))    # 각 학생별 프로젝트를 함께하고 싶은 학생

    print(solve(n, team))