# Part 1:
# Finding the common item between both compartments of each backpack, and outputting the sum of their priorities

file = open("day3InputFile.txt", "r")
totalPriorities = 0
itemPriority = [0,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

for backpack in file:
    halfLength = len(backpack) // 2
    compartment1 = backpack[:halfLength]
    compartment2 = backpack[halfLength:]
    flag = False
    
    for item1 in compartment1:
        if flag == True:
            break
        for item2 in compartment2:
            if item1 == item2:
                totalPriorities += itemPriority.index(item1)
                flag = True
                break
                
file.close()
print(totalPriorities)


# Part 2:
# Finding the common item between every 3 backpacks, and outputting the sum of their priorities

file = open("day3InputFile.txt", "r")
totalPriorities = 0
itemPriority = [0,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
b1 = b2 = b3 = ""

for backpack in file:
    # Removes '\n'
    backpack = backpack[:-1]
    if b1 == "":
        b1 = backpack
    elif b2 == "":
        b2 = backpack
    elif b3 == "":
        b3 = backpack
        
        for item1 in b1:
            if item1 not in b2 or item1 not in b3:
                b1 = b1.replace(item1, "")
        totalPriorities += itemPriority.index(b1[0])
        b1 = b2 = b3 = ""
        
file.close()
print(totalPriorities)
