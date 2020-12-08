with open("Day 2\input.txt", "r") as file:
    text = file.readlines()
    currentLine = ''
    minAmount = 0
    maxAmount = 0
    validAnswers = 0
    for line in text:
        currentLine = line[:-1]
        currentLine = currentLine.replace(":", "")
        currentLine = currentLine.replace("-", " ")
        currentArray = currentLine.split(" ")
        minAmount, maxAmount = int(currentArray[0]), int(currentArray[1])
        count = currentArray[3].count(currentArray[2])
        if minAmount <= count <= maxAmount:
                validAnswers += 1
    print(validAnswers)
