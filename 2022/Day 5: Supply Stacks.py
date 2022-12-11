# Part 1:
# Finds the top crate in each stack after the moving instructions are executed using LIFO priorities

file = open("day5InputFile.txt", "r")

stackDictionary = {1 : ['B', 'G', 'S', 'C'],
                   2 : ['T', 'M', 'W', 'H', 'J', 'N', 'V', 'G'],
                   3 : ['M', 'Q', 'S'],
                   4 : ['B', 'S', 'L', 'T', 'W', 'N', 'M'],
                   5 : ['J', 'Z', 'F', 'T', 'V', 'G', 'W', 'P'],
                   6 : ['C', 'T', 'B', 'G', 'Q', 'H', 'S'],
                   7 : ['T', 'J', 'P', 'B', 'W'],
                   8 : ['G', 'D', 'C', 'Z', 'F', 'T', 'Q', 'M'],
                   9 : ['N', 'S', 'H', 'B', 'P', 'F']}

for instruction in file:
    splitInstructions = instruction.split(" ")
    numberOfMoves = int(splitInstructions[1])
    fromStack = int(splitInstructions[3])
    toStack = int(splitInstructions[5])
    
    for x in range(numberOfMoves):
        stackDictionary[toStack].append(stackDictionary[fromStack].pop())
        
print(stackDictionary[1][-1] + stackDictionary[2][-1] + stackDictionary[3][-1] + stackDictionary[4][-1] + stackDictionary[5][-1] + stackDictionary[6][-1] + stackDictionary[7][-1] + stackDictionary[8][-1] + stackDictionary[9][-1])

file.close()


# Part 2:
# Finds the top crate in each stack after the moving instructions are executed by moving multiple boxes at a time

file = open("day5InputFile.txt", "r")

stackDictionary = {1 : ['B', 'G', 'S', 'C'],
                   2 : ['T', 'M', 'W', 'H', 'J', 'N', 'V', 'G'],
                   3 : ['M', 'Q', 'S'],
                   4 : ['B', 'S', 'L', 'T', 'W', 'N', 'M'],
                   5 : ['J', 'Z', 'F', 'T', 'V', 'G', 'W', 'P'],
                   6 : ['C', 'T', 'B', 'G', 'Q', 'H', 'S'],
                   7 : ['T', 'J', 'P', 'B', 'W'],
                   8 : ['G', 'D', 'C', 'Z', 'F', 'T', 'Q', 'M'],
                   9 : ['N', 'S', 'H', 'B', 'P', 'F']}

for instruction in file:
    splitInstructions = instruction.split(" ")
    numberOfMoves = int(splitInstructions[1])
    fromStack = int(splitInstructions[3])
    toStack = int(splitInstructions[5])

    stackDictionary[toStack].extend(stackDictionary[fromStack][-numberOfMoves:])
    del stackDictionary[fromStack][-numberOfMoves:]
        
print(stackDictionary[1][-1] + stackDictionary[2][-1] + stackDictionary[3][-1] + stackDictionary[4][-1] + stackDictionary[5][-1] + stackDictionary[6][-1] + stackDictionary[7][-1] + stackDictionary[8][-1] + stackDictionary[9][-1])

file.close()
