from aoc_logging import logger


def part_one():
    print("--- Part One ---")

    def value_in_range(ranges, value):
        for valid_range in ranges:
            if valid_range[0] <= value <= valid_range[1]:
                return True

        return False

    all_fields_valid_ranges = []
    ticket_scanning_error_rate = 0

    section = "rules"
    with open("puzzle_input.txt", 'r') as f:
        for line in map(lambda line: line.strip(), f):
            if line == "your ticket:":
                section = "my_ticket"
                continue
            elif line == "nearby tickets:":
                section = "nearby_tickets"
                continue
            elif line == "":
                continue

            match section:
                case "rules":
                    _, ranges = map(lambda s: s.strip(), line.split(":"))
                    ranges = map(lambda s: s.strip(), ranges.split("or"))
                    ranges = [[x for x in map(int, valid_range.split("-"))] for valid_range in ranges]

                    for valid_range in ranges:
                        i = 0
                        while True:
                            # If there is no range in the merged ranged, just add it to the range
                            if not all_fields_valid_ranges:
                                all_fields_valid_ranges.append(valid_range)
                                break

                            all_fields_valid_range = all_fields_valid_ranges[i]

                            # If the start of the new range is larger than the end of range being compared
                            if valid_range[0] > all_fields_valid_range[1]:
                                # If the range from the merged ranged is not the last one
                                if i < len(all_fields_valid_ranges) - 1:
                                    i += 1
                                    continue
                                else:
                                    all_fields_valid_ranges.append(valid_range)
                                    break

                            # If the end of the new range is less than the start of the range being compared:
                            if valid_range[1] < all_fields_valid_range[0]:
                                # The start of the range is necessarily less than the start of the range in the merged range
                                # There is therefore no overlap and the range should be inserted before the range from the merged range
                                all_fields_valid_ranges.insert(i, valid_range)
                                break

                            # The start of the new range is less than the end of the range being compared
                            # and the end of the new range is more than the start
                            # Therefore there is an overlap and we can merge some ranges
                            # At this point we also need to see if any of the other ranges will be merged in
                            if valid_range[0] < all_fields_valid_range[0]:
                                all_fields_valid_ranges[i][0] = valid_range[0]

                            new_end = valid_range[1] if valid_range[1] > all_fields_valid_range[1] else all_fields_valid_range[1]

                            all_fields_valid_ranges[i][1] = valid_range[1]
                            while i+1 < len(all_fields_valid_ranges):
                                if all_fields_valid_ranges[i+1][0] < new_end:
                                    new_end = all_fields_valid_ranges[i+1][1] if all_fields_valid_ranges[i+1][1] >new_end  else new_end
                                    all_fields_valid_ranges.pop(i+1)
                                    continue
                                break
                            all_fields_valid_ranges[i][1] = new_end
                            break

                case "my_ticket":
                    pass

                case "nearby_tickets":
                    values = map(int, line.split(','))
                    for value in values:
                        if not value_in_range(all_fields_valid_ranges, value):
                            ticket_scanning_error_rate += value

    logger.info(f"All valid values: {all_fields_valid_ranges}")
    print(f"Ticket scanning error rate: {ticket_scanning_error_rate}")


def part_two():
    print("--- Part Two ---")

    def determine_valid_fields(rules, value):
        valid_fields = set()

        for field, ranges in rules.items():
            for valid_range in ranges:
                if valid_range[0] <= value <= valid_range[1]:
                    valid_fields.add(field)
        return valid_fields

    rules = dict()

    my_ticket = None

    possible_fields_identities = None

    section = "rules"
    with open("puzzle_input.txt", 'r') as f:
        for line in map(lambda line: line.strip(), f):
            if line == "your ticket:":
                section = "my_ticket"
                continue
            elif line == "nearby tickets:":
                section = "nearby_tickets"
                continue
            elif line == "":
                continue

            match section:
                case "rules":
                    field_name, ranges = map(lambda s: s.strip(), line.split(":"))
                    ranges = map(lambda s: s.strip(), ranges.split("or"))
                    ranges = [[x for x in map(int, valid_range.split("-"))] for valid_range in ranges]

                    rules[field_name] = ranges

                case "my_ticket":
                    my_ticket = [value for value in map(int, line.split(','))]
                    possible_fields_identities = {i: {field_name for field_name in rules.keys()} for i in range(len(my_ticket))}

                case "nearby_tickets":
                    ticket = map(int, line.split(','))
                    possible_fields_identities_ticket = []
                    invalid = False
                    for value in ticket:
                        valid_fields = determine_valid_fields(rules, value)
                        if len(valid_fields) == 0:
                            invalid = True
                            break
                        possible_fields_identities_ticket.append(valid_fields)
                    if not invalid:
                        for i in range(len(possible_fields_identities)):
                            possible_field_identities_ticket = possible_fields_identities_ticket[i]
                            possible_fields_identities[i] = {field_name for field_name in possible_fields_identities[i] if field_name in possible_field_identities_ticket}

    logger.info("Possible field identities")
    for i, field in possible_fields_identities.items():
        logger.info(f"{i}: {field}")

    assigned_fields = set()
    sorted_fields = [None for _ in range(len(my_ticket))]
    for i, field in possible_fields_identities.items():
        sorted_fields[len(field)-1] = (i, field)

    identified_fields = dict()
    for i, possible_field_names in sorted_fields:
        field_name = (possible_field_names - assigned_fields).pop()
        assigned_fields.add(field_name)
        identified_fields[field_name] = i

    answer = 1
    for field_name, i in identified_fields.items():
        logger.info(f"{field_name}, {i}")
        if field_name.startswith("departure"):
            answer *= my_ticket[i]

    print(f"Answer: {answer}")


if __name__ == '__main__':
    print("")
    part_one()
    part_two()