import random


def first_list_comprehension(players: list) -> list:
    return [p.capitalize() for p in players]


def second_list_comprehension(players: list) -> list:
    return [p for p in players if p == p.capitalize()]


def third_dict_comprehension(players: list) -> dict:
    return {k: random.randint(0, 100) for k in players}


def fourth_dict_comprehension(scores: dict, avg: float) -> dict:
    return {k: scores[k] for k in scores if scores[k] > avg}


def avg(scores: dict) -> float:
    return round(sum(scores.values()) / len(scores), 2)


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    players = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]
    print(f"\nInitial list of players: {players}")
    first_list = first_list_comprehension(players)
    print(f"New list with all names capitalized: {first_list}")
    second_list = second_list_comprehension(players)
    print(f"New list of capitalized names only: {second_list}")

    scores = third_dict_comprehension(first_list)
    print(f"\nScore dict: {scores}")
    average = avg(scores)
    print(f"Score average is {average}")
    high = fourth_dict_comprehension(scores, average)
    print(f"High scores: {high}")
