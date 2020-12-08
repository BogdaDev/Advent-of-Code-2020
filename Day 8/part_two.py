from copy import deepcopy

data = []
with open("Day 8\input.txt", "r") as f:
	for line in f:
		line = line.strip().rstrip('.')
		data.append(line)


def getAnswer(lines):
	accumulator = 0
	maxIndex = len(lines)
	seenIndexes = set()
	currentIndex = 0
	while True:
		if currentIndex == maxIndex:
			return accumulator
		
		if currentIndex in seenIndexes:
			return None

		seenIndexes.add(currentIndex)

		instruction = lines[currentIndex].split(" ")

		if instruction[0] == 'acc':
			accumulator += int(instruction[1])
			currentIndex += 1
		
		elif instruction[0] == 'jmp':
			currentIndex += int(instruction[1])
		
		elif instruction[0] == 'nop':
			currentIndex += 1

for i in range(len(data)):
	deepCopy = deepcopy(data)
	if data[i].startswith("nop"):
		deepCopy[i] = data[i].replace("nop", "jmp")
	elif data[i].startswith("jmp"):
		deepCopy[i] = data[i].replace("jmp", "nop")
	answer = getAnswer(deepCopy)
	if answer:
		print("Part 2 answer: {}".format(answer))
		break