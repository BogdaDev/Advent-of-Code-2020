with open("Day 10\input.txt", "r") as file:
    data = file.read().split("\n")
    input_ = []
    for i in data:
        input_.append(int(i))
    data = sorted(input_)

def countOptions(index, nodes, lookup):
    result = 0
    toVisit = []
    if index not in lookup:
        for i in range(index + 1, index + 4):
            if i < len(nodes):
                if nodes[i] - nodes[index] in (1, 2, 3):
                    toVisit.append(i)
            else:
                break
        if toVisit:
            for indexTwo in toVisit:
                result += countOptions(indexTwo, nodes, lookup)
                lookup[index] = result
        else:
            return 1
    return lookup[index]

print("Part 2 answer:", countOptions(0, data, {}))
