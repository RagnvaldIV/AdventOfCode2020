inputTxt = open("Day 7/input.txt", "r")
rules = inputTxt.readlines()
myBag = "shiny gold"

def getChildren(bag):
    childrenCount = 1
    for rule in rules:
        if rule.startswith(bag):
            if rule.count("no other bag"):
                return childrenCount
            childList = rule.split("contain ")[1].split(", ")
            for child in childList:
                count = int(child[0])
                child = child[2:len(child)].split(" bag")[0]
                childrenCount += count * getChildren(child)
    return childrenCount

# Use recursive function, -1 because we aren't counting the initial shiny gold bag
print(getChildren(myBag) - 1)