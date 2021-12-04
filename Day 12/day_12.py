import math

from aoc_logging import logger


def part_one():
    print("--- Part One ---")

    origin = (0, 0)
    position = [cood for cood in origin]
    heading = 0

    with open("navigation_instructions.txt", 'r') as f:
        for line in f:
            instruction = line.strip()
            action, value = instruction[0], int(instruction[1:])

            match action:
                case "N":
                    position[1] += value
                case "S":
                    position[1] -= value
                case "E":
                    position[0] += value
                case "W":
                    position[0] -= value
                case "L":
                    heading += value
                case "R":
                    heading -= value
                case "F":
                    position[0] += (math.cos(math.radians(heading)) * value)
                    position[1] += (math.sin(math.radians(heading)) * value)
            if heading > 180:
                heading -= 360
            elif heading <= -180:
                heading += 360

    print(f"Answer: {int(math.fabs(position[0] - origin[0]) + math.fabs(position[1] - origin[1]))}")


def part_two():
    print("--- Part Two ---")

    origin = (0, 0)
    position = [cood for cood in origin]
    waypoint = [10, 1]

    def rotate(point, angle):
        x, y = point
        theta = math.atan2(y, x)
        theta += math.radians(angle)
        r = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

        rotated_point = [r * math.cos(theta), r * math.sin(theta)]
        integered_rotated_point = [cood for cood in map(round, [r * math.cos(theta), r * math.sin(theta)])]
        return integered_rotated_point

    with open("navigation_instructions.txt", 'r') as f:
        for line in f:
            instruction = line.strip()
            action, value = instruction[0], int(instruction[1:])

            match action:
                case "N":
                    waypoint[1] += value
                case "S":
                    waypoint[1] -= value
                case "E":
                    waypoint[0] += value
                case "W":
                    waypoint[0] -= value
                case "L":
                    waypoint = rotate(waypoint, value)
                case "R":
                    waypoint = rotate(waypoint, -value)
                case "F":
                    position[0] += waypoint[0] * value
                    position[1] += waypoint[1] * value

    print(f"Answer: {int(math.fabs(position[0] - origin[0]) + math.fabs(position[1] - origin[1]))}")


if __name__ == '__main__':
    print("--- Day 12: Rain Risk ---")
    part_one()
    part_two()