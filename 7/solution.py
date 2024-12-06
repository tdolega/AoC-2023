# 7 - Five of a kind, where all five cards have the same label: AAAAA
# 6 - Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# 5 - Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# 4 - Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# 3 - Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# 2 - One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# 1 - High card, where all cards' labels are distinct: 23456
def get_type_value(hand: str, is_joker_special: bool):
    counts = {}
    for card in hand:
        counts[card] = counts.get(card, 0) + 1
    joker_count = 0
    if is_joker_special and "J" in counts and counts["J"] < 5:
        joker_count += counts["J"]
        del counts["J"]
    values_sorted = sorted(counts.values(), reverse=True)
    values_sorted[0] += joker_count

    if values_sorted[0] == 5:
        return "7"
    elif values_sorted[0] == 4:
        return "6"
    elif values_sorted[0] == 3:
        if values_sorted[1] == 2:
            return "5"
        else:
            return "4"
    elif values_sorted[0] == 2:
        if values_sorted[1] == 2:
            return "3"
        else:
            return "2"
    return "1"


NORMAL_CARDS = "23456789TJQKA"
JOKER_CARDS = "J23456789TQKA"


def get_raw_value(hand: str, is_joker_special: bool):
    cards = JOKER_CARDS if is_joker_special else NORMAL_CARDS
    values = [str(cards.index(card)).zfill(2) for card in hand]
    return "".join(values)


def get_value(hand: str, is_joker_special: bool):
    raw_value = get_raw_value(hand, is_joker_special)
    hand_type = get_type_value(hand, is_joker_special)
    return int(f"{hand_type}{raw_value}")


def solve_any(filename: str, is_joker_special: bool):
    plays = []
    with open(filename) as f:
        for line in f:
            hand, bid = line.split()
            plays.append((hand, int(bid)))
    plays.sort(key=lambda x: get_value(x[0], is_joker_special))
    result = 0
    for i, play in enumerate(plays):
        hand, bid = play
        result += bid * (i + 1)
    return result


def solve(filename: str):
    print(filename)
    print(" part 1:", solve_any(filename, False))
    print(" part 2:", solve_any(filename, True))


solve("example.txt")  # 6440, 5905
solve("input.txt")  # 251287184, 250757288
