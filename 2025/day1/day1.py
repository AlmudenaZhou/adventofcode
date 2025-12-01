# Part 1
def calc_sequence_part1(input_list: list[str]):

    zero_occcurrences = 0
    current_point = 50

    for input_count in input_list:
        direction = input_count[0]
        number = int(input_count[1:])
        if direction == "R":
            current_point += number
        elif direction == "L":
            current_point -= number

        current_point %= 100
        if current_point == 0:
            zero_occcurrences += 1
    return zero_occcurrences


# Part 2
def calc_sequence_part2(input_list: list[str]):

    zero_occcurrences = 0
    current_point = 50
    point_list = [current_point]

    for input_count in input_list:
        direction = input_count[0]
        number = int(input_count[1:])

        zero_occcurrences += number // 100
        number %= 100
        if direction == "R":
            current_point += number
        elif direction == "L":
            current_point -= number

        if (current_point == 0 or current_point == 100) and point_list[-1] != 0:
            zero_occcurrences += 1
        elif current_point < 0 and point_list[-1] > 0:
            zero_occcurrences += 1
        elif current_point > 100:
            zero_occcurrences += 1
        current_point %= 100
        # print(input_count, current_point, point_list[-1], zero_occcurrences)
        point_list.append(current_point)
    return zero_occcurrences, point_list


with open("input.txt", "r") as f:
    input_list = [line.strip() for line in f.readlines()]

zero_occurrence_p1 = calc_sequence_part1(input_list)
zero_occurrence_p2, point_list = calc_sequence_part2(input_list)

print("Part 1: ", zero_occurrence_p1)
print("Part 2: ", zero_occurrence_p2)
