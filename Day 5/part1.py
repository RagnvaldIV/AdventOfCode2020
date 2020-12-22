inputTxt = open("Day 5/input.txt", "r")
seats = inputTxt.readlines()
maxSeatId = 0

for seat in seats:
    row = 0
    col = 0
    # Convert row to binary
    for rowBit in range(0,7):
        if seat[rowBit] == 'B':
            row += pow(2,6-rowBit)
    # Same for column
    for colBit in range(0,3):
        if seat[colBit + 7] == 'R':
            col += pow(2,2-colBit)
    # Calculate seat ID and store if max
    seatId = row * 8 + col
    maxSeatId = seatId if seatId > maxSeatId else maxSeatId

print(maxSeatId)