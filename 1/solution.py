from typing import Iterator

NAME_DIGIT_PAIRS = (
    ("one", "1"),
    ("two", "2"),
    ("three", "3"),
    ("four", "4"),
    ("five", "5"),
    ("six", "6"),
    ("seven", "7"),
    ("eight", "8"),
    ("nine", "9"),
)


def get_first_digit(line: str, iterator: Iterator[int], only_numeric: bool) -> str:
    for i in iterator:
        char = line[i]
        if char.isdigit():
            return char
        if only_numeric:
            continue
        for digit_name, digit in NAME_DIGIT_PAIRS:
            l = len(digit_name)
            if line[i : i + l] == digit_name:
                return digit


def solve_line(line: str, only_numeric: bool):
    first_digit = get_first_digit(line, range(len(line)), only_numeric)
    last_digit = get_first_digit(line, range(len(line) - 1, -1, -1), only_numeric)
    return int(first_digit + last_digit)


def solve(filename: str, only_numeric: bool):
    with open(filename) as f:
        lines = f.readlines()

    return sum((solve_line(line, only_numeric) for line in lines))


print("example.txt")
print(" part 1:", solve("example.txt", only_numeric=True))  # 142
print("example2.txt")
print(" part 2:", solve("example2.txt", only_numeric=False))  # 281

print("input.txt")
print(" part 1:", solve("input.txt", only_numeric=True))  # 54951
print(" part 2:", solve("input.txt", only_numeric=False))  # 55218
