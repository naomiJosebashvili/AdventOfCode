# Part 1:
# Finds total number of points earned in a repetitive Rock-Paper-Scissors game when following the provided strategy guide

file = open("day2InputFile.txt", "r")
myTotalPoints = 0

for line in file:
    otherPlayersHand = line[0]
    myHand = line[2]
    # Updates points for rounds where user wins
    if otherPlayersHand == "A" and myHand == "Y" or otherPlayersHand == "B" and myHand == "Z" or otherPlayersHand == "C" and myHand == "X":
        myTotalPoints += 6
    # If there is a draw
    elif otherPlayersHand == "A" and myHand == "X" or otherPlayersHand == "B" and myHand == "Y" or otherPlayersHand == "C" and myHand == "Z":
        myTotalPoints += 3
    # If user picked rock
    if myHand == "X":
        myTotalPoints += 1
    # User picked paper
    elif myHand == "Y":
        myTotalPoints += 2
    # User picked scissors
    elif myHand == "Z":
        myTotalPoints += 3
        
file.close()

print(myTotalPoints)


# Part 2:
# Finds total number of points earned in a repetitive Rock-Paper-Scissors game when following the provided strategy guide

file = open("day2InputFile.txt", "r")
myTotalPoints = 0

for line in file:
    otherPlayersHand = line[0]
    roundEnd = line[2]
    # Updates points for rounds where user loses
    if roundEnd == "X":
        if otherPlayersHand == "A":
            myTotalPoints += 3
        elif otherPlayersHand == "B":
            myTotalPoints += 1
        elif otherPlayersHand == "C":
            myTotalPoints += 2
    # If there is a draw
    elif roundEnd == "Y":
        if otherPlayersHand == "A":
            myTotalPoints += 4
        elif otherPlayersHand == "B":
            myTotalPoints += 5
        elif otherPlayersHand == "C":
            myTotalPoints += 6
    # If user wins
    elif roundEnd == "Z":
        if otherPlayersHand == "A":
            myTotalPoints += 8
        elif otherPlayersHand == "B":
            myTotalPoints += 9
        elif otherPlayersHand == "C":
            myTotalPoints += 7

file.close()

print(myTotalPoints)
