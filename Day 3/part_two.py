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
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
answers = []
for i in slopes:
	answers.append(move(i[0], i[1]))
answer = answers[0]
for i in answers[1:]:
	answer *= i

print(answer)
