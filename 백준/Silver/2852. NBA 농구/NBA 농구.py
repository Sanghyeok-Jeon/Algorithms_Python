import sys
input = sys.stdin.readline

def to_sec(t):
    m, s = map(int, t.split(':'))
    return m * 60 + s

def to_time_str(sec):
    m = sec // 60
    s = sec % 60
    return f"{m:02d}:{s:02d}"

N = int(input().strip())

score1 = score2 = 0
win1_time = win2_time = 0

prev_time = 0

for _ in range(N):
    team, t = input().split()
    cur_time = to_sec(t)

    if score1 > score2:
        win1_time += cur_time - prev_time
    elif score2 > score1:
        win2_time += cur_time - prev_time

    if team == '1':
        score1 += 1
    else:
        score2 += 1

    prev_time = cur_time

end_time = 48 * 60
if score1 > score2:
    win1_time += end_time - prev_time
elif score2 > score1:
    win2_time += end_time - prev_time

print(to_time_str(win1_time))
print(to_time_str(win2_time))
