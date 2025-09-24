def clear_snow(snow_piles):
    snow_piles.sort(reverse=True)
    time = 0

    while snow_piles:
        if len(snow_piles) >= 2:
            snow_piles[0]-= 1
            snow_piles[1]-= 1
            time += 1

            if snow_piles[1] == 0:
                snow_piles.pop(1)

            if snow_piles[0] == 0:
                snow_piles.pop(0)
        else:
            time += snow_piles[0]
            break

        snow_piles.sort(reverse=True)

    return time

n = int(input())
snow_piles = list(map(int, input().split()))

total_time = clear_snow(snow_piles)
print(total_time if total_time <= 1440 else -1)