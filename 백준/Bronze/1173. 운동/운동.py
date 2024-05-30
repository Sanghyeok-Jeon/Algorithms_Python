N, m, M, T, R = map(int, input().split())

needMinute = 0
minuteWorkout = 0
nowPulse = m
while True:
    if minuteWorkout == N:
        break
    
    if m + T > M:
        break
    
    if nowPulse + T <= M:
        minuteWorkout += 1
        nowPulse += T
    else:
        nowPulse -= R
        if nowPulse < m:
            nowPulse = m
    
    needMinute += 1
    
print(needMinute if minuteWorkout else -1)