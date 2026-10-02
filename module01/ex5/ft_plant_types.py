def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("red", "rose", 15.0, 10)
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("=== Tree")
    oak = Tree(5.0, "oak", 200.0, 365)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("=== Vegetable")
    tomato = Vegetable("April", "tomato", 5.0, 10, 2.1)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow(20)
    tomato.age(20)
    tomato.show()


class Plant:
    # Constructor
    def __init__(
        self,
        name: str = "Unknown",
        height: float = 1.0,
        age: int = 1,
        rate: float = 1.0,
    ) -> None:
        self._name = name.capitalize()

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
    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def grow(self, days: int) -> float:
        self._height = round(self._height + days * self._rate, 1)
        return self._height

    def age(self, days: int) -> int:
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


class Tree(Plant):
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

    def produce_shade(self) -> None:
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


if __name__ == "__main__":
    ft_plant_types()
