input = []

with open("Day 1\input.txt", "r") as file:
    input = file.readlines()
    for i in range(len(input)):
        input[i] = int(input[i].replace("\n", "")) 

def checkForYear(input):  
    for i in input: 
        for x in input:  
            if i + x == 2020: 
                return i * x 

print(checkForYear(input)) 

