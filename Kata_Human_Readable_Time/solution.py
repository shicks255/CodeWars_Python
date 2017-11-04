# python! #

# Write a function, which takes a non-negative integer (seconds) as input and
# returns the time in a human-readable format (HH:MM:SS)
#
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)
#
# You can find some examples in the test fixtures.


def make_readable(seconds):
    secondsInHour = 60 * 60
    secondsInMinute = 60

    hours = seconds / secondsInHour
    hours = int(hours)
    seconds = seconds - (secondsInHour*hours)

    minutes = seconds / secondsInMinute
    minutes = int(minutes)
    seconds = seconds - (secondsInMinute*minutes)

    seconds = int(seconds)

    secondString = str(format(seconds, '02d'))
    minuteString = str(format(minutes, '02d'))
    hourString = str(format(hours, '02d'))

    return hourString + ":" + minuteString + ":" + secondString

