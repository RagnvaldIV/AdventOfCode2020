nums = open("Day 9/input.txt", "r").readlines()

preambleLength = 25
invalid = 542529149 # Answer from part 1

# Compute sum starting from this line, prints sum of largest and smallest in set
def sumFrom(line):
    summ = int(nums[line])
    smol = summ
    larg = summ
    while summ < invalid:
        line += 1
        num = int(nums[line])
        smol = num if num < smol else smol
        larg = num if num > larg else larg
        summ += num
        if summ == invalid:
            print(smol + larg)
            return True
    return False

# Iterate and break at first false
for line in range(0, len(nums)):
    if sumFrom(line):
        break
