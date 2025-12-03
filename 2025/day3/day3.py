def get_maximum_voltage(batteries: str, number_of_batteries: int = 2):

    joltage = ""

    for i in range(number_of_batteries):
        batteries_subset = batteries
        left_batteries = number_of_batteries - i - 1

        if left_batteries > 0:
            batteries_subset = batteries[:-(number_of_batteries-i-1)]

        number = max(batteries_subset)
        number_idx = batteries.index(number)
        batteries = batteries[number_idx + 1:]
        joltage += number

    return int(joltage)


with open("input.txt", "r") as f:
    input_list = [line.strip() for line in f.readlines()]

# Part 1
max_voltages = [get_maximum_voltage(batteries, 2) for batteries in input_list]
print("Part 1:", sum(max_voltages))

# Part 2
max_voltages = [get_maximum_voltage(batteries, 12) for batteries in input_list]
print("Part 2:", sum(max_voltages))
