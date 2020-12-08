with open("Day 2\input.txt", "r") as file:
    text = file.readlines()
    currentLine = ''
    firstIndex = 0
    secondIndex = 0
    validAnswers = 0
    for line in text:
        currentLine = line[:-1]
        currentLine = currentLine.replace(":", "")
        currentLine = currentLine.replace("-", " ")
        currentArray = currentLine.split(" ")
        firstIndex, secondIndex = int(currentArray[0]), int(currentArray[1])
        line = currentArray[3]
        char = currentArray[2]
        if line[firstIndex-1] == char or line[secondIndex-1] == char:
            if not line[firstIndex-1] == char and line[secondIndex-1] == char or not line[secondIndex-1] == char and line[firstIndex-1] == char:
                validAnswers += 1
    print(validAnswers)
