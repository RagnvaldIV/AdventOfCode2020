inputTxt = open("Day 5/input.txt", "r")
seats = inputTxt.readlines()
seatIds = []

for seat in seats:
    row = 0
    col = 0
    for rowBit in range(0,7):
        if seat[rowBit] == 'B':
            row += pow(2,6-rowBit)
    for colBit in range(0,3):
        if seat[colBit + 7] == 'R':
            col += pow(2,2-colBit)
    seatIds.append(row * 8 + col)

seatIds.sort()

# Find 1-seat gap in sorted list
for id in range(0,len(seatIds)-1):
    if seatIds[id] == (seatIds[id + 1] - 2):
        print(seatIds[id] + 1)
