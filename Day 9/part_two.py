def getInput():
	with open("Day 9\input.txt", "r") as file:
		data = file.read().split("\n")
		input_ = []
		for i in data:
			input_.append(int(i))
		return input_

def getAnswer():
	data = getInput()
	currentNumber = 25
	for i in range(len(data)):
		currentNumber += 1
		set_ = set(data[currentNumber - 25 : currentNumber])
		for item in data[currentNumber - 25 : currentNumber]:
			if data[currentNumber] - item in set_:
				break
		else:
			for length in range(2, len(data)):
				for x in range(len(data) - length):
					row = sorted(data[x : x + length])
					if sum(row) == data[currentNumber]:
						return row[0] + row[-1]

print("Part 2 answer: ", getAnswer())