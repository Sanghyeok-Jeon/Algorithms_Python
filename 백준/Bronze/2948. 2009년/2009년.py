days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

D, M = map(int, input().split())

w = 4
total_days = sum(days[:M - 1]) + D - 1

print(weekdays[(w + total_days - 1) % 7])