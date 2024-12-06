def solve_any(lines: list[str], fix_kerning: bool):
    parsed = []
    for line in lines:
        line = line.split()
        line = line[1:]
        if fix_kerning:
            line = [int("".join(line))]
        else:
            line = [int(x) for x in line]
        parsed.append(line)
    times, distances = parsed

    result = 1
    for race_time, best_distance in zip(times, distances):
        n_better = 0
        for hold_ms in range(race_time + 1):
            speed = hold_ms
            move_ms = race_time - hold_ms
            distance_traveled = speed * move_ms
            if distance_traveled > best_distance:
                n_better += 1
        result *= n_better
    return result


def solve(filename: str):
    print(filename)
    with open(filename) as f:
        lines = f.readlines()

    print(" part 1:", solve_any(lines, False))
    print(" part 2:", solve_any(lines, True))


solve("example.txt")  # 288, 71503
solve("input.txt")  # 771628, 27363861
