from aoc_logging import logger


def part_one():
    print("--- Part One ---")

    number = None

    previous_25 = []

    with open("numbers.txt", 'r') as f:
        for line in f:
            number = int(line.strip())

            valid = False
            if len(previous_25) == 25:
                for i in range(25-1):
                    for j in range(i+1, 25):
                        number_1, number_2 = previous_25[i], previous_25[j]
                        if number_1 == number_2:
                            continue
                        if number_1 + number_2 == number:
                            valid = True
                            break
                if not valid:
                    break

                previous_25.pop(0)

            previous_25.append(number)

    print(f"Answer: {number}")
    return number


def part_two(invalid_number):
    print("--- Part Two ---")

    numbers = []
    with open("numbers.txt", 'r') as f:
        for line in f:
            numbers.append(int(line.strip()))

    window_bounds = [0, 1]
    window_sum = numbers[0] + numbers[1]

    while True:
        if window_sum == invalid_number and window_bounds[1] - window_bounds[0] >= 1:
            break

        if window_sum < invalid_number:
            window_bounds[1] += 1
            window_sum += numbers[window_bounds[1]]
        elif window_sum > invalid_number:
            window_sum -= numbers[window_bounds[0]]
            window_bounds[0] += 1

    contiguous_set = numbers[window_bounds[0]: window_bounds[1]+1]

    print(f"Answer: {min(contiguous_set) + max(contiguous_set)}")



if __name__ == '__main__':
    print("--- Day 9: Encoding Error ---")
    invalid_number = part_one()
    part_two(invalid_number)