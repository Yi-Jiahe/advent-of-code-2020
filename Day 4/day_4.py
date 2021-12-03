from aoc_logging import logger


def part_one():
    print("--- Part One ---")

    n_valid_passports = 0

    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    passport_template = {
        "byr": None,
        "iyr": None,
        "eyr": None,
        "hgt": None,
        "hcl": None,
        "ecl": None,
        "pid": None,
        "cid": None,
    }

    passport = passport_template.copy()

    def validate_passport(passport):
        valid = True
        for key, value in passport.items():
            if key in required_fields:
                if value is None:
                    valid = False
                    break
        if valid:
            logger.info(f"VALID  : {passport}")
            return 1
        else:
            logger.info(f"INVALID: {passport}")
            return 0

    with open("batch_file.txt", 'r') as f:
        for line in f:
            line = line.strip()

            # Validate passport
            if line == "":
                n_valid_passports += validate_passport(passport)

                # Prepare new passport
                passport = passport_template.copy()
                continue

            fields = line.split()
            for field in fields:
                key, value = field.strip().split(":")
                passport[key] = value

    n_valid_passports += validate_passport(passport)

    print(f"There are {n_valid_passports} valid passports in the batch file")


def part_two():
    print("--- Part Two ---")

    n_valid_passports = 0

    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    passport_template = {
        "byr": None,
        "iyr": None,
        "eyr": None,
        "hgt": None,
        "hcl": None,
        "ecl": None,
        "pid": None,
        "cid": None,
    }

    passport = passport_template.copy()

    def validate_passport(passport):
        valid = True
        for key, value in passport.items():
            if key in required_fields:
                if value is None:
                    valid = False
                    break
                match key:
                    case "byr":
                        if not (1920 <= int(value) <= 2002):
                            valid = False
                    case "iyr":
                        if not (2010 <= int(value) <= 2020):
                            valid = False
                    case "eyr":
                        if not (2020 <= int(value) <= 2030):
                            valid = False
                    case "hgt":
                        height, units = value[:-2], value[-2:]
                        match units:
                            case "cm":
                                if not (150 <= int(height) <= 193):
                                    valid = False
                            case "in":
                                if not (59 <= int(height) <= 76):
                                    valid = False
                            case _:
                                valid = False
                    case "hcl":
                        if not value.startswith('#'):
                            valid = False
                            break
                        if len(value) != 7:
                            valid = False
                            break
                        for char in value[1:]:
                            if not (char.isdigit() or char in {'a', 'b', 'c', 'd', 'e', 'f'}):
                                valid = False
                                break
                    case "ecl":
                        if value not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
                            valid = False
                    case "pid":
                        if len(value) != 9:
                            valid = False
                            break
                        for char in value:
                            if not char.isdigit():
                                valid = False
                                break
                if not valid:
                    break
        if valid:
            logger.info(f"VALID  : {passport}")
            return 1
        else:
            logger.info(f"INVALID: {passport}")
            return 0

    with open("batch_file.txt", 'r') as f:
        for line in f:
            line = line.strip()

            # Validate passport
            if line == "":
                n_valid_passports += validate_passport(passport)

                # Prepare new passport
                passport = passport_template.copy()
                continue

            fields = line.split()
            for field in fields:
                key, value = field.strip().split(":")
                passport[key] = value

    n_valid_passports += validate_passport(passport)

    print(f"There are {n_valid_passports} valid passports in the batch file")


if __name__ == '__main__':
    print("--- Day 4: Passport Processing ---")
    part_one()
    part_two()