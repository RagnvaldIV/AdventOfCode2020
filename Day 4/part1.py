inputTxt = open("Day 4/input.txt", "r")
ppCount = 1 # Not sure why but I'm missing the last line
# ppFields = []
ppValidFields = 0
binFields = 0

# Uncomment below to count total passports

# lines = 1
# for line in inputTxt.readlines():
#     if len(line) == 1:
#         lines += 1
# print("Total: " + str(lines))
# inputTxt.seek(0,0)

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


for line in inputTxt.readlines():
    if line[0] != '\n':
        # line has text, split and add to fields
        fields = line.split()
        for field in fields:
            # Convert to binary to check
            binFields = binaryRepresentation(field[0:3], binFields)
            # Simply don't check for cid, other 7 must be fulfilled
            if field[0:3] != 'cid':
                # ppFields.append(field)
                ppValidFields += 1
    else:
        # Check if this last passport was valid, reset array
        if ppValidFields == 7:
            print(format(binFields, 'b').zfill(8))
            ppCount += 1
        else:
            print(format(binFields, 'b').zfill(8) + "<------ INVALID")
        # ppFields.clear()
        binFields = 0
        ppValidFields = 0

print("Valid: " + str(ppCount))