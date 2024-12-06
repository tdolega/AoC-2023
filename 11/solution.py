def solve_any(filename: str, expand_multiplier=2):
    expand_multiplier -= 1  # one will be already counted

    with open(filename) as f:
        lines = [list(line.strip()) for line in f.readlines()]

    empty_rows = []
    for i, row in enumerate(lines):
        if all([c == "." for c in row]):
            empty_rows.append(i)
    empty_cols = []
    for i in range(len(lines[0])):
        if all([lines[j][i] == "." for j in range(len(lines))]):
            empty_cols.append(i)

    galaxies = []
    for i, row in enumerate(lines):
        for j, c in enumerate(row):
            if c == "#":
                galaxies.append((i, j))

    result = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            x1, y1 = galaxies[i]
            x2, y2 = galaxies[j]
            empty_rows_between = [row_idx for row_idx in empty_rows if row_idx > min(x1, x2) and row_idx < max(x1, x2)]
            empty_cols_between = [col_idx for col_idx in empty_cols if col_idx > min(y1, y2) and col_idx < max(y1, y2)]
            additional_x = len(empty_rows_between) * expand_multiplier
            additional_y = len(empty_cols_between) * expand_multiplier
            result += abs(x1 - x2) + abs(y1 - y2) + additional_x + additional_y
    return result


def solve(filename: str, part_2_multiplier: int):
    print(filename)
    print(" part 1:", solve_any(filename))
    print(" part 2:", solve_any(filename, part_2_multiplier))


solve("example.txt", 100)  # 374, 8410
solve("input.txt", 1000000)  # 9974721, 702770569197
