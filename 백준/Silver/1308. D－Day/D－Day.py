def is_leap_year(year):
    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True

    return False

def days_in_month(year, month):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return days_in_month[month - 1]

def count_days(year, month, day):
    days = 0

    for y in range(1, year):
        days += 366 if is_leap_year(y) else 365

    for m in range(1, month):
        days += days_in_month(year, m)

    days += day

    return days

def main():
    import sys
    input = sys.stdin.readline
    today = list(map(int, input().split()))
    d_day = list(map(int, input().split()))

    if ((d_day[0] - today[0] > 1000)
            or (d_day[0] - today[0] == 1000 and d_day[1] > today[1])
            or (d_day[0] - today[0] == 1000 and d_day[1] == today[1] and d_day[2] >= today[2])):
        print("gg")
    else:
        today_days = count_days(today[0], today[1], today[2])
        d_day_days = count_days(d_day[0], d_day[1], d_day[2])
        print(f"D-{d_day_days - today_days}")

if __name__ == "__main__":
    main()