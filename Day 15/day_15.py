from aoc_logging import logger


starting_numbers = [1, 20, 11, 6, 12, 0]


def part_one():
    print("--- Part One ---")

    last_spoken_turn = dict()

    turn = 1
    last_spoken_number = None
    while True:
        spoken_number = None
        # Determine number to say
        if turn <= len(starting_numbers):
            spoken_number = starting_numbers[turn-1]
        else:
            if len(last_spoken_turn[last_spoken_number]) == 1:
                spoken_number = 0
            else:
                turn_minus_2, turn_minus_1 = last_spoken_turn[last_spoken_number]
                spoken_number = turn_minus_1 - turn_minus_2

        if spoken_number not in last_spoken_turn:
            last_spoken_turn[spoken_number] = [turn]
        else:
            last_spoken_turn[spoken_number].append(turn)
            if len(last_spoken_turn[spoken_number]) > 2:
                last_spoken_turn[spoken_number].pop(0)

        if turn == 2020:
            break

        turn += 1
        last_spoken_number = spoken_number

    print(f"Answer: {spoken_number}")


def part_two():
    print("--- Part Two ---")

    last_spoken_turn = dict()

    turn = 1
    last_spoken_number = None
    while True:
        spoken_number = None
        # Determine number to say
        if turn <= len(starting_numbers):
            spoken_number = starting_numbers[turn-1]
        else:
            if len(last_spoken_turn[last_spoken_number]) == 1:
                spoken_number = 0
            else:
                turn_minus_2, turn_minus_1 = last_spoken_turn[last_spoken_number]
                spoken_number = turn_minus_1 - turn_minus_2

        if spoken_number not in last_spoken_turn:
            last_spoken_turn[spoken_number] = [turn]
        else:
            last_spoken_turn[spoken_number].append(turn)
            if len(last_spoken_turn[spoken_number]) > 2:
                last_spoken_turn[spoken_number].pop(0)

        if turn == 30000000:
            break

        turn += 1
        last_spoken_number = spoken_number

    print(f"Answer: {spoken_number}")


if __name__ == '__main__':
    print("--- Day 15: Rambunctious Recitation ---")
    part_one()
    part_two()