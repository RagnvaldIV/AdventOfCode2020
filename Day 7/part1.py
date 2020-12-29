inputTxt = open("Day 7/input.txt", "r")
rules = inputTxt.readlines()
myBag = "shiny gold"
parents = set()

def addParents(bag):
    for rule in rules:
        if rule.count(bag) and not rule.startswith(bag):
            parent = rule.split(" bags")[0]
            parents.add(parent)
            addParents(parent)

addParents(myBag)
print(len(parents))
