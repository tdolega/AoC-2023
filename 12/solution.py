import re
from functools import cache


def parse_line(line: str):
    springs, groups = line.split()
    groups = tuple(map(int, groups.split(",")))
    return springs, groups


@cache
def count_solutions(springs: str, groups: tuple[int]):
    if not groups:
        if "#" in springs:
            return 0
        return 1

    n_solutions = 0
    group_size = groups[0]
    spots_for_group = rf"(?=[^#]([?#]{{{group_size}}}))"
    for spot_match in re.finditer(spots_for_group, springs):
        start, end = spot_match.span(1)

        if "#" in springs[:start]:  # todo: move this check to the regex
            continue

        n_solutions += count_solutions(springs[end:], groups[1:])

    return n_solutions


def solve_line(springs: str, groups: tuple[int]):
    springs = "." + springs
    return count_solutions(springs, groups)


def solve(filename: str):
    print(filename)
    with open(filename, "r") as f:
        lines = f.readlines()

    springs, groups = zip(*map(parse_line, lines))

    answer_1 = sum(map(solve_line, springs, groups))
    print(f" part 1: {answer_1}")

    N = 5
    springs = ["?".join([s] * N) for s in springs]
    groups = [g * N for g in groups]
    answer_2 = sum(map(solve_line, springs, groups))
    print(f" part 2: {answer_2}")


solve("example.txt")  # 21, 525152
solve("input.txt")  # 7490, 65607131946466
