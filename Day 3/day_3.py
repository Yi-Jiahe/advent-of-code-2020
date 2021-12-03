from aoc_logging import logger

def part_one():
    print("--- Part One ---")

    n_trees = 0

    x = 0

    width = None
    with open("map.txt", 'r') as f:
        for line in f:
            line = line.strip()

            if width is None:
                width = len(line)
            else:
                if line[x] == "#":
                    n_trees += 1

            x = (x+3) % width

    print(f"I will encounter {n_trees} trees")


def part_two():
    print("--- Part Two ---")

    slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ]

    n_trees = [0 for _ in slopes]

    xs = [0 for _ in slopes]

    width = None
    with open("map.txt", 'r') as f:
        for i, line in enumerate(f):
            line = line.strip()

            for i_slope, (slope, x) in enumerate(zip(slopes, xs)):
                if width is None:
                    width = len(line)
                if i % slope[1] == 0:
                    if line[x] == "#":
                        n_trees[i_slope] += 1

                    xs[i_slope] = (x+slope[0]) % width

    print(n_trees)
    answer = 1
    for n in n_trees:
        answer *= n
    print(f"Answer: {answer}")


if __name__ == '__main__':
    print("--- Day 3: Toboggan Trajectory ---")
    part_one()
    part_two()