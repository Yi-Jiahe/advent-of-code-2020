import math

from aoc_logging import logger

def find_seat_id(boarding_pass):
    row_range = [0, 127]
    column_range = [0, 7]

    for char in boarding_pass[:7]:
        match char:
            case 'F':
                row_range[1] -= math.ceil((row_range[1] - row_range[0]) / 2)
            case 'B':
                row_range[0] += math.ceil((row_range[1] - row_range[0]) / 2)
    if row_range[0] != row_range[1]:
        raise Exception(f"Row partitioning failed: {row_range}")

    for char in boarding_pass[-3:]:
        match char:
            case 'L':
                column_range[1] -= math.ceil((column_range[1] - column_range[0]) / 2)
            case 'R':
                column_range[0] += math.ceil((column_range[1] - column_range[0]) / 2)
    if column_range[0] != column_range[1]:
        raise Exception(f"Column partitioning failed: {column_range}")

    row = row_range[0]
    column = column_range[1]

    return row * 8 + column


def part_one():
    print("--- Part One ---")

    highest_seat_id = -1

    with open("boarding_passes.txt", 'r') as f:
        for line in f:
            boarding_pass = line.strip()

            seat_id = find_seat_id(boarding_pass)

            if seat_id > highest_seat_id:
                highest_seat_id = seat_id

    print(f"The highest seat ID is {highest_seat_id}")


def part_two():
    print("--- Part Two ---")

    seats = [False for _ in range(127*8 + 7)]
    FILLED = True

    with open("boarding_passes.txt", 'r') as f:
        for line in f:
            boarding_pass = line.strip()

            seat_id = find_seat_id(boarding_pass)

            seats[seat_id] = FILLED

    section = "front"
    found = False
    for seat_id, seat in enumerate(seats):

        if section == "front":
            if seat is FILLED:
                section = "middle"
                continue
        if section == "middle":
            if seat is not FILLED:
                if not found:
                    found = True
                    print(f"My seat ID is {seat_id}")
                    continue
                else:
                    if seat is not FILLED:
                        section = "back"
                        continue


if __name__ == '__main__':
    print("--- Day 5: Binary Boarding ---")
    part_one()
    part_two()