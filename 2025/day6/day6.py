def resolve_math_problem_part1(input_list):
    operations = {}

    operands = input_list[-1]

    for row in input_list[:-1]:
        for idx, element in enumerate(row):
            if idx not in operations:
                operations[idx] = element
            else:
                operations[idx] += operands[idx] + element

    results = [eval(operation) for operation in operations.values()]
    return sum(results)


def resolve_math_problem_part2(input_list):
    operands = input_list[-1].split(" ")
    operands = list(filter(lambda x: x.strip() != "", operands))

    operations = {}

    for row in input_list[:-1]:
        for idx, element in enumerate(row):
            if idx not in operations:
                operations[idx] = element
            else:
                operations[idx] += element

    operand_idx = 0

    results = []
    new_operation = ""

    for operation in operations.values():
        operand = operands[operand_idx]
        if operation.strip() == "":
            new_operation = new_operation[:-1]
            results.append(eval(new_operation))
            new_operation = ""
            operand_idx += 1
        else:
            new_operation += operation + operand
    return sum(results)


# Part 1
with open("input.txt", "r") as f:
    input_list = [line.strip().split(" ") for line in f.readlines()]

input_list = [list(filter(lambda x: x.strip() != "", input_l)) for input_l in input_list]
print("Part 1: ", resolve_math_problem_part1(input_list))

# Part 2
with open("input.txt", "r") as f:
    input_list = [line for line in f.readlines()]

print("Part 2: ", resolve_math_problem_part2(input_list))
