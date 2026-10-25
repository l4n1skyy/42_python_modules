import typing
import random


def gen_event(
    players: list,
    actions: list,
) -> typing.Generator[tuple, None, None]:
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(events: list[tuple]) -> typing.Generator[tuple, None, None]:
    while events:
        rand = random.randint(0, len(events) - 1)
        e = events.pop(rand)
        yield e


if __name__ == "__main__":
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "release",
        "use",
    ]
    gen = gen_event(players, actions)
    print("=== Game Data Stream Processor ===")
    for n in range(1000):
        k = next(gen)
        print(f"Event {n}: Player {k[0]} did action {k[1]}")

    ten_events = [next(gen) for _ in range(10)]
    print(f"Built list of 10 events: {ten_events}")

    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")
