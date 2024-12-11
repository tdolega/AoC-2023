import re


def string_hash(s: str):
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h %= 256
    return h


def solve_2(steps: list[str]):
    boxes = [{} for _ in range(256)]
    for step in steps:
        parsed = re.match(r"([a-z]+)([=-])(\d?)", step)
        label, op, focal_length = parsed.groups()
        box_i = string_hash(label)
        box = boxes[box_i]
        match op:
            case "=":
                box[label] = int(focal_length)
            case "-":
                box.pop(label, None)

    focusing_power = 0
    for box_i, box in enumerate(boxes, start=1):
        for slot_i, focal_length in enumerate(box.values(), start=1):
            focusing_power += box_i * slot_i * focal_length
    return focusing_power


def solve(filename: str):
    print(filename)
    with open(filename) as f:
        steps = f.read().strip().split(",")

    print(" part 1:", sum(map(string_hash, steps)))
    print(" part 2:", solve_2(steps))


solve("example.txt")  # 1320, 145
solve("input.txt")  # 521341, 252782
