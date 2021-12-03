from aoc_logging import logger


def parse_rule(rule):
    container, _, contents_list = rule.partition("contain")
    container_colour = " ".join(container.strip().split(" ")[:-1])

    contents_list = contents_list.strip().split(",")

    contents = dict()

    for content in contents_list:
        details = content.strip(" .").split(" ")
        if details[0] == "no":
            contents = dict()
            break
        quantity = int(details[0])
        colour = " ".join(details[1:-1])
        contents[colour] = quantity

    return container_colour, contents


bags = dict()

with open("rules.txt", 'r') as f:
    for line in f:
        rule = line.strip()
        container, contents = parse_rule(rule)

        if container not in bags:
            bags[container] = {
                "parents": set(),
                "contents": contents
            }
        else:
            if len(bags[container]["contents"]) != 0:
                raise Exception("Bag already defined")
            else:
                bags[container]["contents"] = contents

        for bag in contents:
            if bag not in bags:
                bags[bag] = {
                    "parents": set(),
                    "contents": dict()
                }
            if container in bags[bag]["parents"]:
                raise Exception("Parent already registered")
            else:
                bags[bag]["parents"].add(container)


def part_one():
    print("--- Part One ---")

    search_list = []
    searched = set()
    ancestors = set()

    for parent in bags["shiny gold"]["parents"]:
        search_list.append(parent)
        searched.add(parent)
        ancestors.add(parent)

    while search_list:
        searching = search_list.pop(0)
        for parent in bags[searching]["parents"]:
            if parent not in searched:
                search_list.append(parent)
                searched.add(parent)
                if parent not in ancestors:
                    ancestors.add(parent)

    print(f"Answers: {len(ancestors)}")


def part_two():
    print("--- Part Two ---")

    memo = dict()

    def required_bags(bag):
        if bag in memo:
            print(f"Retrieving from memo: {bag}: {memo[bag]}")
            return memo[bag]

        n = 1
        for colour, number in bags[bag]["contents"].items():
            n += number * required_bags(colour)

        memo[bag] = n
        print(n, bag, bags[bag])

        return n

    print(f"Answer: {required_bags('shiny gold') - 1}")


if __name__ == '__main__':
    print("--- Day 7: Handy Haversacks ---")
    part_one()
    part_two()