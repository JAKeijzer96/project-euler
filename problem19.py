'''
27/04/2020

You are given the following information, but you may prefer to do some research for yourself.

   - 1 Jan 1900 was a Monday.
   - Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
   - A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

'''

# Leap year occurs every 4 years, since 2000 is divisible by 400
# January through december have [31, 28+1, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] days
# +21 days is always possible to end up at the same day of the week in the same month

week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sundays = 0

for year in range(1900, 2001): # for every year 1900 up to and including 2000
    months[1] = 29 if year % 4 == 0 else 28
    for month in range(12): # for month index 0 to 11
        for day in range(1, months[month]+1): # for every day of the month
            current_day = week[0]
            week.pop(0)
            week.append(current_day)
            if day >= 8 and day <= 21: # partly skip through the month
                continue
            # We start at 01/01/1900 to cycle through the weekdays, but we only
            # start counting at 01/01/1901
            if year > 1900 and day == 1 and current_day == 'sunday': # if the first day is a sunday
                sundays += 1

print(sundays)