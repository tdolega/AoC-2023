def merge_layers(map1: list[tuple[int, int, int]], map2: list[tuple[int, int, int]]):
    merged_map = []
    for minimum, maximum, diff in map1:
        for minimum2, maximum2, diff2 in map2:
            out_min = max(minimum, minimum2 - diff)
            out_max = min(maximum, maximum2 - diff)
            if out_min <= out_max:
                merged_map.append((out_min, out_max, diff + diff2))
    return merged_map


def answer(seeds: list[int], layers: list[list[tuple[int, int, int]]]):
    result = float("inf")
    for minimum, maximum, diff in layers:
        for min_seed, length_seed in zip(seeds[::2], seeds[1::2]):
            max_seed = min_seed + length_seed
            min_cond = max(minimum, min_seed)
            max_cond = min(maximum, max_seed)
            if min_cond <= max_cond:
                result = min(result, min_cond + diff)
    return result


def solve(filename: str):
    print(filename)
    with open(filename, "r") as f:
        lines = f.readlines()

    layers = []
    current_map_idx = -1
    for line in lines[1:]:
        parts = line.split()
        if len(parts) == 2:
            current_map_idx += 1
            layers.append([])
        elif len(parts) == 3:
            mapping = [int(part) for part in parts]
            destination, source, length = mapping
            mapping = (source, source + length, destination - source)
            layers[current_map_idx].append(mapping)

    for i, layer in enumerate(layers):
        layers[i].sort(key=lambda x: x[0])
        layers[i] = [(0, layer[0][0], 0)] + layer + [(layer[-1][1], float("inf"), 0)]

    merged_layers = layers[0]
    for layer in layers[1:]:
        merged_layers = merge_layers(merged_layers, layer)
    merged_layers = [mapping for mapping in merged_layers if mapping[0] < mapping[1]]

    seeds = lines[0].split()[1:]
    seeds = [int(seed) for seed in seeds]
    answer_2 = answer(seeds, merged_layers)

    seeds = [[seed, 1] for seed in seeds]
    seeds = [item for sublist in seeds for item in sublist]
    answer_1 = answer(seeds, merged_layers)

    print(" part 1:", answer_1)
    print(" part 2:", answer_2)


solve("example.txt")  # 35, 46
solve("input.txt")  # 600279879, 20191102
