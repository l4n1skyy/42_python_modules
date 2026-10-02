def ft_plant_growth() -> None:
    rose = Plant("rose", 25.0, 30, 0.8)
    start_height = rose.height

    print("=== Garden Plant Growth ===")
    rose.show()

    for n in range(7):
        print(f"=== Day {n + 1} ===")
        rose.grow(1)
        rose.age(1)
        rose.show()

    end_height = rose.height

    print(f"Growth this week: {round(end_height - start_height, 1)}cm")


class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        days: int,
        rate: float = 1.0,
    ) -> None:

        self.name = name.capitalize()
        self.height = height
        self.days = days
        self.rate = rate

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days} days old")

    def grow(self, days: int) -> float:
        self.height = round(self.height + days * self.rate, 1)
        return self.height

    def age(self, days: int) -> int:
        self.days += days
        return self.days


if __name__ == "__main__":
    ft_plant_growth()
