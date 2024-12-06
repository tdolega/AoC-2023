PIPES = {
    # symbol: [up, right, down, left]
    "|": [1, 0, 1, 0],
    "-": [0, 1, 0, 1],
    "L": [1, 1, 0, 0],
    "J": [1, 0, 0, 1],
    "7": [0, 0, 1, 1],
    "F": [0, 1, 1, 0],
    ".": [0, 0, 0, 0],
    "S": [1, 1, 1, 1],
    "X": [0, 0, 0, 0],  # visited marker
}


def start_pos(lines: list[str]):
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "S":
                return x, y


def get_next(lines: list[str], x: int, y: int):
    next_positions = []
    c = lines[y][x]
    pipe = PIPES[c]
    if pipe[0] and y > 0:
        next_c = lines[y - 1][x]
        next_pipe = PIPES[next_c]
        if next_pipe[2]:
            next_positions.append((x, y - 1))
    if pipe[1] and x < len(lines[0]) - 1:
        next_c = lines[y][x + 1]
        next_pipe = PIPES[next_c]
        if next_pipe[3]:
            next_positions.append((x + 1, y))
    if pipe[2] and y < len(lines) - 1:
        next_c = lines[y + 1][x]
        next_pipe = PIPES[next_c]
        if next_pipe[0]:
            next_positions.append((x, y + 1))
    if pipe[3] and x > 0:
        next_c = lines[y][x - 1]
        next_pipe = PIPES[next_c]
        if next_pipe[1]:
            next_positions.append((x - 1, y))
    return next_positions


def solve_1(lines: list[str]):
    positions = [start_pos(lines)]
    i = -1
    while len(positions):
        next_positions = []
        for x, y in positions:
            next_positions += get_next(lines, x, y)
            lines[y][x] = "X"
        positions = next_positions
        i += 1
    return i


def solve_2(parsed_lines: list[str], original_lines: list[str]):
    # step 1: correct "S" to what it should be
    x, y = start_pos(original_lines)
    connected = get_next(original_lines, x, y)
    s_table = [
        1 if min([y for (x, y) in connected]) < y else 0,
        1 if max([x for (x, y) in connected]) > x else 0,
        1 if max([y for (x, y) in connected]) > y else 0,
        1 if min([x for (x, y) in connected]) < x else 0,
    ]
    for symbol, table in PIPES.items():
        if table == s_table:
            original_lines[y][x] = symbol
            break

    # step 2: ray casting
    area = 0
    for y in range(len(parsed_lines)):
        is_inside = False
        for x in range(len(parsed_lines[0])):
            parsed = parsed_lines[y][x]
            original = original_lines[y][x]
            if parsed == "X" and original in ["|", "F", "7"]:
                is_inside = not is_inside
            elif parsed != "X" and is_inside:
                area += 1
    return area


def solve(filename: str):
    print(filename)
    with open(filename) as f:
        lines = [list(line.strip()) for line in f.readlines()]
        lines2 = [line[:] for line in lines]  # lines too

    print(" part 1:", solve_1(lines))
    print(" part 2:", solve_2(lines, lines2))


solve("example.txt")  # -, 4
solve("example2.txt")  # -, 8
solve("input.txt")  # 7012, 395
