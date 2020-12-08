def getInput():
    input_ = []
    with open('Day 6\input.txt', 'r') as file:
        arr = []
        lines = file.readlines()
        for i in range(len(lines)):
            if lines[i] == "\n":
                input_.append(arr)
                arr = []
            elif i == len(lines)-1:
                arr.append(lines[len(lines)-1])
                input_.append(arr)
                arr = []
            else:
                arr.append(lines[i].strip('\n'))
        return input_
def answers():
    data = getInput()
    answers = []
    e = 0
    repetitiveChars = []
    for i in data:
        currentArray = []
        repetitiveChars = []
        str_ = "".join(i)
        if len(i) != 1:
            for x in str_:
                if x not in repetitiveChars:
                    if str_.count(x) > 1:
                        repetitiveChars.append(x)
            answers.append(len(repetitiveChars)-1)
        else:
            answers.append(len("".join(i)))
    sum = 0
    print(answers)
    for i in answers:
        sum += i
    print(sum)
answers()
I have to fix this