import random

ACHIEVEMENTS = [
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "Strategist",
    "Unstoppable",
    "Speed Runner",
    "Survivor",
    "Treasure Hunter",
    "First Steps",
    "Sharp Mind",
    "Hidden Path Finder",
]

LEN = len(ACHIEVEMENTS)


def gen_player_achievements() -> set[str]:
    count = random.randint(round(LEN * 0.4), round(LEN * 0.75))
    return set(random.sample(ACHIEVEMENTS, count))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")

    pool = set(ACHIEVEMENTS)
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"\nPlayer Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    everyone = alice.union(bob, charlie, dylan)
    print(f"\nAll distinct achievements: {everyone}")

    common = alice.intersection(bob, charlie, dylan)
    print(f"\nCommon achievements: {common}")

    print(f"\nOnly Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}")

    print(f"\nAlice is missing: {pool.difference(alice)}")
    print(f"Bob is missing: {pool.difference(bob)}")
    print(f"Charlie is missing: {pool.difference(charlie)}")
    print(f"Dylan is missing: {pool.difference(dylan)}")
