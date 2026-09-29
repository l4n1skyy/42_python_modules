def ft_plant_factory() -> None:
    rose = Plant("rose", 25.0, 30)
    oak = Plant("oak", 200.0, 365)
    cactus = Plant("cactus", 5.0, 90)
    sunflower = Plant("sunflower", 80.0, 45)
    fern = Plant("fern", 15.0, 120)
    plants = [rose, oak, cactus, sunflower, fern]
    print("=== Plant Factory Output ===")
    for i in range(5):
        print("Created: ", end="")
        plants[i].show()


class Plant:
    def __init__(self, name: str, height: float, days: int, rate: float = 1.0) -> None:

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
    ft_plant_factory()
