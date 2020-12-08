def get_input():
    with open('Day 6\input.txt', 'r') as file:
        read_file = file.read()
        data = read_file.split('\n\n')
    return data

def get_answer():
    total_sum = 0

    for group in get_input():
        groups = []

        for set_group in group.split('\n'):
            groups.append(set(set_group))

        total_sum += len(set.intersection(*groups))
    print("Answer for part 2: " + str(total_sum))

get_answer()