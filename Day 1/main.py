# Open file and set up vars
inputTxt = open("Day 1/input.txt", "r")
years = []
imported = 0


# Define function to check each number in array against all others
def doMath():
    for num1 in years:
        for num2 in years:
            if((num1 + num2) == 2020):
                product = num1 * num2
                print("2020 found, answer: " + str(product))
                return

# Import all years into array
while imported == 0:
    line1 = inputTxt.readline()
    if(len(line1) > 0):
        years.append(int(line1))
    else:
        imported = 1
print("Years imported: " + str(len(years)))

# Call the math function
doMath()