from typing import Callable, Dict


def get_fewest_possible(grabs: str):
    maxes = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for grab in grabs.split(";"):
        for single in grab.split(","):
            n_cubes, color = single.split()
            maxes[color] = max(maxes[color], int(n_cubes))
    return maxes


def solve_any(filename: str, score_fn: Callable[[int, Dict[str, int]], int]):
    with open(filename) as f:
        lines = f.readlines()

    result = 0
    for line in lines:
        game_id, grabs = line.split(":")
        game_id = int(game_id[5:])
        fewest_possible = get_fewest_possible(grabs)
        result += score_fn(game_id, fewest_possible)
    return result


def solve_1(filename: str):
    CONSTRAINTS = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    def score_fn(game_id, cubes_count):
        for color, n_cubes in cubes_count.items():
            if n_cubes > CONSTRAINTS[color]:
                return 0
        return game_id

    print(" part 1:", solve_any(filename, score_fn))


def solve_2(filename: str):
    def score_fn(game_id, cubes_count):
        power = 1
        for n_cubes in cubes_count.values():
            power *= n_cubes
        return power

    print(" part 2:", solve_any(filename, score_fn))


def solve(filename):
    print(filename)
    solve_1(filename)
    solve_2(filename)


solve("example.txt")  # 8, 2286
solve("input.txt")  # 2913, 55593
