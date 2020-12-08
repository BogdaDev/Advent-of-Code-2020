
with open("Day 8\input.txt", "r") as file:
    data = file.read().split("\n")


def getAnswer():
    accumulator = 0
    i = 0
    n = len(data)
    things = []
    while i != n:
        if i+1 not in things:
            #print(i)
            if "acc" in data[i]:
                if data[i].split(" ")[1][0] == "+":
                    accumulator += int(data[i].split(" ")[1][1:]) 
                    i += 1
                else:
                    accumulator -= int(data[i].split(" ")[1][1:]) 
                    i += 1
                things.append(i)
            elif "jmp" in data[i]:
                if data[i].split(" ")[1][0] == "+":
                    i += int(data[i].split(" ")[1][1:])
                else:
                    i -= int(data[i].split(" ")[1][1:]) 
                things.append(i)
            elif "nop" in data[i]:
                i += 1 
                things.append(i)
        else:
            return accumulator
print(getAnswer())