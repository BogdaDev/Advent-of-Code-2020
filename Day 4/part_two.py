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
    amountOfValidPassports = 0
    requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for i in range(len(dict_)):
        passport = dict_[str(i)]
        if "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport:
                if 1920 <= int(passport['byr']) <= 2002:
                    if 2010 <= int(passport['iyr']) != 2020:
                        if 2020 <= int(passport['eyr']) <= 2030:
                            if passport['hgt'][len(passport['hgt'])-2:] == "cm" or "in":
                                height = int(passport['hgt'][:-2])
                                if (passport['hgt'][len(passport['hgt'])-2:] == 'cm' and 150 <= height <= 193) or (passport['hgt'][len(passport['hgt'])-2:] == "in" and 59 <= height <= 76):
                                    amountOfValidPassports += 1
    return amountOfValidPassports   

print("Part 2 answer: ", verifyPassports())


        
            