# ! python3

# You have a sequence of positive numbers starting with 1, but one number is missing!
#
# Find out the missing number; if the sequence is not broken, you should return 0. Each sequence always increments by 1.
#
# In short: an invalid sequence (a string with non numeric character) must return 1,
# an already complete (or empty) sequence must return 0; a broken sequence with more than one number missing should
# return the lowest missing number; otherwise return the missing number.
#
# Note that the input may be with random order.

# find_missing_number("1 3 2 5") # returns 4, because 4 is missing
# find_missing_number("1 2 3 4") # returns 0, because the sequence isn't broken
# find_missing_number("1 5") # returns 2, because the sequence is missing more than one number and 2 is the lowest between 2, 3 and 4
# find_missing_number("2 1 4 3 a") # returns 1, because it's an invalid sequence. in this case, it's invalid because contain a non numerical character


def find_missing_number(numberString):
    numbers = numberString.split()
    realNumbers = []
    for number in numbers:
        if not number.isdigit():
            return 1
        realNumbers.append(int(number))
    realNumbers.sort()

    # empty
    if len(realNumbers) == 0:
        return 0
    start = realNumbers[0]

    # doesnt start with 1
    if realNumbers[0] != 1:
        return 1

    missingNumberArray = []
    for number in realNumbers:
        if int(number) != start:
            missingNumberArray.append(start)
        start = number+1

    if len(missingNumberArray) > 0:
        if len(missingNumberArray) == 1:
            return missingNumberArray[0]
        else:
            return 2

    return 0
