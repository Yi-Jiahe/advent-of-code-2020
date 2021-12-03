from aoc_logging import logger


def part_one():
    print("--- Part One ---")

    seats = []

    with open("seat_layout.txt", 'r') as f:
        for i, line in enumerate(f):
            for j, char in enumerate(line.strip()):
                if char == 'L':
                    seats.append((i, j))

    rows, columns = i+1, j+1

    is_occupied = [[False for _ in range(columns)] for _ in range(rows)]

    while True:
        changes = dict()
        for seat in seats:
            i, j = seat
            if is_occupied[i][j]:
                occupied_adjacent_seats = 0

                for i_adj in [-1, 0, 1]:
                    if occupied_adjacent_seats >= 4:
                        break
                    for j_adj in [-1, 0, 1]:
                        if i_adj == 0 and j_adj == 0:
                            continue
                        row, col = i+i_adj, j+j_adj
                        if row < 0 or row >= rows or col < 0 or col >= columns:
                            continue
                        if is_occupied[row][col]:
                            occupied_adjacent_seats += 1
                        if occupied_adjacent_seats >= 4:
                            changes[(i, j)] = False
                            break
            else:
                adjacent_seat_is_occupied = False
                for i_adj in [-1, 0, 1]:
                    if adjacent_seat_is_occupied:
                        break
                    for j_adj in [-1, 0, 1]:
                        if i_adj == 0 and j_adj == 0:
                            continue
                        row, col = i+i_adj, j+j_adj
                        if row < 0 or row >= rows or col < 0 or col >= columns:
                            continue
                        if is_occupied[row][col]:
                            adjacent_seat_is_occupied = True
                            break
                if not adjacent_seat_is_occupied:
                    changes[(i, j)] = True

        if len(changes) == 0:
            break

        for seat, occupied in changes.items():
            i, j = seat
            is_occupied[i][j] = occupied

    occupied_seats = 0
    for seat in seats:
        i, j = seat
        if is_occupied[i][j]:
            occupied_seats += 1

    print(f"{occupied_seats} seats end up occupied")


def part_two():
    print("--- Part Two ---")


if __name__ == '__main__':
    print("--- Day 11: Seating System ---")
    part_one()
    part_two()