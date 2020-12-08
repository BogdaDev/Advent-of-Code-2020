def get_input():
  with open("Day 7\input.txt", "r") as file:
    data = file.read().split("\n")
  return data

def get_bags(color):
    data = get_input()
    lines = []
    for i in data:
        if color in i and i.index(color) != 0:
            lines.append(i)
    
    allColors = []

    if len(lines) == 0:
        return []
    else:
        colors = []
        for line in lines:
            colors.append(line[:line.index("bags")-1])
        for color in colors:
            if color in allColors:
                colors.remove(color)
        for color in colors:
            allColors.append(color)
            bags = get_bags(color)

            allColors += bags

        uniqueColors = []

        for color in allColors:
            if color not in uniqueColors:
                uniqueColors.append(color)
        return uniqueColors
    

print(len(get_bags("shiny gold")))
    


