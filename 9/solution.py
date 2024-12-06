def solve_line(line: str, lookup_pos: int):
    # parse
    numbers = line.split()
    numbers = list(map(int, numbers))
    # create tree
    steps = [numbers]
    while any([n != 0 for n in steps[-1]]):
        step = steps[-1]
        next_step = [n2 - n1 for (n1, n2) in zip(step, step[1:])]
        steps.append(next_step)
    # predict
    for i in range(len(steps) - 1):
        i = len(steps) - i - 1
        last_here = steps[i][lookup_pos]
        last_above = steps[i - 1][lookup_pos]
        if lookup_pos == 0:
            steps[i - 1].insert(lookup_pos, last_above - last_here)
        else:  # -1
            steps[i - 1].append(last_above + last_here)
    return steps[0][lookup_pos]


def solve_any(filename: str, lookup_pos: int):
    with open(filename) as f:
        return sum(solve_line(line, lookup_pos) for line in f.readlines())


def solve(filename: str):
    print(filename)
    print(" part 1:", solve_any(filename, -1))
    print(" part 2:", solve_any(filename, 0))


solve("example.txt")  # 114, 2
solve("input.txt")  # 1884768153, 1031
