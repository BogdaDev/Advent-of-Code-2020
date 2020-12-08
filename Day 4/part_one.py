import re

def getInput():
    thing = []
    toReturn = []
    with open('input.txt', 'r') as file:
        text = file.read()
        text = text.split('\n')
        for i in range(len(text)):
            if not ":" in text[i] or i == len(text)-1:
                toReturn.append(thing)
                thing = []
            else:
                thing.append(text[i])
        return toReturn

def getPassportsDict():
    dict_ = {
    }
    input_ = getInput()
    for i in range(len(input_)):
        thing = []
        for x in " ".join(input_[i]).split(" "):
            thing.append(x)
        d = {
        }    
        for z in thing:
            u = z.split(':')   
            d.update({
                u[0]: u[1]
            })
        dict_.update({
            str(i): d
        })
    return dict_

def verifyPassports():
    dict_ = getPassportsDict()
    amountOfValidPassports = 1
    verify = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for i in range(len(dict_)):
        passport = dict_[str(i)]
        if "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport:
            amountOfValidPassports += 1
    return amountOfValidPassports   

print("Part 1 answer: ", verifyPassports())