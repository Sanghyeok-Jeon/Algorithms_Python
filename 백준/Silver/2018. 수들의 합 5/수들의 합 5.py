N = int(input())

start, end = 1, 1
current_sum = 1
count = 0

while start <= N:
    if current_sum < N:
        end += 1
        current_sum += end
    elif current_sum > N:
        current_sum -= start
        start += 1
    else:
        count += 1
        end += 1
        current_sum += end

print(count)