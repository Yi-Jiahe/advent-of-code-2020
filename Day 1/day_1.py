from aoc_logging import logger

def part_one():
    print("--- Part One ---")

    entries = []
    with open("expense_report.txt", 'r') as f:
        for line in f:
            entry = int(line.strip())
            entries.append(entry)

    N = len(entries)

    for i in range(N-1):
        for j in range(i+1, N):
            entry_1, entry_2 = entries[i], entries[j]
            if entry_1 + entry_2 == 2020:
                print(f"Answer {entry_1 * entry_2}")


def part_two():
    print("--- Part Two ---")

    entries = []
    with open("expense_report.txt", 'r') as f:
        for line in f:
            entry = int(line.strip())
            entries.append(entry)

    N = len(entries)

    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                entry_1, entry_2, entry_3 = entries[i], entries[j], entries[k]
                if sum([entry_1, entry_2, entry_3]) == 2020:
                    print(f"Answer {entry_1 * entry_2 * entry_3}")


if __name__ == '__main__':
    print("--- Day 1: Report Repair ---")
    part_one()
    part_two()
    logger.info("hi")