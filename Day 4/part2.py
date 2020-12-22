inputTxt = open("Day 4/input.txt", "r")
ppCount = 1 # Not sure why but I'm missing the last line
ppValidFields = 0
validByr = range(1920, 2002 + 1)
validIyr = range(2010, 2020 + 1)
validEyr = range(2020, 2030 + 1)
validHgtIn = range(59, 76 + 1)
validHgtCm = range(150, 193 + 1)
validEcl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


# Check hexadecimal for hair color
def isHex(s):
    try:
        int(s, 16)
        return 1
    except ValueError:
        return 0


# Essentially a big switch case
def validField(field):
    fieldParts = field.split(':')
    tag = fieldParts[0]
    val = fieldParts[1]
    if (tag == 'byr'):
        if validByr.count(int(val)):
            return 1
    if (tag == 'iyr'):
        if validIyr.count(int(val)):
            return 1
    if (tag == 'eyr'):
        if validEyr.count(int(val)):
            return 1
    if tag == 'hgt':
        if (val[len(val) - 2:len(val)] == 'in'):
            if (len(val) == 4) and validHgtIn.count(int(val[0:2])):
                return 1
        elif (val[len(val) - 2:len(val)] == 'cm'):
            if (len(val) == 5) and validHgtCm.count(int(val[0:3])):
                return 1
    if (tag == 'hcl'):
        if (val[0] == '#'):
            return isHex(val[1:7])
    if (tag == 'ecl'):
        if validEcl.count(val):
            return 1
    if (tag == 'pid'):
        if len(val) == 9:
            return 1
    return 0

# Read through all lines
for line in inputTxt.readlines():
    if line[0] != '\n':
        # line has text, split and add to fields
        fields = line.split()
        for field in fields:
            ppValidFields += validField(field)
    else:
        # Check if this last passport was valid, reset count
        if ppValidFields == 7:
            ppCount += 1
        ppValidFields = 0

print("Valid: " + str(ppCount))