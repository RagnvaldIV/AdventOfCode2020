# Open file and set up vars
inputTxt = open("Day 2/input.txt", "r")
goodPass = 0

# Scan through lines and add to count if it fits
for line in inputTxt:
    pos1 = int(line.split('-')[0]) - 1
    line2 = line.split('-')[1]
    pos2 = int(line2.split(' ')[0]) - 1
    line2 = line2.split(' ', 1)[1]
    letter = line2[0]
    password = line2[3:len(line2)]
    match1 = password[pos1] == letter
    match2 = password[pos2] == letter

    # Pesky python with no XOR
    if((match1 and not match2) or (not match1 and match2)):
        goodPass += 1
        print(line)


    # print(password)
print(goodPass)