import time


def part1(puzzle_input):
    lines = puzzle_input.split("\n")
    point_sum = 0
    for line in lines:
        _, numbers = line.split(":")
        winning_nums, our_nums = numbers.split("|")
        winning_set = set(winning_nums.split())
        our_set = set(our_nums.split())

        matches = len(winning_set.intersection(our_set))
        points = int(pow(2, matches - 1))
        point_sum += points

    return point_sum


def part2(puzzle_input):
    lines = puzzle_input.split("\n")
    card_list = []
    for line in lines:
        _, numbers = line.split(":")
        winning_nums, our_nums = numbers.split(" | ")
        winning_set = set(winning_nums.split())
        our_set = set(our_nums.split())

        matches = len(winning_set.intersection(our_set))
        card_list.append([int(matches), 1])

    score = 0
    for card_id, (matches, amount_of_cards) in enumerate(card_list):
        score += amount_of_cards
        for new_card_id in range(card_id + 1, card_id + 1 + matches):
            card_list[new_card_id][1] += amount_of_cards

    return score


if __name__ == '__main__':
    day = 4
    with open(rf'../Input/day{day}.txt', 'r') as f:
        puzzle_read = f.read()

    timer_start = time.perf_counter()
    result = part1(puzzle_read)
    print(f"Day {day}, Part 1 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")

    timer_start = time.perf_counter()
    result = part2(puzzle_read)
    print(f"Day {day}, Part 2 result is: {result}, computed in: {time.perf_counter() - timer_start:.3} seconds")
