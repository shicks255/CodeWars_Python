#! python3

# Make a program that filters a list of strings and returns a list with only your friends name in it.

# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours!

# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

def friend(x):
    friends = []
    for name in x:
        if len(name) == 4:
            friends.append(name)

    return friends


print(friend(["Kieren", "Ryan", "Kieran", "Jason", "Yous"]))