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
    if hours >= 1:
        hours = int(hours)
        seconds = seconds - (secondsInHour*hours)
    else:
        hours = 00

    minutes = seconds / secondsInMinute
    if minutes >= 1:
        minutes = int(minutes)
        seconds = seconds - (secondsInMinute*minutes)
    else:
        minutes = 00

    seconds = int(seconds)

    secondString = ""
    minuteString = ""
    hourString = ""

    if hours > 0 and hours < 10:
        hourString = "0" + str(hours)
    elif hours == 0:
        hourString = "00"
    else:
        hourString = str(hours)

    if minutes > 0 and minutes < 10:
        minuteString = "0" + str(minutes)
    elif minutes == 0:
        minuteString = "00"
    else:
        minuteString = str(minutes)

    if seconds > 0 and seconds < 10:
        secondString = "0" + str(seconds)
    elif seconds == 0:
        secondString = "00"
    else:
        secondString = str(seconds)

    return hourString + ":" + minuteString + ":" + secondString

# self.assert_equal(make_readable(0), "00:00:00")
# self.assert_equal(make_readable(5), "00:00:05")
# self.assert_equal(make_readable(60), "00:01:00")
# self.assert_equal(make_readable(86399), "23:59:59")
# self.assert_equal(make_readable(359999), "99:59:59")
