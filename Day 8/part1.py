ops = open("Day 8/input.txt", "r").readlines()

seenLines = set()
line = 0
accumulator = 0

# Effect op on line and return next line/jump
def lineOp(line):
    seenLines.add(line)
    lineOp = ops[line]
    op = lineOp[0:3]
    if op == 'jmp':
        arg = int(lineOp[3:len(lineOp)])
        return line + arg
    elif op == 'acc':
        global accumulator
        arg = int(lineOp[3:len(lineOp)])
        accumulator += arg
    return line + 1

# Run until we see any line a 2nd time
while line not in seenLines:
    line = lineOp(line)

print(accumulator)
