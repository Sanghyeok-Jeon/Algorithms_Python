def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    
    return False

def days_in_month(month, leap_year):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year:
        month_days[1]= 29
        
    return month_days[month - 1]

def calculate_day_of_year(day, month, year, hour, minute):
    leap_year = is_leap_year(year)
    day_of_year = 0
    for m in range(1, month):
        day_of_year += days_in_month(m, leap_year)
        
    day_of_year += day - 1
    day_of_year += (hour * 60 + minute) / (24 * 60)
    
    return day_of_year

def calculate_percentage(day_of_year, year):
    total_days = 366 if is_leap_year(year) else 365
    
    return (day_of_year / total_days) * 100

import datetime

input_date = input().strip()
date_object = datetime.datetime.strptime(input_date, "%B %d, %Y %H:%M")

day = date_object.day
month = date_object.month
year = date_object.year
hour = date_object.hour
minute = date_object.minute

day_of_year = calculate_day_of_year(day, month, year, hour, minute)
percentage = calculate_percentage(day_of_year, year)

print(f"{percentage:.9f}")
