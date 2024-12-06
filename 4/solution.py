def solve(filename: str):
    print(filename)
    with open(filename) as f:
        lines = f.readlines()

    points = 0
    card_count = {}
    for line in lines:
        card_id, numbers = line.split(":")
        card_id = int(card_id[5:])
        card_count[card_id] = card_count.get(card_id, 0) + 1
        winning_numbers, got_numbers = numbers.split("|")
        winning_numbers = set(winning_numbers.split())
        got_numbers = set(got_numbers.split())
        n_hits = len(winning_numbers.intersection(got_numbers))
        for i in range(card_id + 1, card_id + n_hits + 1):
            card_count[i] = card_count.get(i, 0) + card_count[card_id]
        if n_hits > 0:
            points += 2 ** (n_hits - 1)

    print(" part 1:", points)
    print(" part 2:", sum(card_count.values()))


solve("example.txt")  # 13, 30
solve("input.txt")  # 18653, 5921508
