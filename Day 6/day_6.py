from aoc_logging import logger


def part_one():
    print("--- Part One ---")

    count = 0

    yes_tions = set()

    with open("answers.txt", 'r') as f:
        for line in f:
            line = line.strip()

            if line == "":
                count += len(yes_tions)
                yes_tions = set()
                continue

            for question in line:
                if question not in yes_tions:
                    yes_tions.add(question)

    count += len(yes_tions)

    print(f"Answer: {count}")


def part_two():
    print("--- Part Two ---")

    count = 0

    group_size = 0
    yes_tions = dict()

    def count_per_group(yes_tions, group_size):
        count = 0
        for yeses in yes_tions.values():
            if yeses == group_size:
                count += 1
        return count

    with open("answers.txt", 'r') as f:
        for line in f:
            line = line.strip()

            if line == "":
                count += count_per_group(yes_tions, group_size)

                group_size = 0
                yes_tions = dict()
                continue

            group_size += 1
            for question in line:
                if question not in yes_tions:
                    yes_tions[question] = 0
                yes_tions[question] += 1

    count += count_per_group(yes_tions, group_size)

    print(f"Answer: {count}")


if __name__ == '__main__':
    print("--- Day 6: Custom Customs ---")
    part_one()
    part_two()