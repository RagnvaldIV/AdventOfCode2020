ops = open("Day 8/input.txt", "r").readlines()

seenLines = set()
line = 0
accumulator = 0

# Effect op on line and return next instruction line
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

# Modify line, switching nop and jmp instructions
def modLine(line):
    arg = line[3:len(line)]
    if line[0:3] == 'jmp':
        line = 'nop' + arg
    elif line[0:3] == 'nop':
        line = 'jmp' + arg
    return line

# Iterate through lines, flipping JMP and NOP instructions 1 by 1
for lineNum in range(0,len(ops)-1):
    op = ops[lineNum]
    # Skip this line if ACC instruction
    if op[0:3] == 'acc':
        continue
    # Reset counts
    seenLines.clear()
    accumulator = 0
    line = 0
    ops[lineNum] = modLine(op)
    # Run instructions with this line mod
    while line not in seenLines:
        # Check if program terminates
        if(line >= len(ops)):
            print(accumulator)
            break
        line = lineOp(line)
    # Reset to original
    ops[lineNum] = op
