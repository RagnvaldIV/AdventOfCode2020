nums = open("Day 9/input.txt", "r").readlines()

preambleLength = 25

# Check sum of previous 25 regressively, prints result
def sumCheck(line):
    for i in range(1, preambleLength + 1):
        num1 = int(nums[line - i])
        for j in range(i + 1, preambleLength + 1):
            num2 = int(nums[line - j])
            summ = num1 + num2
            # print("lines " + str(line - i) + " (" + str(num1) + ") and " + str(line - j) + " (" + str(num2) + ") sum to " + str(summ))
            if int(nums[line]) == summ:
                return True
    print(nums[line])
    return False

# Start after preamble and break at first false
for line in range(preambleLength, len(nums)):
    if not sumCheck(line):
        break
