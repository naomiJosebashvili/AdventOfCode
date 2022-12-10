# Part 1:
# Finds the highest total number of calories carried by an Elf

file = open("day1InputFile.txt", "r")

arrayTotalElfCalories = []
totalCalories = 0

for line in file:
	if line != "\n":
		calories = int(line)
		totalCalories += calories
	else:
		arrayTotalElfCalories.append(totalCalories)
		totalCalories = 0
		
file.close()
	
highestCalories = 0
for elf in arrayTotalElfCalories:
	if elf > highestCalories:
		highestCalories = elf
		
print(highestCalories)


# Part 2:
# Finds the 3 Elves carrying the most calories and sums their loads

file = open("day1InputFile.txt", "r")

arrayTotalElfCalories = []
totalCalories = 0

for line in file:
	if line != "\n":
		calories = int(line)
		totalCalories += calories
	else:
		arrayTotalElfCalories.append(totalCalories)
		totalCalories = 0
		
file.close()
	
arrayTotalElfCalories.sort()
print(arrayTotalElfCalories[-1] + arrayTotalElfCalories[-2] + arrayTotalElfCalories[-3])
