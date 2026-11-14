from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory
from ex4 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    InvalidStrategyError,
)

Opponent = tuple[CreatureFactory, BattleStrategy]


def battle(opponents: list[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    try:
        for i, (factory1, strategy1) in enumerate(opponents):
            for factory2, strategy2 in opponents[i + 1:]:
                fighter1 = factory1.create_base()
                fighter2 = factory2.create_base()
                print("\n* Battle *")
                print(fighter1.describe())
                print(" vs.")
                print(fighter2.describe())
                print(" now fight!")
                strategy1.act(fighter1)
                strategy2.act(fighter2)
    except InvalidStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")


def run_tournament(title: str, opponents: list[Opponent]) -> None:
    labels = []
    for factory, strategy in opponents:
        creature = type(factory.create_base()).__name__
        kind = type(strategy).__name__.replace("Strategy", "")
        labels.append(f"({creature}+{kind})")
    print(title)
    print(" [ " + ", ".join(labels) + " ]")
    battle(opponents)


if __name__ == "__main__":
    flame = FlameFactory()
    transform = TransformCreatureFactory()
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()

    run_tournament(
        "Tournament 0 (basic)", [(flame, normal), (transform, aggressive)]
    )
    print()
    run_tournament(
        "Tournament 1 (error)", [(transform, aggressive), (flame, aggressive)]
    )
