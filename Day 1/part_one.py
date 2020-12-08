input = [] #Defining an array called input. So I can loop something.

# Getting the input array.
with open("Day 1\input.txt", "r") as file:
    input = file.readlines()
    for i in range(len(input)):
        input[i] = int(input[i].replace("\n", "")) 


#A function that is going to return a number.
def checkForYear(input):  
    for i in input: 
        for x in input:    #Those 2 loops are for getting two numbers and 
            if i + x == 2020: #adding them together and check if they are equal to 2020. 
                return i * x #Multiplying the two numbers together

print(checkForYear(input)) 

