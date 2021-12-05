from aoc_logging import logger

title = "--- Day 17: Conway Cubes ---"


def display_cubes(active_cubes):
    x_min, x_max = 0, 0
    y_min, y_max = 0, 0
    z_min, z_max = 0, 0

    for x, y, z in active_cubes:
        if x < x_min:
            x_min = x
        if x > x_max:
            x_max = x
        if y < y_min:
            y_min = y
        if y > y_max:
            y_max = y
        if z < z_min:
            z_min = z
        if z > z_max:
            z_max = z

    for z in range(z_min, z_max + 1):
        logger.info("")
        logger.info(f"z={z}")
        for x in range(x_min, x_max + 1):
            row = ""
            for y in range(y_min, y_max + 1):
                if (x, y, z) in active_cubes:
                    row += '#'
                else:
                    row += '.'
            logger.info(row)


def part_one():
    print("--- Part One ---")
    logger.info(title)
    logger.info("--- Part One ---")

    active_cubes = set()

    with open("puzzle_input.txt", 'r') as f:
        z = 0
        for x, row in enumerate(map(lambda line: line.strip(), f)):
            for y, cube in enumerate(row):
                if cube == '#':
                    active_cubes.add((x, y, z))

    logger.info("Before any cycles:")
    display_cubes(active_cubes)

    for i in range(6):
        logger.info(f"Start of cycle {i+1}")
        logger.info(f"Active cubes      : {active_cubes}")

        deactivated_cubes = set()
        inactive_cubes_to_check = set()

        for active_cube in active_cubes:
            x, y, z = active_cube
            neighbouring_active_cubes = 0

            for x_adj in range(x - 1, x + 2):
                for y_adj in range(y - 1, y + 2):
                    for z_adj in range(z - 1, z + 2):
                        adjacent_cube = (x_adj, y_adj, z_adj)
                        if adjacent_cube == active_cube:
                            continue
                        if adjacent_cube in active_cubes:
                            neighbouring_active_cubes += 1
                        else:
                            inactive_cubes_to_check.add(adjacent_cube)
            if not (neighbouring_active_cubes == 2 or neighbouring_active_cubes == 3):
                deactivated_cubes.add(active_cube)

        activated_cubes = set()

        for inactive_cube in inactive_cubes_to_check:
            x, y, z = inactive_cube
            neighbouring_active_cubes = 0
            for x_adj in range(x - 1, x + 2):
                for y_adj in range(y - 1, y + 2):
                    for z_adj in range(z - 1, z + 2):
                        adjacent_cube = (x_adj, y_adj, z_adj)
                        if adjacent_cube == inactive_cube:
                            continue
                        if adjacent_cube in active_cubes:
                            neighbouring_active_cubes += 1
            if neighbouring_active_cubes == 3:
                activated_cubes.add(inactive_cube)

        logger.info(f"Deactivated cubes : {deactivated_cubes}")
        logger.info(f"Activated cubes   : {activated_cubes}")

        logger.info(f"Number of active cubes = {len(active_cubes)}")
        active_cubes -= deactivated_cubes
        logger.info(f"Number of deactivated cubes = {len(deactivated_cubes)}")
        logger.info(f"Number of active cubes = {len(active_cubes)}")
        active_cubes |= activated_cubes
        logger.info(f"Number of activated cubes = {len(activated_cubes)}")
        logger.info(f"Number of active cubes = {len(active_cubes)}")

        logger.info(f"After {i+1} cycle{'' if i == 0 else 's'}:")
        display_cubes(active_cubes)

        logger.info("")

    print(f"There are {len(active_cubes)} active cubes after the sixth cycle")

    logger.info("")


def part_two():
    print("--- Part Two ---")
    logger.info(title)
    logger.info("--- Part Two ---")

    active_cubes = set()

    with open("puzzle_input.txt", 'r') as f:
        z, w = 0, 0
        for x, row in enumerate(map(lambda line: line.strip(), f)):
            for y, cube in enumerate(row):
                if cube == '#':
                    active_cubes.add((x, y, z, w))

    for i in range(6):
        logger.info(f"Start of cycle {i+1}")
        logger.info(f"Active cubes      : {active_cubes}")

        deactivated_cubes = set()
        inactive_cubes_to_check = set()

        for active_cube in active_cubes:
            x, y, z, w = active_cube
            neighbouring_active_cubes = 0

            for w_adj in range(w - 1, w + 2):
                for z_adj in range(z - 1, z + 2):
                    for x_adj in range(x - 1, x + 2):
                        for y_adj in range(y - 1, y + 2):
                            adjacent_cube = (x_adj, y_adj, z_adj, w_adj)
                            if adjacent_cube == active_cube:
                                continue
                            if adjacent_cube in active_cubes:
                                neighbouring_active_cubes += 1
                            else:
                                inactive_cubes_to_check.add(adjacent_cube)
            if not (neighbouring_active_cubes == 2 or neighbouring_active_cubes == 3):
                deactivated_cubes.add(active_cube)

        activated_cubes = set()

        for inactive_cube in inactive_cubes_to_check:
            x, y, z, w = inactive_cube
            neighbouring_active_cubes = 0
            for w_adj in range(w - 1, w + 2):
                for z_adj in range(z - 1, z + 2):
                    for x_adj in range(x - 1, x + 2):
                        for y_adj in range(y - 1, y + 2):
                            adjacent_cube = (x_adj, y_adj, z_adj, w_adj)
                            if adjacent_cube == inactive_cube:
                                continue
                            if adjacent_cube in active_cubes:
                                neighbouring_active_cubes += 1
            if neighbouring_active_cubes == 3:
                activated_cubes.add(inactive_cube)

        logger.info(f"Deactivated cubes : {deactivated_cubes}")
        logger.info(f"Activated cubes   : {activated_cubes}")

        logger.info(f"Number of active cubes = {len(active_cubes)}")
        active_cubes -= deactivated_cubes
        logger.info(f"Number of deactivated cubes = {len(deactivated_cubes)}")
        logger.info(f"Number of active cubes = {len(active_cubes)}")
        active_cubes |= activated_cubes
        logger.info(f"Number of activated cubes = {len(activated_cubes)}")
        logger.info(f"Number of active cubes = {len(active_cubes)}")

        logger.info("")

    print(f"There are {len(active_cubes)} active cubes after the sixth cycle")

    logger.info("")

    logger.info("")


if __name__ == '__main__':
    print(title)
    part_one()
    part_two()
