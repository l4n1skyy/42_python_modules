from abc import ABC, abstractmethod
from ex3 import Creature, TransformCapability


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, entity: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, entity: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, entity: Creature) -> bool:
        return True

    def act(self, entity: Creature) -> None:
        print(entity.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, entity: Creature) -> bool:
        return isinstance(entity, TransformCapability)

    def act(self, entity: Creature) -> None:
        if not isinstance(entity, TransformCapability):
            raise InvalidStrategyError(
                f"Invalid Creature '{type(entity).__name__}' "
                "for this aggressive strategy"
            )
        print(entity.transform())
        print(entity.attack())
        print(entity.revert())
