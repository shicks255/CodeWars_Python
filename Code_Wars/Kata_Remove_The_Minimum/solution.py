#! python3

# Given an array of integers, remove the smallest value.
# Do not mutate the original array/list.
# If there are multiple elements with the same value, remove the one with a lower index.
# If you get an empty array/list, return an empty array/list.

# Don't change the order of the elements that are left.

def remove_smallest2(numbers):
    if len(numbers) == 0:
        return []
    min = None
    for i,x in enumerate(numbers):
        if min is None or x < numbers[min]:
            min = i;

    newList = numbers[:]
    newList.pop(min)
    return newList

# doesnt work, removes ALL smallest items
def remove_smallest(numbers):
    return [item for item in numbers if min(numbers) != item]

def remove_smallest3(numbers):
    if len(numbers) == 0:
        return []
    mini = numbers.index(min(numbers))
    return numbers[0:mini] + numbers[mini+1:]

print(remove_smallest3([2,1,5,3,1]))