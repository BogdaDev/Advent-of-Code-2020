def getInput():
    with open("Day 9\input.txt", "r") as file:
        data = file.read().split("\n")
        input_ = []
        for i in data:
            input_.append(int(i))
    return input_

def getAnswer():
    currentNumber = 25
    data = getInput()
    for i in range(len(data)):
        currentNumber += 1
        set_ = set(data[currentNumber - 25 : currentNumber])
        for item in data[currentNumber - 25 : currentNumber]:
            if data[currentNumber] - item in set_:
                break
        else:
            return data[currentNumber]

print("Part 1 answer is:", getAnswer())
            