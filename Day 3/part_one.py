def getInput():
	with open("Day 3\input.txt", "r") as file:
		data = file.readlines()
		for i in range(len(data)):
			data[i] = data[i].strip("\n") 
	return data

def move(toMoveX, toMoveY):
	editedInput = getInput()[::toMoveY]
	currentIndex = 0
	trees = 0
	for row in editedInput:
		rowLenght = len(editedInput[0]) 
		if row[currentIndex % rowLenght] == "#":
			editedRow = list(row)
			editedRow[currentIndex % rowLenght] = "X"
			#print("".join(editedRow))	
			trees += 1
		currentIndex += toMoveX
	return trees

print(move(3, 1))

