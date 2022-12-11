# Part 1:
# Finds how many pairs of Elves are assigned to clean sections that overlap entirely

file = open("day4InputFile.txt", "r")
numberOfFullyOverlappedPairs = 0

for pair in file:
    splitPairs = pair.split(",")
    elf1 = splitPairs[0].split("-")
    elf2 = splitPairs[1].split("-")
    elf1LowerBound = int(elf1[0])
    elf1UpperBound = int(elf1[1])
    elf2LowerBound = int(elf2[0])
    elf2UpperBound = int(elf2[1])
    if elf1LowerBound >= elf2LowerBound and elf1UpperBound <= elf2UpperBound or elf1LowerBound <= elf2LowerBound and elf2UpperBound <= elf1UpperBound:
        numberOfFullyOverlappedPairs += 1
        
file.close()
print(numberOfFullyOverlappedPairs)


# Part 2:
# Finds how many pairs of Elves are assigned to clean sections that overlap

def isOverlapping(elf1, elf2):
    elf1LowerBound = int(elf1[0])
    elf1UpperBound = int(elf1[1])
    elf2LowerBound = int(elf2[0])
    elf2UpperBound = int(elf2[1])
    if (elf1LowerBound >= elf2LowerBound and elf1LowerBound <= elf2UpperBound) or (elf1UpperBound >= elf2LowerBound and elf1UpperBound <= elf2UpperBound):
        return True
    return False

file = open("day4InputFile.txt", "r")
numberOfOverlappedPairs = 0
    
for pair in file:
    splitPairs = pair.split(",")
    elf1 = splitPairs[0].split("-")
    elf2 = splitPairs[1].split("-")
    if isOverlapping(elf1, elf2) or isOverlapping(elf2, elf1):
        numberOfOverlappedPairs += 1
        
file.close()
print(numberOfOverlappedPairs)
