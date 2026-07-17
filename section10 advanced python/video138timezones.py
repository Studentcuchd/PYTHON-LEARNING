#Navie a date and time object that doesnot know about timezones

# A naive datetime has date and time information but no timezone information attached.

from datetime import datetime
print(datetime.now())



# Aware timezone
#now(timezone.utc)

from datetime import datetime,timezone,tzinfo

print(datetime.now(timezone.utc))
print(datetime.now(timezone.utc).tzinfo)

