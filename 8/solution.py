import numpy as np


def solve_node(instructions: list[int], nodes: dict[str, list[str]], node: str):
    steps = 0
    while node[-1] != "Z":  # for part 1 should be "ZZZ" but this works for both
        instruction = instructions[steps % len(instructions)]
        node = nodes[node][instruction]
        steps += 1
    return steps


def solve_any(filename: str, is_part2: bool):
    with open(filename) as f:
        lines = f.readlines()

    instructions = lines[0].strip()
    instructions = [0 if i == "L" else 1 for i in instructions]

    nodes = {}
    for line in lines[2:]:
        node, children_names = line.strip().split(" = ")
        nodes[node] = children_names[1:-1].split(", ")

    if is_part2:
        start_nodes = [node for node in nodes if node[-1] == "A"]
    else:
        start_nodes = ["AAA"]

    steps = [solve_node(instructions, nodes, node) for node in start_nodes]
    return np.lcm.reduce(steps)


print("example.txt")
print(" part 1:", solve_any("example.txt", False))  # 2
print("example2.txt")
print(" part 1:", solve_any("example2.txt", False))  # 6
print("input.txt")
print(" part 1:", solve_any("input.txt", False))  # 20777
print("example3.txt")
print(" part 2:", solve_any("example3.txt", True))  # 6
print("input.txt")
print(" part 2:", solve_any("input.txt", True))  # 13289612809129
