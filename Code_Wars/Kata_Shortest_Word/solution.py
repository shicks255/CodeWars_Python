# ! python3

# x Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.


def find_short(s):
    shortest = ''
    words = s.split()
    for word in words:
        print(shortest)
        if len(word) < len(shortest) or len(shortest) == 0:
            shortest = word

    return len(shortest)


print(find_short('Lets all go on holiday somewhere very cold'))
