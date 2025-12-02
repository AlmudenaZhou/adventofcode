# Part 1

def get_invalid_codes_part1(code_number_len: int):
    if code_number_len % 2 == 0:
        n = code_number_len // 2
        for number in range(10**(n-1), 10**n):
            number_str = str(number)
            repeated_number = number_str + number_str
            yield repeated_number


def part1_main(input_str):
    input_list = input_str.split(',')
    invalid_numbers = []
    for input_ind in input_list:
        start, end = input_ind.split('-')
        code_number_len = len(start)
        if len(start) != len(end):
            print(f"Start and end have different lengths. {start}, {end}")
            if len(start) + 1 == len(end):
                code_number_len = len(start) if code_number_len % 2 == 0 else len(end)
            else:
                print(f"Error: start and end have lengths differing by more than 1. {start}, {end}")
        for invalid_code in get_invalid_codes_part1(code_number_len):
            if int(start) <= int(invalid_code) <= int(end):
                invalid_numbers.append(int(invalid_code))
    return invalid_numbers


# Part 2

def get_invalid_codes_part2(code_number_len: int):
    n_comb = code_number_len // 2

    for n in range(1, n_comb + 1):
        if code_number_len % n != 0:
            continue

        repetition_times = code_number_len // n
        for number in range(10**(n-1), 10**n):
            number_str = str(number)
            repeated_number = number_str * repetition_times
            yield repeated_number


def part2_main(input_str):

    input_list = input_str.split(',')
    invalid_numbers = []
    for input_ind in input_list:
        start, end = input_ind.split('-')
        code_number_lens = range(len(start), len(end)+1)
        ind_invalid_numbers = []
        for code_number_len in code_number_lens:
            for invalid_code in get_invalid_codes_part2(code_number_len):
                if int(start) <= int(invalid_code) <= int(end):
                    ind_invalid_numbers.append(int(invalid_code))
        ind_invalid_numbers = list(set(ind_invalid_numbers))
        invalid_numbers.extend(ind_invalid_numbers)
    return invalid_numbers


with open("input.txt", "r") as f:
    input_str = f.read()

invalid_numbers_part1 = part1_main(input_str)
print("Part 1: ", sum(invalid_numbers_part1))

invalid_numbers_part2 = part2_main(input_str)
print("Part 2: ", sum(invalid_numbers_part2))
