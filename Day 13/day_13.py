import math

from aoc_logging import logger


def part_one():
    print("--- Part One ---")

    earliest_departure = None
    buses = None

    with open("notes.txt", 'r') as f:
        for i, line in enumerate(f):
            if i == 0:
                earliest_departure = int(line.strip())
            if i == 1:
                buses = [int(bus) for bus in map(lambda x: x.strip(), line.strip().split(",")) if bus.strip() != 'x']

    earliest_bus = None
    shortest_wait = earliest_departure

    for bus in buses:
        last_departure = earliest_departure % bus
        wait = None
        if last_departure == 0:
            wait = 0
        else:
            wait = bus - last_departure
        if wait < shortest_wait:
            earliest_bus = bus
            shortest_wait = wait

    print(f"The earliest bus is bus no.{earliest_bus} with a wait of {shortest_wait} minutes")
    print(f"Answer: {earliest_bus * shortest_wait}")


def part_two():
    print("--- Part Two ---")

    buses = None

    with open("notes.txt", 'r') as f:
        for i_line, line in enumerate(f):
            if i_line == 0:
                pass
            if i_line == 1:
                buses = [(i, int(bus)) for (i, bus) in enumerate(map(lambda x: x.strip(), line.strip().split(","))) if bus != 'x']

    buses.sort(key=lambda bus: bus[1], reverse=True)

    print(buses)

    timestamp = -buses[0][0]
    while True:
        found = True
        for bus in buses:
            offset, bus_id = bus
            if (timestamp + offset) % bus_id != 0:
                found = False
                break

        if found:
            break

        timestamp += buses[0][1]

    print(f"Answer: {timestamp}")


if __name__ == '__main__':
    print("--- Day 13: Shuttle Search ---")
    part_one()
    part_two()