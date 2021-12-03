from aoc_logging import logger


instructions = []
with open("boot_code.txt", 'r') as f:
    for line in f:
        operation, argument = line.strip().split(" ")
        instructions.append([operation, int(argument)])


def part_one():
    print("--- Part One ---")

    accumulator = 0

    executed_instructions = set()

    i = 0
    while True:
        if i in executed_instructions:
            break
        executed_instructions.add(i)

        operation, argument = instructions[i]

        match operation:
            case "acc":
                accumulator += argument
            case "jmp":
                i += argument
                continue
            case "nop":
                pass

        i += 1

    print(f"Answer: {accumulator}")


def part_two():
    print("--- Part Two ---")

    end = len(instructions)

    def evaluate_instructions(instructions, end):
        accumulator = 0

        executed_instructions = set()

        i = 0
        while True:
            if i in executed_instructions:
                return False, accumulator
            if i >= end:
                return True, accumulator

            executed_instructions.add(i)

            operation, argument = instructions[i]

            match operation:
                case "acc":
                    accumulator += argument
                case "jmp":
                    i += argument
                    continue
                case "nop":
                    pass

            i += 1

    answer = None

    for i in range(end):
        instructions_copy = [instruction.copy() for instruction in instructions]

        match instructions_copy[i][0]:
            case "acc":
                continue
            case "jmp":
                instructions_copy[i][0] = "nop"
            case "nop":
                instructions_copy[i][0] = "jmp"

        fixed, accumulator = evaluate_instructions(instructions_copy, end)
        if fixed:
            answer = accumulator
            break

    print(f"Answer: {answer}")


if __name__ == '__main__':
    print("--- Day 8: Handheld Halting ---")
    part_one()
    part_two()
