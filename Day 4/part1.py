inputTxt = open("Day 4/input.txt", "r")
ppCount = 0
# ppFields = []
ppValidFields = 0
# binFields = 0



def binaryRepresentation(tag, binFields):
    if tag == 'byr':
        binFields += 128
    if tag == 'iyr':
        binFields += 64
    if tag == 'eyr':
        binFields += 32
    if tag == 'hgt':
        binFields += 16
    if tag == 'hcl':
        binFields += 8
    if tag == 'ecl':
        binFields += 4
    if tag == 'pid':
        binFields += 2
    if tag == 'cid':
        binFields += 1
    return binFields

for line in inputTxt:
    if line[0] != '\n':
        # line has text, split and add to fields
        fields = line.split()
        for field in fields:
            # Convert to binary to check
            # binFields = binaryRepresentation(field[0:3], binFields)
            if field[0] != 'c':
                # ppFields.append(field)
                ppValidFields += 1
    else:
        # Check if this last passport was valid, reset array
        if ppValidFields == 7:
            # print(format(binFields, 'b').zfill(8))
            ppCount += 1
        # else:
            # print(format(binFields, 'b').zfill(8) + "<------ INVALID")
        # ppFields.clear()
        binFields = 0
        ppValidFields = 0

print(ppCount)