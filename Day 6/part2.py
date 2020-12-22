# WARNING:  Because we check for an empty line with '\n' to count the 
#           group, add 2 empty lines at the end of the input file
inputTxt = open("Day 6/input.txt", "r")
answers = inputTxt.readlines()

# Init group with all possible questions since we're intersect-updating
thisGroup = {
        'a', 'b', 'c', 'd', 'e', 'f',
        'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r',
        's', 't', 'u', 'v', 'w', 'x',
        'y', 'z'
    }
totalAnswers = 0

# Iterate through lines, adding questions to set
for answer in answers:
    if answer[0] != '\n':
        # Build a set for each person and intersect with group
        thisPerson = set()
        for question in range(0,len(answer) - 1):
            thisPerson.add(answer[question])
        thisGroup.intersection_update(thisPerson)
    else:
        # End of group, add questions to total and reset group set
        totalAnswers += len(thisGroup)
        thisGroup = {
            'a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x',
            'y', 'z'
        }

print(totalAnswers)