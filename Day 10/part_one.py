with open("Day 10\input.txt", "r") as file:
    data = file.read().split("\n")
    input_ = []
    for i in data:
        input_.append(int(i))
    data = sorted(input_)

def getAnswer():
    oneDifferences = [0]
    threeDifferences = [3]
    for i in range(len(data)-1):
        if data[i+1] - data[i] == 3:
            threeDifferences.append(data[i])
        elif data[i+1] - data[i] == 1:
            oneDifferences.append(data[i])
    return (len(oneDifferences) * len(threeDifferences))
    
print("Part 1 answer:", getAnswer())