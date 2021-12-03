from aoc_logging import logger


def part_one():
    print("--- Part One ---")

    joltages = []

    with open("output_joltages.txt", 'r') as f:
        for line in f:
            joltage = int(line.strip())
            joltages.append(joltage)

    joltages.sort()

    joltages.insert(0, 0)
    joltages.append(joltages[-1] + 3)

    differences = {
        1: 0, 2: 0, 3: 0
    }

    last_joltage = None
    for joltage in joltages:
        if last_joltage is not None:
            differences[joltage - last_joltage] += 1
        last_joltage = joltage

    print(f"Answer: {differences[1] * differences[3]}")


def part_two():
    print("--- Part Two ---")


if __name__ == '__main__':
    print("--- Day 10: Adapter Array ---")
    part_one()
    part_two()