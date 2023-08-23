# 1. Get the current day, month, year, hour, minute and timestamp from datetime module
# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
# 3. Today is 5 December, 2019. Change this time string to time.
# 4. Calculate the time difference between now and new year.
# 5. Calculate the time difference between 1 January 1970 and now.
# 6. Think, what can you use the datetime module for? Examples:
#       Time series analysis
#       To get a timestamp of any activities in an application
#       Adding posts on a blog

from datetime import datetime,timedelta,date

#1.
print("EJERCICIO 1\n")

current_datetime = datetime.now()
print(current_datetime)
day = current_datetime.day
print(day)
hour = current_datetime.hour
print(hour)
minute = current_datetime.minute
print(minute)
seconds = current_datetime.second
print(seconds)
timestamp = datetime.timestamp(current_datetime)
print(timestamp)

#2.
print("\nEJERCICIO 2\n")

current_date = datetime.now()
now = current_date.strftime("%m/%d/%Y, %H,%M,%S")
print("t", now)

#3.
print("\nEJERCICIO 3\n")

date_str = "5 December, 2019"
date_time = datetime.strptime(date_str, "%d %B, %Y")
print("Today is ", date_time)

#4.
print("\nEJERCICIO 4\n")

now = datetime.now()
new_year = datetime(2024,1,1)
difference = new_year - now
print(difference)

#5.
print("\nEJERCICIO 5\n")

now = datetime.now()
now_timestamp = datetime.timestamp(now)
print(now_timestamp)

