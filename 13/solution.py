from operator import itemgetter

ASH = "."
ROCK = "#"
SYMBOL_SWAP = {ASH: ROCK, ROCK: ASH}
ROW_MULTIPLIER = 100
COL_MULTIPLIER = 1


def is_symmetric_by_row(puzzle: list[list[str]], split_row: int):
    for i in range(min(split_row, len(puzzle) - split_row)):
        i_above = split_row - i - 1
        i_below = split_row + i
        if puzzle[i_above] != puzzle[i_below]:
            return False
    return True


def find_horizontal_reflections(puzzle: list[list[str]]):
    return [split_row for split_row in range(1, len(puzzle)) if is_symmetric_by_row(puzzle, split_row)]


def find_vertical_reflections(puzzle: list[list[str]]):
    return find_horizontal_reflections(list(zip(*puzzle)))


def solve_1(puzzle: list[list[str]]):
    solutions = []
    if rows := find_horizontal_reflections(puzzle):
        solutions.extend(row * ROW_MULTIPLIER for row in rows)
    if columns := find_vertical_reflections(puzzle):
        solutions.extend(column * COL_MULTIPLIER for column in columns)
    return solutions


def solve_2(puzzle: list[list[str]]):
    solutions = set()
    for y in range(len(puzzle)):
        for x in range(len(puzzle[y])):
            puzzle[y][x] = SYMBOL_SWAP[puzzle[y][x]]
            solutions.update(solve_1(puzzle))
            puzzle[y][x] = SYMBOL_SWAP[puzzle[y][x]]

    initial_solution = solve_1(puzzle).pop()
    solutions.discard(initial_solution)
    assert len(solutions) == 1, solutions
    return solutions.pop()


def solve(filename: str):
    print(filename)
    with open(filename) as f:
        puzzles = [list(map(list, puzzle.splitlines())) for puzzle in f.read().split("\n\n")]

    print(" part 1:", sum(map(itemgetter(0), map(solve_1, puzzles))))
    print(" part 2:", sum(map(solve_2, puzzles)))


solve("example.txt")  # 405, 400
solve("input.txt")  # 30518, 36735
