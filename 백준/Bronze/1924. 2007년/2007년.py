month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekdays = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
x, y = map(int, input().split())
days = sum(month[:x-1]) + y-1
print(weekdays[days%7])