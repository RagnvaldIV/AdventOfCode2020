# WARNING:  Because we check for an empty line with '\n' to count the 
#           group, add 2 empty lines at the end of the input file
inputTxt = open("Day 6/input.txt", "r")
answers = inputTxt.readlines()
thisGroup = set()
totalAnswers = 0

# Iterate through lines, adding questions to set
for answer in answers:
    if answer[0] != '\n':
        for question in range(0,len(answer) - 1):
            thisGroup.add(answer[question])
    else:
        # End of group, add questions to total and clear group set
        totalAnswers += len(thisGroup)
        thisGroup.clear()

print(totalAnswers)