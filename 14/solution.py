ROUNDED = "O"
CUBE = "#"
EMPTY = "."


def calculate_load(platform: list[list[str]]):
    load = 0
    for distance, row in enumerate(platform[::-1], start=1):
        for tile in row:
            if tile == ROUNDED:
                load += distance
    return load


def move_rock(platform: list[list[str]], x: int, y: int, dx: int, dy: int):
    while 0 <= x + dx < len(platform[0]) and 0 <= y + dy < len(platform) and platform[y + dy][x + dx] == EMPTY:
        platform[y + dy][x + dx] = ROUNDED
        platform[y][x] = EMPTY
        x += dx
        y += dy


def tilt_platform(platform: list[list[str]], dx: int, dy: int):
    if dx:  # horizontal tilt
        x_range = range(len(platform[0]))
        x_range = x_range if dx < 0 else x_range[::-1]
        for x in x_range:
            for y in range(len(platform)):
                if platform[y][x] == ROUNDED:
                    move_rock(platform, x, y, dx, dy)
    elif dy:  # vertical tilt
        y_range = range(len(platform))
        y_range = y_range if dy < 0 else y_range[::-1]
        for y in y_range:
            for x in range(len(platform[0])):
                if platform[y][x] == ROUNDED:
                    move_rock(platform, x, y, dx, dy)


def cycle_platform(platform: list[list[str]]):
    for dx, dy in ((0, -1), (-1, 0), (0, 1), (1, 0)):
        tilt_platform(platform, dx, dy)


def cycle_platform_loop(platform: list[list[str]], cycles: int):
    history = {}
    for cycle in range(cycles):
        cycle_platform(platform)
        platform_str = "".join("".join(row) for row in platform)

        if platform_str in history:
            cycle_repeat_length = cycle - history[platform_str]
            cycles_remaining = (cycles - cycle - 1) % cycle_repeat_length
            for _ in range(cycles_remaining):
                cycle_platform(platform)
            break

        history[platform_str] = cycle


def solve(filename: str):
    print(filename)
    with open(filename) as f:
        platform = list(map(list, f.read().splitlines()))

    platform1 = [row[:] for row in platform]  # copy
    tilt_platform(platform1, 0, -1)
    print(" part 1:", calculate_load(platform1))

    platform2 = [row[:] for row in platform]  # copy
    cycle_platform_loop(platform2, 1000000000)
    print(" part 2:", calculate_load(platform2))


solve("example.txt")  # 136, 64
solve("input.txt")  # 108840, 103445
