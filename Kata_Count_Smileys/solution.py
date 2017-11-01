#! python3

# Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.
#
# Rules for a smiling face:
# -Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# -A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# -Every smiling face must have a smiling mouth that should be marked with either ) or D.
# No additional characters are allowed except for those mentioned.
#     Valid smiley face examples:
# :) :D ;-D :~)
# Invalid smiley faces:
# ;( :> :} :]
#
# Example cases:
#
# countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
# countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
# countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;


# class CountSmileys:
def count_smileys(arr):
    if len(arr) == 0:
        return 0
    numberOfSmileys = 0
    for item in arr:
        length = len(item)
        if item[0] == ';' or item[0] == ':':
            if item[length-1] == ')' or item[length-1] == 'D':
                if length == 3 and (item[1] == '-' or item[1] == '~'):
                    numberOfSmileys = numberOfSmileys+1
                if length == 2:
                    numberOfSmileys = numberOfSmileys+1
    return numberOfSmileys


