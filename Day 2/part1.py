# Open file and set up vars
inputTxt = open("Day 2/input.txt", "r")
goodPass = 0

# Scan through lines and add to count if it fits
for line in inputTxt:
    min = int(line.split('-')[0])
    line2 = line.split('-')[1]
    max = int(line2.split(' ')[0])
    line2 = line2.split(' ', 1)[1]
    letter = line2[0]
    password = line2[3:len(line2)]
    count = password.count(letter)

    if(count >= min and count <= max):
        goodPass += 1
        print(line)


    # print(password)
print(goodPass)