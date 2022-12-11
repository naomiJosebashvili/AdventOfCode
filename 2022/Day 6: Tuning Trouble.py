# Part 1:
# Finds the first 4 consecutive characters that are unique

file = open("day6InputFile.txt", "r")

stringOfCharacters = file.readline()
flag = False

for x in range(3, len(stringOfCharacters)):
    if flag == False:
        listOfLast4Characters = [stringOfCharacters[x-3], stringOfCharacters[x-2], stringOfCharacters[x-1], stringOfCharacters[x]]
        setOfLast4Characters = set(listOfLast4Characters)
        #print(listOfLast4Characters)
        #print(setOfLast4Characters)
        if len(setOfLast4Characters) == 4:
            print(x+1)
            flag = True
            
file.close()


# Part 2:
# Finds the first 14 consecutive characters that are unique

file = open("day6InputFile.txt", "r")

stringOfCharacters = file.readline()
flag = False

for x in range(13, len(stringOfCharacters)):
    if flag == False:
        listOfLast4Characters = []
        for y in reversed(range(14)):
            listOfLast4Characters.append(stringOfCharacters[x-y])
        setOfLast4Characters = set(listOfLast4Characters)
        #print(listOfLast4Characters)
        #print(setOfLast4Characters)
        if len(setOfLast4Characters) == 14:
            print(x+1)
            flag = True
            
file.close()
