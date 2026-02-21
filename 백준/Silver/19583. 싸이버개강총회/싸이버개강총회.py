import sys

def to_min(t: str) -> int:
    h, m = map(int, t.split(':'))
    return h * 60 + m

input = sys.stdin.readline

S, E, Q = input().split()
S = to_min(S)
E = to_min(E)
Q = to_min(Q)

before = set()   # S 이전에 출석(채팅)한 사람들
after = set()    # E~Q 사이에 채팅한 사람들(출석 후보)

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    t, name = line.split()
    tm = to_min(t)

    if tm <= S:
        before.add(name)
    elif E <= tm <= Q:
        # S 이전에 왔던 사람만 '퇴장 확인' 대상으로 체크
        if name in before:
            after.add(name)

print(len(after))