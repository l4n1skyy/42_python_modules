def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_age(400)}")

    print("=== Flower")
    rose = Flower("red", "rose", 15.0, 10, 8.0)
    rose.show()
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(1)
    rose.bloom()
    rose.show()
    display_stats(rose)

    print("=== Tree")
    oak = Tree(5.0, "oak", 200.0, 365)
    oak.show()
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_stats(oak)

    print("=== Seed")
    sunflower = Seed("yellow", "sunflower", 80.0, 45, 1.5)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(20)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_stats(sunflower)

    print("=== Anonymous")
    anon = Plant.anonymous()
    anon.show()
    display_stats(anon)


class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grow: int = 0
            self._age: int = 0
            self._show: int = 0

        def set_grow(self, grow: int) -> None:
            self._grow = grow

        def set_age(self, age: int) -> None:
            self._age = age

        def set_show(self, show: int) -> None:
            self._show = show

        def get_grow(self) -> int:
            return self._grow

        def get_age(self) -> int:
            return self._age

        def get_show(self) -> int:
            return self._show

        def display(self) -> None:
            print(
                f"Stats: {self._grow} grow,",
                f"{self._age} age,",
                f"{self._show} show",
            )

    # Constructor
    def __init__(
        self,
        name: str = "Unknown",
        height: float = 1.0,
        age: int = 1,
        rate: float = 1.0,
    ) -> None:
        self._name = name.capitalize()
        self._stats = Plant._Stats()

        if height < 0.0:
            print(f"{self._name}: Error, height can't be negative")
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
        if rate < 0.0:
            print(f"{self._name}: Error, rate can't be negative")

        self._height = height + 0.0 if height >= 0 else 1.0
        self._age = age if age >= 0 else 1
        self._rate = rate if rate >= 0.0 else 1.0

    # Methods
    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    @staticmethod
    def check_age(age: int) -> bool:
        return age > 365

    def show(self) -> None:
        self._stats.set_show(self._stats.get_show() + 1)
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def grow(self, days: int) -> float:
        self._stats.set_grow(self._stats.get_grow() + 1)
        self._height = round(self._height + days * self._rate, 1)
        return self._height

    def age(self, days: int) -> int:
        self._stats.set_age(self._stats.get_age() + 1)
        self._age += days
        return self._age

    # Getters
    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_rate(self) -> float:
        return self._rate

    def get_name(self) -> str:
        return self._name

    def get_stats(self) -> "Plant._Stats":
        return self._stats

    # Setters
    def set_height(self, height: float) -> None:
        if height >= 0.0:
            self._height = height + 0.0
            print(f"Height updated: {height}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
            print(f"Age updated: {age} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def set_rate(self, rate: float) -> None:
        if rate >= 0.0:
            self._rate = rate
        else:
            print(f"{self._name}: Error, rate can't be negative")
            print("Rate update rejected")

    def set_name(self, name: str) -> None:
        if name != "" and name != " ":
            self._name = name.capitalize()
        else:
            print(f"{self._name}: Error, name can't be empty")
            print("Name update rejected")


class Flower(Plant):
    def __init__(
        self,
        color: str,
        name: str = "Unknown",
        height: float = 1.0,
        age: int = 1,
        rate: float = 1.0,
    ) -> None:
        super().__init__(name, height, age, rate)
        self._bloomed: bool = False
        self._color: str = color

    @classmethod
    def anonymous(cls) -> "Flower":
        return cls("Unknown", "Unknown plant", 0.0, 0)

    def bloom(self) -> None:
        self._bloomed = True

    def get_bloomed(self) -> bool:
        return self._bloomed

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        print(
            f"{self._name} is blooming beautifully!"
            if self._bloomed
            else f"{self._name} has not bloomed yet"
        )


class Seed(Flower):
    def __init__(
        self,
        color: str,
        name: str = "Unknown",
        height: float = 1.0,
        age: int = 1,
        rate: float = 1.0,
    ) -> None:
        super().__init__(color, name, height, age, rate)
        self._seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


class Tree(Plant):
    class _Stats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade: int = 0

        def set_shade(self, shade: int) -> None:
            self._shade = shade

        def get_shade(self) -> int:
            return self._shade

        def display(self) -> None:
            super().display()
            print(f"{self._shade} shade")

    def __init__(
        self,
        trunk_diameter: float,
        name: str = "Unknown",
        height: float = 1.0,
        age: int = 1,
        rate: float = 1.0,
    ) -> None:
        super().__init__(name, height, age, rate)
        self._trunk_diameter: float = trunk_diameter
        self._tree_stats = Tree._Stats()
        self._stats = self._tree_stats

    @classmethod
    def anonymous(cls) -> "Tree":
        return cls(0.0, "Unknown plant", 0.0, 0)

    def produce_shade(self) -> None:
        self._tree_stats.set_shade(self._tree_stats.get_shade() + 1)
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height}cm long and {self._trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(
        self,
        harvest_season: str,
        name: str = "Unknown",
        height: float = 1.0,
        age: int = 1,
        rate: float = 1.0,
    ) -> None:
        super().__init__(name, height, age, rate)
        self._nutritional_value: int = 0
        self._harvest_season = harvest_season

    @classmethod
    def anonymous(cls) -> "Vegetable":
        return cls("Unknown", "Unknown plant", 0.0, 0)

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")

    def grow(self, days: int) -> float:
        height = super().grow(days)
        self._nutritional_value += days // 2
        return height

    def age(self, days: int) -> int:
        age = super().age(days)
        self._nutritional_value += days // 2
        return age


def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant.get_stats().display()


if __name__ == "__main__":
    ft_garden_analytics()
