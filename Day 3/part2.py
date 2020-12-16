# Open file and set up vars
inputTxt = open("Day 3/input.txt", "r")

# Read over file to get size of array
lineLength = len(inputTxt.readline()) - 1
numOfLines = len(inputTxt.readlines()) + 1
slope = [[0 for i in range(lineLength)] for j in range(numOfLines)] 

position = 0
treeCount = [0, 0, 0, 0, 0]

inputTxt.seek(0, 0)
# Import input as array
for row in range(numOfLines):
    line = inputTxt.readline()
    # print(line)
    for i in range(lineLength):
        slope[row][i] = line[i]

# Iterate through rows, moving position
# r1d1
for row in range(numOfLines):
    if(slope[row][position%lineLength] == '#'):
        treeCount[0] += 1
    position += 1
# r3d1
position = 0
for row in range(numOfLines):
    if(slope[row][position%lineLength] == '#'):
        treeCount[1] += 1
    position += 3
# r5d1
position = 0
for row in range(numOfLines):
    if(slope[row][position%lineLength] == '#'):
        treeCount[2] += 1
    position += 5
# r7d1
position = 0
for row in range(numOfLines):
    if(slope[row][position%lineLength] == '#'):
        treeCount[3] += 1
    position += 7
# r1d2
position = 0
skip = False
for row in range(numOfLines):
    if not skip:
        if(slope[row][position%lineLength] == '#'):
            treeCount[4] += 1
        position += 1
        print(row)
    skip = not skip

result = treeCount[0] * treeCount[1] * treeCount[2] * treeCount[3] * treeCount[4]
print("Each run: " + str(treeCount))
print("Answer is " + str(result))