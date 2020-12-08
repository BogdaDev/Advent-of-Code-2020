from math import ceil, floor
def getInput():
    with open('Day 5\input.txt', 'r') as file:
        input_ = file.readlines()
    return input_
def getSeatID(seat):
    currentRow, currentColumn = [0, 127], [0, 7]
    for i in seat:
        if i == 'F':
            currentRow[1] = floor(currentRow[1] - (currentRow[1]-currentRow[0])/2)
        elif i == 'B':
            currentRow[0] = ceil((currentRow[0] + (currentRow[1]-currentRow[0])/2))
        elif i == 'L':
            currentColumn[1] = floor(currentColumn[1] - (currentColumn[1]-currentColumn[0])/2)
        elif i == 'R':
            currentColumn[0] = ceil((currentColumn[0] + (currentColumn[1]-currentColumn[0])/2))
    return (currentRow[1] * 8) + currentColumn[1]
seatsIDs = []
for i in getInput():
    seatsIDs.append(getSeatID(i))
def getMissingSeat(seats):
    for i in range(len(seats)):
        if i > min(seats):
            if i not in seats:
                return i
print("part 2 answer: ", getMissingSeat(seatsIDs))