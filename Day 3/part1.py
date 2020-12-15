# Open file and set up vars
inputTxt = open("Day 3/input.txt", "r")

lineLength = 31
numOfLines = 323
slope = [[0 for i in range(lineLength)] for j in range(numOfLines)] 

position = 0
travel = 3
treeCount = 0

# Import input as array
for row in range(numOfLines):
    line = inputTxt.readline()
    # print(line)
    for i in range(lineLength):
        slope[row][i] = line[i]

# Iterate through rows, moving position
for row in range(numOfLines):
    if(slope[row][position%lineLength] == '#'):
        treeCount += 1
    position += travel

print("Answer is " + str(treeCount))