# Solution-1

# from datetime import datetime

# date = "Oct 14 1999 9:50 PM"
# print(type(date))

# date_time = datetime.strptime(date,"%b %d %Y %I:%M%p")
# print(date_time)

# Solution-2

from dateutil import parser

date_time = parser.parse("Oct 14 1999 9:50 PM")
print(date_time)