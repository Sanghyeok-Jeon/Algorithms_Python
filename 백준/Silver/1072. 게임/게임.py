def minimum_games_to_increase_win_rate(x, y):
    current_rate = (y * 100) // x
    if current_rate >= 99:
        return -1

    low, high = 0, 1_000_000_000
    result = -1

    while low <= high:
        mid = (low + high) // 2
        new_rate = ((y + mid) * 100) // (x + mid)

        if new_rate > current_rate:
            result = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return result

X, Y = map(int, input().split())
print(minimum_games_to_increase_win_rate(X, Y))