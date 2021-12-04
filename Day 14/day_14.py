import math
import re

from aoc_logging import logger


uint36_max = int(math.pow(2, 36)) - 1


def dump_memory(memory):
    i = 0
    while i < len(memory) // 36:
        data = memory[i*36: i*36 + 36]
        print(i, data, len(data))
        i += 1


def part_one():
    print("--- Part One ---")

    def write_to_memory(memory, mask, address, value):
        start_index = address * 36
        end_index = start_index + 36

        binary_value = format(value % (uint36_max + 1), '036b')

        masked_value = ""
        for mask_bit, value_bit in zip(mask, binary_value):
            if mask_bit == "X":
                masked_value += value_bit
            else:
                masked_value += mask_bit

        logger.info(f"value:  {binary_value}   (decimal {value})")
        logger.info(f"mask:   {mask}")
        logger.info(f"result: {masked_value}   (decimal {int(masked_value, 2)})")
        logger.info("")

        if len(memory) < start_index:
            return memory + '0' * (start_index - len(memory)) + masked_value
        elif start_index == len(memory):
            return memory + masked_value
        else:
            return memory[:start_index] + masked_value + memory[end_index:]

    memory = ""

    mask = None
    with open("initialization_program.txt", 'r') as f:
        for line in f:
            line = line.strip()
            rhs, lhs = map(lambda x: x.strip(), line.split("="))
            if rhs == "mask":
                mask = lhs
            else:
                m = re.search("^mem\[([0-9]+)\]$", rhs)
                address = int(m[1])
                value = int(lhs)
                memory = write_to_memory(memory, mask, address, value)

    value_sum = 0

    i = 0
    while i < len(memory) // 36:
        data = memory[i*36: i*36 + 36]
        value_sum += int(data, 2)
        i += 1

    print(f"Answer: {value_sum}")


def part_two():
    print("--- Part Two ---")


    def find_addresses(mask, address):
        written_addresses = set()

        binary_address = format(address % (uint36_max + 1), '036b')

        masked_address = ""
        for mask_bit, address_bit in zip(mask, binary_address):
            masked_address += address_bit if mask_bit == '0' else mask_bit

        logger.info(f"value:  {binary_address}   (decimal {address})")
        logger.info(f"mask:   {mask}")
        logger.info(f"result: {masked_address}")

        search_stack = [masked_address]
        while search_stack:
            masked_address = search_stack.pop(0)

            contains_X = False
            for i, masked_bit in enumerate(masked_address):
                if masked_bit == 'X':
                    contains_X = True
                    for replacement_bit in ["0", "1"]:
                        replacement = masked_address[:i] + replacement_bit + masked_address[i+1:]
                        search_stack.append(replacement)
                    if contains_X:
                        break

            if not contains_X:
                logger.info(f"{masked_address}   (decimal {int(masked_address, 2)})")
                written_addresses.add(int(masked_address, 2))

        logger.info("")

        return written_addresses


    memory = dict()

    mask = None
    with open("initialization_program.txt", 'r') as f:
        for line in f:
            line = line.strip()
            rhs, lhs = map(lambda x: x.strip(), line.split("="))
            if rhs == "mask":
                mask = lhs
            else:
                m = re.search("^mem\[([0-9]+)\]$", rhs)
                address = int(m[1])
                value = int(lhs)
                for written_address in find_addresses(mask, address):
                    memory[written_address] = value

    value_sum = 0
    for value in memory.values():
        value_sum += value

    print(f"Answer: {value_sum}")


if __name__ == '__main__':
    print("--- Day 14: Docking Data ---")
    part_one()
    part_two()