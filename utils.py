import datetime
from config import *

# returns current time like 12:34:56 with the offset in seconds
def get_time(offset=0):
    is24hr = use24HourTime
    now = datetime.datetime.now() + datetime.timedelta(seconds=offset) # gets current time and adds the offset in seconds
    if is24hr == True:
        formatted_time = now.strftime("%H:%M:%S")
        return formatted_time
    formatted_time = now.strftime("%I:%M:%S %p")
    return formatted_time # format and return