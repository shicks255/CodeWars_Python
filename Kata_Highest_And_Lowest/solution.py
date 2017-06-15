#! python3

# In this little assignment you are given a string of space separated numbers,
# and have to return the highest and lowest number.

# Example:

# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"


def high_and_low(numbers):
    newNumbers = numbers.split()
    lowest = 0
    highest = 0
    for num in newNumbers:
        if int(num) < lowest or lowest == 0:
            lowest = int(num)

        if int(num) > highest or highest == 0:
            highest = int(num)

    numbers = str(highest) + ' ' + str(lowest)
    return numbers

print(high_and_low("1 2 -11 2 3 4 5"))
