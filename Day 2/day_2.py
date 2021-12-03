from aoc_logging import logger

def part_one():
    print("--- Part One ---")

    n_valid_passwords = 0

    with open("passwords.txt", 'r') as f:
        for line in f:
            policy, password = line.strip().split(":")
            password = password.strip()
            times, letter = policy.strip().split(" ")
            min_occurances, max_occurances = map(int, times.strip().split("-"))

            occurances = 0
            for char in password:
                if char == letter:
                    occurances += 1
            if min_occurances <= occurances <= max_occurances:
                n_valid_passwords += 1

    print(f"{n_valid_passwords} passwords are valid")


def part_two():
    print("--- Part Two ---")

    n_valid_passwords = 0

    with open("passwords.txt", 'r') as f:
        for line in f:
            policy, password = line.strip().split(":")
            password = password.strip()
            times, letter = policy.strip().split(" ")
            positions = map(int, times.strip().split("-"))

            matches = 0
            for position in positions:
                if password[position-1] == letter:
                    matches += 1

            if matches == 1:
                n_valid_passwords += 1
                logger.info(f"VALID  : {line.strip()}")
            else:
                logger.info(f"INVALID: {line.strip()}")

    print(f"{n_valid_passwords} passwords are valid")


if __name__ == '__main__':
    print("--- Day 2: Password Philosophy ---")
    part_one()
    part_two()
